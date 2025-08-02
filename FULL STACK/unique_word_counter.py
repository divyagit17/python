sentence = input("Enter a sentence: ")

words = sentence.split()
lowercase_words =   [word.lower() for word in words]
unique_words = set(lowercase_words)


print("Number of unique words:", len(unique_words))
print("unique words found:")
for word in unique_words:
    print(word)
    
