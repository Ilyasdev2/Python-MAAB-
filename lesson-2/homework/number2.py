try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(max(num1, num2, num3), min(num1, num2, num3))   
except:
    print('Enter valid numbers')