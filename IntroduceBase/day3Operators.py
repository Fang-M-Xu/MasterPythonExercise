import math
'''
age =22
height=172.9
complex_number=4j

base = float(input("ENter base: "))
height = float(input("ENter height: "))
area = 0.5*base*height

print("The area of the triangle: ",area)

sideA = float(input("ENter sideA: "))
sideB = float(input("ENter sideB: "))
sideC = float(input("ENter bsideC: "))
perimeter=0
perimeter = sideC+sideB+sideA
print("The perimeter of the triangle: ",perimeter)

length = float(input("ENter length: "))
width = float(input("ENter width: "))

area_rectangle = length*width
perimeter_rectangle = 2*(length+width)
print("The area of the rectangle: ",area_rectangle,", The perimeter of the rectangle: ",perimeter_rectangle)

def func1(x):
    y = 2*x-2
    return y
def func2(y):
    x = (y+2)/2
    return x

x18 = int(input("ENter x18: "))
y18 = int(func1(x18))
x28 = int(input("ENter x28: "))
y28 = func1(x28)
slope1 =  (y28-y18)/(x28-x18)
x_intercept = func2(0)
y_intercept = func1(0)
print("The slope1: ",slope1,", x-intercept: ",x_intercept,", y-intercept: ",y_intercept)

p = [2,2]
q=[6,10]
slope2 = (q[1]-p[1])/(q[0]-p[0])
Euclidean_d =  math.dist(p,q)
print("The slope2: ",slope2,", Euclidean_d: ",Euclidean_d)

print(slope2>=slope1)

# String
length_comp = len("python")<len("dragon")
print(length_comp)
print('on' in 'python' and 'on' in 'dragon')
print("jargon" in "I hope this course is not full of jargon.")
print("on" in "python" and "dragon")
len_str = len("python")
print(len_str,float(len_str),str(len_str))

def checkEvenNum(n):
    if n%2 == 0:
        return True
    else:
        return False
num = int(input("Enter a num: "))
print("The even state of this num is ",checkEvenNum(num))

floor_d = 7//3
print(floor_d == int(2.7))

print(type('10') == type(10))
print(int(9.8)==10)

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour:"))
print("Your weekly earning is ", hours*rate)
'''
def pow_loop(num):
    str_loop = str(num) +', '
    for n in range(3):
        temp = num**n
        str_loop = str_loop + str(temp) +', '
    return str_loop
print('\n',pow_loop(1),'\n',pow_loop(2),'\n',pow_loop(3),'\n',pow_loop(4),'\n',pow_loop(5))