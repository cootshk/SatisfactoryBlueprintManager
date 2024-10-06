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
#include "icon_ids.h"

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
struct BlueprintConfigContents {
    vector<byte>* raw{};
    ByteReader* parser{};
    string Name;
    string Description;
    int IconID{};
    string IconName;
    int ColorR{};
    int ColorG{};
    int ColorB{};
    int ColorA{};
    string ColorHex;
    string IconLibrary;
    string IconLibraryType;
};
BlueprintConfigContents parse_blueprint(const string& path, const string& savename, const string& blueprint) {
    /*
     * Byte order:
     * Always 2 (we don't know): Int32
     * Description: String
     * Icon ID: Int32
     * ColorR: Int32
     * ColorG: Int32
     * ColorB: Int32
     * ColorA: Int32
     * Optional:
     * Icon Library: String
     * Icon Library Type: String
     */
    auto parsed_bp = open_blueprint(path, savename, blueprint);
    auto parser = ByteReader(parsed_bp);
    BlueprintConfigContents contents;
    contents.raw = &parsed_bp;
    contents.parser = &parser;
    contents.Name = blueprint;
    parser.readInt32(); // Skip over the first int which is always 2 for some reason
    contents.Description = parser.readString();
    contents.IconID = parser.readInt32();
    contents.IconName = get_icon_name(contents.IconID);
    contents.ColorR = parser.readInt32();
    contents.ColorG = parser.readInt32();
    contents.ColorB = parser.readInt32();
    contents.ColorA = parser.readInt32();
    contents.ColorHex = parser.readHex() + parser.readHex() + parser.readHex() + parser.readHex();
    try {
        contents.IconLibrary = parser.readString();
        contents.IconLibraryType = parser.readString();
    } catch(const runtime_error& e) {
//        cout << e.what() << endl;
        contents.IconLibrary = "";
        contents.IconLibraryType = "";
    }
    return contents;
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
    auto contents = parse_blueprint(path, savename, blueprint);
    cout << "Name: " << contents.Name << endl;
    cout << "Description: " << contents.Description << endl;
    cout << "Icon ID: " << contents.IconID << endl;
    cout << "Icon Name: " << contents.IconName << endl;
    cout << "Color: (RGBA) " << contents.ColorR << " " << contents.ColorG << " " << contents.ColorB << " " << contents.ColorA << endl;
    cout << "Color: (HEX) " << "#" + contents.ColorHex << endl;

    return 0;
}
