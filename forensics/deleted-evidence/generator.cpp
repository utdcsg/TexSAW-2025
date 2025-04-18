#include <cstdlib>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <openssl/sha.h>

void hash_SHA256(unsigned char hash[], const std::string& message) {
    SHA256_CTX sha256_ctx;
    SHA256_Init(&sha256_ctx);
    SHA256_Update(&sha256_ctx, message.c_str(), message.length());
    SHA256_Final(hash, &sha256_ctx);
    return;
}

int main() {
    int count = 0;
    while(true) {
        // last seed is 89
        std::string file_name;
        std::cout << "Enter seed file name:\n";
        std::cin >> file_name;

        if(!std::filesystem::exists(file_name)) {
            std::cerr << "File does not exist!\n";
            return -1;
        }

        std::ifstream seed_file;
        std::string seed;
        seed_file.open(file_name);
        if(!std::getline(seed_file, seed)) {
            std::cerr << "No seed in file!\n";
            seed_file.close();
            return -1;
        }
        seed_file.close();

        const int hlen = SHA256_DIGEST_LENGTH;
        unsigned char hash[hlen];
        char hex_hash[hlen*2+1];
        hash_SHA256(hash, seed);

        for(int i=0; i<hlen; i++) {
            sprintf(hex_hash+i*2, "%02x", hash[i]);
        }
        hex_hash[hlen*2] = '\0';

        FILE* flag;
        flag = fopen("flag.txt", "w");
        fprintf(flag, "texsaw{");
        fprintf(flag, hex_hash);
        fprintf(flag, "}");
        fclose(flag);
        //flag("flag" + std::to_string(count) + ".txt");
        //std::cout << "texsaw{" << hex_hash << "}\n";
        //flag << "texsaw{";
        //flag << hex_hash;
        //flag << "}\n";
        //flag.close();

        memset(hash, 0, hlen);
        memset(hex_hash, 0, hlen*2+1);
        count++;
    }  

    return 0;
}
