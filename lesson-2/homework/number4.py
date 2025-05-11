try:
    num1 = int(input())
    num2 = int(input())
    num3 = divmod(num1, num2)
    print(num3[0], num3[1])
except:
    print('Enter valid numbers')
