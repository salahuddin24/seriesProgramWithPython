# list as input from user
# n = input("inter a text of numbers : ")
# list = n.split()
#
# print(list)
# sum = 0
# for num in list :
#     sum = sum + int(num)
# print( "sum of list item is : ",sum)


#-----------------
numOfWords = 0
numOfLetters = 0
numOfDigits = 0
text = input("Enter any sentence with digits : ")

for x in text :
    x = x.lower()
    if x >= 'a' and x <= 'z' :
        numOfLetters = numOfLetters + 1
    elif x >= '0' and x <= '9' :
        numOfDigits = numOfDigits + 1
    elif x == ' ':
        numOfWords = numOfWords + 1


print(numOfLetters)
print(numOfWords + 1)
print(numOfDigits)









