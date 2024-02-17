# Problem1: Display Nonrepeated char in a word
wordFirst = input("Enter a string:").lower()

for char in wordFirst:
    # print(char)
    if wordFirst.count(char) == 1:
        print("Non-repeated char is:",char)
    
    
# Problem2: Display First Nonrepeated char in a word

wordSecond = input("Enter a string:").lower()

for char in wordSecond:
    # print(char)
    if wordSecond.count(char) == 1:
        print("Non-repeated char is:",char)
        break