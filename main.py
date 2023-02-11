print("\t\t\t\t\t\t\t\t\t\tWelcome to the CCCCCCOOOO__parser!\n\n\n")


if __name__ == "__main__":
    to_compile_str = ''
    with open("parse_this.py") as c_file:
        to_compile_str = c_file.read().strip()

    all_keywords = []
    with open('all_keywords.txt', 'r') as keywords_file:
        for word in keywords_file:
            all_keywords.append(word.strip())
    print(to_compile_str, "\n")
    print(all_keywords)
