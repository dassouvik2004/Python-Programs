import string

def countOccurances(text):
    text = text.translate(str.maketrans("","",string.punctuation)) #Remove any special character (, . ; '') into none
    word = text.split() # Split the text into word. Ep, "apple, mango, apple" -> ['apple','mango','apple']
    uniqueWord = set(word) # Convert it into set because set removes any duplicate. Ep, ['apple','mango','apple'] -> {'apple','mango'}
    wordCount = {} # Create a dictionary

    for unique_words in uniqueWord: # itarates individual word in UniqueWord
        count = 0 # For counting number of occurance
        for w in word: # itarates individual word in word(which split text into word)
            if w.lower() == unique_words.lower(): # Comparing both are equal or not
                count += 1 # counts every occurances
        wordCount[unique_words.lower()] = count # then convert it into key and value and assign in the dictionary
    return wordCount # returns dictionary 

text = input("Enter a string: ")

occuarances = countOccurances(text)

print(occuarances)