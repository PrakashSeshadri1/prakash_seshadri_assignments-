def get_details():
  name = str(input("enter your name:"))
  age = int(input("enter your age:"))
  fcolor = str(input('enter your color:'))
  return name, age, fcolor
name, age, fcolor = get_details()
print("Hello " + name )
print("you are " + str(age) + " years old")
print("your favorite color is " + fcolor)
