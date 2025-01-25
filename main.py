def main():
    print("\n---Reporting of Frankenstein---\n")
    file_contents = getText()

    words = getWords(file_contents)
    alpha = getChars(file_contents)

    printReport(alpha, words)

def getText():
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def getWords(text):
    return text.split()

def getChars(text):
    alpha = dict()
    text_len = (len(text))
    text = text.lower()

    for i in range(0, text_len):
        ch = text[i]
        if ch not in alpha:
            alpha[ch] = 1
        else:
            alpha[ch] += 1
    return alpha

def printReport(alpha, words):
    print(f"{len(words)} words found in the document\n")
    alpha = list(alpha.items())
    alpha.sort(key=lambda x: x[1], reverse=True)
    for i in range(0, len(alpha)):
        if (alpha[i][0].isalpha()):
            print(f"The '{alpha[i][0]}' character was found {alpha[i][1]} times")
    print("\n---End of Report---\n")

def sort_key(dict):
    return dict[""]
main()