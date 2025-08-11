print('Hello developer!')

#variables 

name = input('Enter your name ? ')

#remove spaces from left and right side of variable
name = name.strip()

#to make capitalize
name = name.title()

##above variable can also be write in single line of code as below
#name = input('Enter your name ? ').strip().title()


print(f"Hey \"{name}\"welcome to the world of code , Enjoy your day ! ")

 
 # integers
x = int(input('Enter your lucky numer ? '))
y = float(input (' what is your age ? '))

## float : decimal value same as integer.
##to round off use a varible for output . ex : z = round(x+y) 

z = round(x*y , 2) 
print(f'here is your id {z:,}')

#creating  a function

def msg():
    print(' lets do some math ')

msg()

def num():
    x = float(input('Enter a number to be squared :' ))
    print('x squared is ' , square(x))

def square(n) :
    return n * n

num()

print('Pleasure to meet you , comeback soon...')
