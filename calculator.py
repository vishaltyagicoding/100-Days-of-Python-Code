def add(first_num, second_num):
    total = first_num + second_num
    return total


def sub(first_num, second_num):
    total = first_num - second_num
    return total


def mult(first_num, second_num):
    total = first_num * second_num
    return total


def div(first_num, second_num):
    total = first_num / second_num
    return total


num1 = int(input("Enter first number? "))
op = input("Enter operator? Type '+', '-', '*' and '/' ")
num2 = int(input("Enter second number? "))

result = 0
if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = sub(num1, num2)
elif op == "*":
    result = mult(num1, num2)

elif op == "/":
    result = div(num1, num2)

print(f"{num1} {op} {num2} = {result}")
