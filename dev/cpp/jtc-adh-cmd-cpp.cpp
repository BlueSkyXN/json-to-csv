#include <iostream>
#include <fstream>
#include <cstring>
#include "json.hpp"

using json = nlohmann::json;

#define BUFFER_SIZE 1024

// 将JSON对象转换为CSV格式的字符串，并追加到缓冲区中
void json_to_csv(const json& j, std::string& buffer) {
    if (j.is_array()) {
        for (auto& subitem : j) {
            json_to_csv(subitem, buffer);
        }
    } else if (j.is_object()) {
        int first_item = 1;
        for (auto& [key, value] : j.items()) {
            if (!first_item) {
                buffer += ",";
            }
            buffer += key;
            buffer += ",";
            if (value.is_number()) {
                buffer += std::to_string(value.get<double>());
            } else if (value.is_string()) {
                buffer += "\"";
                buffer += value.get<std::string>();
                buffer += "\"";
            } else {
                json_to_csv(value, buffer);
            }
            first_item = 0;
        }
        buffer += "\n";
    }
}

int main() {
    std::string buffer;
    json j;
    std::ifstream infile("my_large_json_file.json");
    if (!infile.is_open()) {
        std::cerr << "Failed to open JSON file." << std::endl;
        return 1;
    }

    // 按块读取JSON文件并解析为JSON对象
    char chunk[BUFFER_SIZE];
    while (infile.read(chunk, BUFFER_SIZE)) {
        auto len = infile.gcount();
        chunk[len] = '\0';
        try {
            j = json::parse(chunk);
            json_to_csv(j, buffer);
        } catch (std::exception& e) {
            std::cerr << "Failed to parse JSON: " << e.what() << std::endl;
            return 1;
        }
    }
    infile.close();

    // 将转换后的CSV字符串写入文件中
    std::ofstream outfile("my_output.csv");
    if (!outfile.is_open()) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }
    outfile.write(buffer.c_str(), buffer.length());
    outfile.close();

    return 0;
}
