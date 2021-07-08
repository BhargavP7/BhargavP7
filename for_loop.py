
month_list=["january" ,"february","march","april","may"]
exp = [2350,2500,12200,1300]
s=(int)=input("enter amount:")

month = -1
for i in range(len(exp)):
	if s == exp[i]:
	month = i
	break;

if month != -1:
	print(f'you spent{s} in {month_list[month]}')
else:
	print(f'youn can not spend{s} in this list')
