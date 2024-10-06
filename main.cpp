#include <iostream>
#include <string>
#include "cstdint"
#include <fstream>
#include <filesystem>
#include "vector"
#ifdef _WIN32
#include <windows.h>
#endif
#ifdef __linux__
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#endif
#include "read_bytes.h"

using namespace std;
namespace fs = filesystem;
const string windows_path = R"(C:\Users\{user}\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\)";
const string linux_path = "/home/{user}/.steam/steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/";
const string backup_linux_path = "/run/media/{user}/SteamLibrary/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/";

string get_blueprint_path() {
    // Returns the path to the blueprint folder
    string path;
#ifdef _WIN32
    char username[UNLEN+1];
    DWORD username_len = UNLEN+1;
    GetUserName(username, &username_len);
    path = windows_path;
    path.replace(path.find("{user}"), 6, username);
    cout << path << endl;
#endif
#ifdef __linux__
    path = linux_path;
    const string username = getenv("USER");
    path.replace(path.find("{user}"), 6, username);
    cout << path << endl;
#endif
    fs::path FilePath = path;
    if (fs::exists(FilePath)) {
        cout << "Path exists" << endl;
    } else {
        cout << "Path does not exist" << endl;
#ifdef __linux__
        path = backup_linux_path;
        path.replace(path.find("{user}"), 6, username);
        cout << path << endl;
        FilePath = path;
        if (fs::exists(FilePath)) {
            cout << "Backup Path exists" << endl;
        } else {
            cout << "Backup Path does not exist" << endl;
            return "";
        }
    }
#endif
    return path;
}
vector<string> get_saves(const string &path) {
    // Returns a list of saves
    if (path.empty()) {
        return {};
    }
    vector<string> saves;
    for (const auto &entry: fs::directory_iterator(path)) {
        saves.push_back(entry.path().filename());
    }
    return saves;
}
vector<string> get_save_blueprints(const string &path, const string &savename) {
    // Returns a list of blueprints for a save
    if (savename.empty()) {
        return {};
    }
    vector<string> blueprints;
    try {
        for (const auto &entry: fs::directory_iterator(path + savename)) {
            if (entry.path().filename().string().ends_with(".sbp")) blueprints.push_back(entry.path().filename().string().erase(entry.path().filename().string().size() - 4)); // remove .sbp
        }
    } catch (const fs::filesystem_error& e) {
        return {};
    }
    return blueprints;
}

vector<byte> open_blueprint(const string &path, const string &savename, const string &blueprint) {
//    https://github.com/etothepii4/satisfactory-file-parser/blob/main/src/parser/parser.ts
// Returns an uint8 array of the blueprint file
    fs::path file_path = path+savename+"/"+blueprint+".sbpcfg";
    if (!fs::exists(file_path)) {
        throw runtime_error("File does not exist");
    }
    vector<byte> buffer;
    ifstream file(file_path, ios::binary);
    if (file.is_open()) {
        file.seekg(0, ios::end);
        size_t size = file.tellg();
        file.seekg(0, ios::beg);
        buffer.resize(size);
        file.read(reinterpret_cast<char*>(buffer.data()), size);
        file.close();
    } else {
        cout << "Failed to open file" << endl;
        throw fs::filesystem_error("Failed to open file", file_path, error_code());
    }
    cout << "File size: " << buffer.size() << endl;
    return buffer;
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    const string path = get_blueprint_path();
    if (path.empty()) {
        cout << "Path is empty" << endl;
        return 1;
    }
    cout << "Detected saves:" << endl;
    for (const string& name : get_saves(path)) {
        cout << name << endl;
    }
    cout << "Enter save name: ";
    string savename;
    getline(cin, savename);
    cout << "Detected blueprints for save " << savename << ":" << endl;
    auto blueprints = get_save_blueprints(path, savename);
    if (blueprints.empty()) {
        cout << "No blueprints found. Did you spell the save correctly?" << endl;
        return 1;
    }
    for (const string& name : blueprints) {
        cout << name << endl;
    }
    cout << "Enter blueprint name: ";
    string blueprint;
    getline(cin, blueprint);
    vector<byte> parsed_bp = open_blueprint(path, savename, blueprint);
    cout << "Parsed blueprint:" << endl;
    for (byte i : parsed_bp) {
        cout << static_cast<int>(i) << " ";
    }
    cout << endl;
    cout << "First int:" << endl;
    auto parser = ByteReader(parsed_bp);
    cout << parser.readInt32() << endl;
    cout << "Description:" << endl;
    cout << parser.readString() << endl;
    cout << "Icon ID:" << endl;
    cout << parser.readInt32() << endl;
    cout << "Color: (RGBA)" << endl; // RGBA
    cout << parser.readInt32() << " " << parser.readInt32() << " " << parser.readInt32() << " " << parser.readInt32() << endl;
    parser.position -= 16;
    cout << "Color: (HEX)" << endl;
    cout << "#" << parser.readHex() << parser.readHex() << parser.readHex() << parser.readHex() << endl;
    cout << "Length:" << endl;
    cout << parser.position << " out of: " << parser.bytestream.size() << endl;

    return 0;
}
