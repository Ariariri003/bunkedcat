'''
FORMATED OUTPUT
======================
Date: 17/10/2019
----------------------
'''

a, b, c = 5, 3.2, "\"Hello\""

print (a)
print(b)
print(c)

print("%s\t%s\t%s" % (a,b,c))
print("%s\n%s\n%s" % (a,b,c))

print('I love my {} with {}'.format('burger','Cheese'))
print('I love my {1} with {0}'.format('burger','Cheese'))


y = 10
massage = "Happy {}th Birthday!".format(y)
print(massage)
z=95
x = "Happy {}th Birthday!".format(z)
print(x)

