name= input('enter your name :',)
roll_no=  input('enter your roll no :')

print ('Hello ' +str(name)+  ' your roll no. is ' +str(roll_no)) #method 1
print ('Hello',name,'your roll no. is ', roll_no) #method 2
print('Hello %s your roll no. is %s' % (name, roll_no)) #method3
print('Hello {} your roll no is {}' .format(name,roll_no)) #method 4