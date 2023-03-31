#include <stdio.h>
#include <string.h>

int constants[] = {0x40, 0x41, 0x42};
const int flag_length = 29;
char raw[] = {0x122, 0x124, 0x128, 0x126, 0x134, 0x138, 0x127, 0x122, 0x125, 0x12a, 0x122, 0x12f, 0x138, 0x170, 0x139, 0x177, 0x124, 0x17a, 0x12d, 0x171, 0x114, 0x172, 0x172, 0x114, 0x127, 0x177, 0x13b, 0x170, 0x13a};
char flag[29];
char test[] = "hope you are doing good";

void init_constants() {
    for (int i = 0; i < 3; i++) {
        constants[i] = ((constants[i] << 2) | (constants[i] >> 6))^0x42;
    }
}

void generate_flag() {
    for (int i = 0; i < flag_length; i++) {
        flag[i] = raw[i] ^ constants[i % 3];
    }
}

int main() {
    init_constants();
    generate_flag();
    printf("Please enter the flag: ");
    char input[100];
    scanf("%s", input);
    if (strcmp(input, flag) == 0) {
        printf("Correct!\n");
    } else if (strcmp(input, "accessdenied{its_not_that_easy_hehehe}")) {
        printf("You are not supposed to see this!\n");
    } else {
        printf("Wrong!\n");
    }
    
    return 0;
}