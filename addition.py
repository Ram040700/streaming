a=int(input("Enter a number\n"))
b=int(input("Enter a number\n"))
c={1:"addition",2:"Substraction",3:"division"}
print("\n",c) 
d=int(input("Enter your choice\n"))
if d==1:
  print("Total addition is ",a+b)
elif d==2:
  print("Total Sub =",a-b)
else:
  try:
      print("Answer",a/b)
  except:
      print("Something went wrong")      