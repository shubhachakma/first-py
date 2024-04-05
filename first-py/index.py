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
print(thisdict)