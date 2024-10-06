# 1 + 2 + 3 + 4 + 5 + ... + n
# 2 + 4 + 6 + 8 + .....+ n
# 1 + 3 + 5 + 7 + .....+n
# 4 + 8 + 12 + ..... + n

# n = int(input("Enter the last number : "))
# sum = 0
# for x in range(1 , n+1, 1) :
#     sum  = sum + x
# print(sum)

# 1^2 + 2^2 + 3^2 + .... + n^2

# lastNum = int(input("Enter the last number :"))
# sum2 = 0
# for x in range(1, lastNum+1, 1):
#     sum2 = sum2 + x*x
# print(sum2)

### 2^2 + 4^2 + 6^2 + .... + n^2
# 1 + 1/2 + 1/3 + .....+ 1/n


# # 2*4*6*....*n
# num3 = int(input("Enter the last number :"))
# sum3 = 1
# for x in range(2, num3+1, 2):
#     sum3 = sum3 * x
# print(sum3)


# petarn solve
"""
*
**
*** 
****
"""
# n = 5
# for i in range(n+1) :
#     print(i*"*")


from random import randint

for x in range(1, 6) :
    guessNum = int(input("Enter your guess between 1 to 5 : "))
    randomNum = randint(1, 5)

    if guessNum == randomNum :
        print("You have won !")
    else :
        print("You have lost")
        print("randon number was :", randomNum)














