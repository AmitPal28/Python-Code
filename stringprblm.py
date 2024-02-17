# Problem1: Display Nonrepeated char in a word
word = input("Enter a string:").lower()

for char in word:
    # print(char)
    if word.count(char) == 1:
        print("Non-repeated char is:",char)
        