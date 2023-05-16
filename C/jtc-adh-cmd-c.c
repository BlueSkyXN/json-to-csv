#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cJSON.h"

#define BUFFER_SIZE 1024

// 将JSON对象转换为CSV格式的字符串，并追加到缓冲区中
void json_to_csv(cJSON *json, char *buffer, int *len) {
    if (cJSON_IsArray(json)) {
        cJSON *subitem = json->child;
        while (subitem != NULL) {
            json_to_csv(subitem, buffer, len);
            subitem = subitem->next;
        }
    } else if (cJSON_IsObject(json)) {
        cJSON *subitem = json->child;
        int first_item = 1;
        while (subitem != NULL) {
            if (!first_item) {
                strcat(buffer, ",");
                (*len)++;
            }
            strcat(buffer, subitem->string);
            strcat(buffer, ",");
            (*len) += strlen(subitem->string) + 1;

            if (cJSON_IsNumber(subitem)) {
                char num_buf[32];
                snprintf(num_buf, sizeof(num_buf), "%.2f", subitem->valuedouble);
                strcat(buffer, num_buf);
                (*len) += strlen(num_buf);
            } else if (cJSON_IsString(subitem)) {
                strcat(buffer, "\"");
                strcat(buffer, subitem->valuestring);
                strcat(buffer, "\"");
                (*len) += strlen(subitem->valuestring) + 2;
            }

            first_item = 0;
            subitem = subitem->next;
        }
        strcat(buffer, "\n");
        (*len)++;
    }
}

int main() {
    char buffer[BUFFER_SIZE];
    int len = 0;
    cJSON *json = NULL;
    FILE *fp = fopen("my_large_json_file.json", "r");
    if (fp == NULL) {
        printf("Failed to open JSON file.\n");
        return 1;
    }

    // 按块读取JSON文件并解析为JSON对象
    while (!feof(fp)) {
        char chunk[BUFFER_SIZE];
        size_t read_len = fread(chunk, sizeof(char), BUFFER_SIZE, fp);
        if (read_len > 0) {
            json = cJSON_Parse(chunk);
            if (json != NULL) {
                json_to_csv(json, buffer, &len);
                cJSON_Delete(json);
            }
        }
    }
    fclose(fp);

    // 将转换后的CSV字符串写入文件中
    fp = fopen("my_output.csv", "w");
    if (fp == NULL) {
        printf("Failed to open output file.\n");
        return 1;
    }
    fwrite(buffer, len, 1, fp);
    fclose(fp);

    return 0;
}
