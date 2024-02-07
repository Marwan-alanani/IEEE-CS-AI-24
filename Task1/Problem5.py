def main():
    word = input()
    if palindrome(word):
        print("The word '"+word+"' is a palindrome")
    else:
        print("The word '"+word+"' is not a palindrome")


def palindrome(word):
    word = word.lower()
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True  
main()