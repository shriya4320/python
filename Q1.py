m1=input('Enter marks of sub1:')
m2=input('Enter marks of sub2:')
m3=input('Enter marks of sub3:')

avg=m1+m2+m3/3
print('avg marks are:')
print(avg)

if avg>90:
    print('A grade')

elif avg>=75:
    print('B grade')

elif avg>=50:
    print('C grade')

else:
    print('FAIL')
