#print("hello,world")
x = 5
y = 90
#print(x+y)
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)
#print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
#print(x + y + z)

def myfunc():
  global x
  x = "fantastic"

myfunc()

#print("Python is " + x)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print(thisdict)
a=float(input('enter first side:'))
b=float(input('enter first side:'))
c=float(input('enter first side:'))
s=(a+b+c) /2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)
print('the area of the triangle is %0.2f' %area)