def main():
    usr_input = input()
    if __import__("base64").b85encode(__import__("zlib").compress(usr_input.encode())) == REPLACE_ME_WITH_FLAG.encode():
        print("correct flag!")


main()
