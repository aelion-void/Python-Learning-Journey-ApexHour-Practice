print("Hello developer ! Let's compare two numbers by math ")

# < , > , <= , >= , == , != these are the mathematical operator .
x = int(input('x = '))
y = int(input('y = '))

if x > y :
    print(' x is greater than y ')

if x < y :
    print(' x is greater than y ')

if x == y :
    print(' x is equal to y ')

# The following is the grading system for total of 100 mars obtained :

score = int(input( " Let's assign grade for marks obtained : "))

if  score >100 :
    print(' your score is more than 100')

elif score > 90 :
    print('Grade A')

elif score > 80 :
    print('Grade B')

elif score > 70 :
    print('Grade C')

elif score > 60 :
    print('Grade D')

elif score > 50 :
    print('Grade E') 

else :
    print(' Not eligile to Grade!')

#Enter a number to define is it even or odd , this can be done in 2 ways : 
#1
"""
x = int(input('Enter a number to define is it even or odd :'))

if x % 2 == 0 : 
    print('Even')
else :
    print('Odd')
"""
    
#2

def num() :
    x = int(input('Enter a number to define is it even or odd :'))
    if even(x) :
        print('Even')
    else :
        print('Odd')

def even(n) :
    return n % 2 == 0 

num()

#lets try new data type called match

name = input('Enter the first name from Great houses of westeros in Game Of Thrones : ')

match name :
    case "Daenerys" | "Viserys" | "Aerys II" | "Rhaegar" | "Rhaella" | "Rhaenys" |"Aegon" |"Jhonsnow"  :
        print("House Targaryen ")

    case "Rickard" | "Eddard"| "Catelyn"| "Robb" | "Sansa"| "Arya"| "Bran"| "Rickon"| "Benjen" :
        print("House Stark of Winterfell")

    case "Robert" |"Stannis" |"Renly" | "Shireen" :  
        print (" House Baratheon of Storm's End ")

    case "Tywin" |"Joanna" |"Jaime"| "Cersei"| "Tyrion"| "Joffrey"| "Myrcella"| "Tommen" :
        print("House Lannister of Casterly Rock")
    
    case "Balon" |"Alannys" |"Rodrik" |"Maron" |"Yara" |"Theon" :
        print("House Greyjoy of Pyke")

    case "Jon" |"Lysa"| "Robert| Eyrie":
        print("House Arryn of the Eyrie")

    case "Hoster" |"Minisa"| "Catelyn"| "Lysa"| "Edmure" |"Roslin" :
        print("House Tully of Riverrun")

    case "Mace" |"Alerie"| "Olenna" |"Loras" |"Margaery" :
        print("House Tyrell of Highgarden")

    case "Doran"| "Elia"| "Oberyn"| "Trystane":
        print("House Martell of Sunspear")
    
    
    case _:
        print('Not in major house of GOT or does not exist . ') 

print('Come back next time !')

