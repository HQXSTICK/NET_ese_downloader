#include <fstream>
#include <iostream>

using namespace std;

string num, local, _local;

void Powershell() {
  ofstream file;
  file.open("test.ps1");
  string newArg = "-auto";
  string powershell;
  powershell += "$WebClient = New-Object System.Net.WebClient\n$WebClient.DownloadFile(\"http://music.163.com/song/media/outer/url?id=";
  powershell += num;
  powershell += ".mp3\",\"";
  powershell += local;
  powershell += "\")\n";
  file << powershell;
  file.close();
  system("powershell -ExecutionPolicy Bypass -F test.ps1");
  remove("test.ps1");
}

int main() {
  ifstream fin("out.txt");
  fin >> _local;
  for (int i = 1; num != "0"; i++) {
    fin >> num;
    local = _local + "\\";
    local += "NeteaseMusic#" + num + ".mp3";
    if (num != "0") {
      Powershell();
    }
    cout << "[Task " << i << " success]\n";
  }
  return 0;
}
