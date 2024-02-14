
path = "Sample.txt"
# make a set of all words in file
set_words = set()
# make a dictionary where word is key and value is the frequency of the word in the given file
word_frequency = {}
with open(path) as file:
    for word in file.read().split():
        word = word.replace(".","")
        set_words.add(word.lower())
    
    for word in set_words:
        word_frequency[word] = 0
    
    # return reading position to beginning of file
    file.seek(0)

    for word in file.read().split():
        word = word.replace(".","")
        word_frequency[word.lower()] +=1
    
for key,value in word_frequency.items():
    print(f"{key} : {value}")
