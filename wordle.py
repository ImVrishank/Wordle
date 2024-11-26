
def linear_search(arr, to_search):
    index = -1
    for item in arr:
        if item == to_search:
            pass

#boxes :
#⬜⬜⬜ gray instead of white
#🟨🟨🟨
#🟩🟩🟩

word = "hello"
guess = ""
op = ""
tries = 0
max_tries = 6
letter_list = []


while(guess != word and tries < max_tries):
    guess = input("enter your guess: ")
    print("your current progress: ")

    for index in range(0,5):
        #if letters in both the word and guess are matching
        if word[index] == guess[index]:
            op += "🟩"
        #add the yellow boxes later, this is just checking for indexing
        else:
            op += "⬜"
    
    print(op)
    #if guess is perfect
    if op == "🟩🟩🟩🟩🟩":
        print(f"well played! you guessed it in {tries} tries")
        break

    op = ""
    tries += 1

if tries == max_tries:
    print("better luck next time!")