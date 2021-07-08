indian=["mumbai","banglore","chennai","delhi"]
pakistan=["lahor","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]
city=input("enter your first city")
city1=input("enter your second city")

if city and city1 in inadia:
	print("in india")

elif city and city1 in pakistan:
	print("in pakistan")

elif city and city1 in bangladesh:
	print("in bangladesh")

else:
	print("dont same country")


