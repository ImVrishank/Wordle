import random


word_file = open("words.txt", "r") 
# reading the file 
words = word_file.read() 
  
# replacing end splitting the text  
# when newline ('\n') is seen. 
words = words.split("\n") 

word = words[random.randint(0,len(words)-1)]

print(word)