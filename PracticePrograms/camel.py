### Daniel Bittner September 2025
### Program to convert a sentence to camel case

def camelcase(sentence):
    title_case = sentence.title()
    upper_camel_case = title_case.replace(" ", "")
    return upper_camel_case[o:1].lower() + upper_camel_case[1:]

def main():
    sentence = input("Enter your sentence: ")
    output = camelcase(sentence)
    print(output)

if __name__ == "__main__":
    main()