import string
path = "Sample.txt" 
# make a set of all words in file
set_words = set()
# make a dictionary where word is the key, and value is the frequency of the word in the given file
word_frequency = {}
with open(path) as file:
    for word in file.read().split():
        # remove punctuation
        for punct in string.punctuation:
            word = word.replace(punct,"")
        # if string was only made up of punctuation we shouldn't add it
        if word:
            set_words.add(word.lower())
    
    for word in set_words:
        word_frequency[word] = 0
    
    # return reading position to beginning of file
    file.seek(0)

    for word in file.read().split():
        for punct in string.punctuation:
            word = word.replace(punct,"")
        if word:
            word_frequency[word.lower()] +=1
    
for key,value in word_frequency.items():
    print(f"{key} : {value}")
