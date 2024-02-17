# Problem1: Display Nonrepeated char in a word
wordFirst = input("Enter a word: ").lower()

for char in wordFirst:
    # print(char)
    if wordFirst.count(char) == 1:
        print("Non-repeated char is:",char)
    
    
# Problem2: Display First Nonrepeated char in a word

wordSecond = input("Enter a word: ").lower()

for char in wordSecond:
    # print(char)
    if wordSecond.count(char) == 1:
        print("Non-repeated char is:",char)
        break
    
# Problem3: Display Reverse of word using loop
wordThird = input("Enter a word: ")
revWord = ""

for c in wordThird:
    revWord = c + revWord
print("Reverse of word is: ",revWord)