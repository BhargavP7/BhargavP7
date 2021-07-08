a = input("Enter Value: ")
print(type(a))

if a in (0,1,2,3,4,5,6,7,8,9):
	print("it is a number")
elif a in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
	print("it is a alphabet & charcter")
elif a in ('!','@','#','$','%','^','&','*','()','+','=','?','<','>','-','_','~','`'):
	print("it is a alphabet & charcter")
else:
	print("enter value is not numberm alphabet,charcter,special charcter")	
