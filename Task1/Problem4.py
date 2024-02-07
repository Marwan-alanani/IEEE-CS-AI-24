def main():
    sentence = input().split()
    reversedSentence = ""
    for i in range(len(sentence)-1,-1,-1):
        reversedSentence += sentence[i]+" "
    print(reversedSentence)
main()