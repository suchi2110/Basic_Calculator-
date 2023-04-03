num1 = float(input('enter your first number'))
num2 = float(input('enter your second number'))
operator = input('enter which operation you want to do')

if operator == '+':
    res1 = num1 + num2
    print('addition of', num1, 'and', num2, 'is', res1)
elif operator == '-':
    res2 = num1 - num2
    print('substraction of ', num1, 'by', num2, 'is', res2)
elif operator == '*':
    res3 = num1 * num2
    print('multiplication of', num1,'and', num2, 'is', res3)
elif operator == '/' :
    res4 = num1 / num2
    print('division of', num1, 'by', num2, 'is',res4)
elif operator == '%':
    res5 = num1 % num2
    print('modulus of', num1, 'and', num2, 'is', res5)
elif operator == '**':
    res6 = num1 ** num2
    print('exponent of', num1, 'to the ', num2, 'is', res6)
elif operator == '//':
    res7=num1//num2
    print('floor division of',num1,'and ',num2,'is',res7)
else:
    print('please select a appropriate operator!!!!')