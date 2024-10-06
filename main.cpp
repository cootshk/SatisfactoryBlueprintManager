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
using namespace std;
namespace fs = filesystem;
string windows_path = R"(C:\Users\{user}\AppData\Local\FactoryGame\Saved\SaveGames\blueprints\)";
string linux_path = "/home/{user}/.steam/steam/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/";
string backup_linux_path = "/run/media/{user}/SteamLibrary/steamapps/compatdata/526870/pfx/drive_c/users/steamuser/AppData/Local/FactoryGame/Saved/SaveGames/blueprints/";

string get_blueprint_path() {
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
    if (path.empty()) {
        return {};
    }
    vector<string> saves;
    for (const auto &entry: fs::directory_iterator(path)) {
        saves.push_back(entry.path().filename());
    }
    return saves;
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


    return 0;
}
