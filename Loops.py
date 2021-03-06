//Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
eve_nums = []
counter=0
while(counter < 15):
    if counter % 2 == 0:
        eve_nums.append(counter)
    counter= counter+ 1       
print(eve_nums)

output : [0, 2, 4, 6, 8, 10, 12, 14]
Result	Actual Value	Expected Value	Notes
Pass	'[0, 2..., 14]'	'[0, 2..., 14]'	Testing that eve_nums has been assigned the correct elements


//Below, we’ve provided a for loop that sums all the elements of list1. Write code that accomplishes the same task, but instead uses a while loop. Assign the accumulator variable to the name accum.
list1 = [8, 3, 4, 5, 6, 7, 9]
tot = 0
for elem in list1:
    tot = tot + elem
---------------------------- 
accum = 0
for elem in list1:
    accum = accum + elem
print(accum)    
----------------------------    
accum = 0
n = 0
while n<7:
    accum = accum + list1[n]
    n = n + 1

Result	Actual Value	Expected Value	Notes
Pass	42	42	Testing that accum has the correct value.
Pass	'while'	'\nlist...+ 1\n\n'	Testing your code (Don't worry about actual and expected values).


//Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(numberList):
    each_num = []
    index = 0
    while(index < len(numberList) and numberList[index] != 4):
        each_num.append(numberList[index])
        index = index+ 1       
    return each_num 

print(stop_at_four([4, 2, 8])) 


Result	Actual Value	Expected Value	Notes
Pass	'[0, 9...1, 7]'	'[0, 9...1, 7]'	Testing the function stop_at_four on the input [0, 9, 4.5, 1, 7, 4, 8, 9, 3].
Pass	[]	[]	Testing the function stop_at_four on the input [4, 1, 2, 8].
Pass	[]	[]	Testing the function stop_at_four on the input [4].
Pass	[1, 6, 2, 3, 9]	[1, 6, 2, 3, 9]	Testing that stop_at_four([1, 6, 2, 3, 9]) returns ([1, 6, 2, 3, 9])
You passed: 100.0% of the tests
------------------------------------------------
    
#def stop_at_four(n):
#    each_num = []
#    counter=0
#    while(counter <= n):
#        each_num.append(counter)
#        counter= counter+ 1       
#    return each_num 
#print(stop_at_four(4))

output : [0, 1, 2, 3, 4]


//Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(L):
    l = []
    n = 0
    while L[n] != 5:
        l.append(L[n])
        n = n + 1
        if len(L) == n:
            break
    return l
    
Result	Actual Value	Expected Value	Notes
Pass	[1, 2, 3, 4]	[1, 2, 3, 4]	Testing that sublist([1, 2, 3, 4, 5, 6, 7, 8]) returns [1, 2, 3, 4]
Pass	[]	[]	Testing that sublist([5]) returns []
Pass	[8, 6]	[8, 6]	Testing that sublist([8, 6, 5]) returns [8, 6]
Pass	[1, 6, 2, 3, 9]	[1, 6, 2, 3, 9]	Testing that sublist([1, 6, 2, 3, 9]) returns ([1, 6, 2, 3, 9])
You passed: 100.0% of the tests

//Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(L):
    l = []
    n = 0
    while L[n] != 7:
        l.append(L[n])
        n = n + 1
        if len(L) == n:
            break
    return l
       
  Result	Actual Value	Expected Value	Notes
Pass	'[0, 2..., 14]'	'[0, 2..., 14]'	Testing that check_nums stops on the correct postion with input [0,2,4,9,2,3,6,8,12,14,7,9,10,8,3]
Pass	'[9, 3..., 10]'	'[9, 3..., 10]'	Testing that check_nums stops on the correct position with input [9,302,4,62,78,97,10,7,8,23,53,1]
Pass	[]	[]	Testing that check_nums stops on the correct position with input [7,8,3,2,4,51]
Pass	[1, 6, 2, 3, 9]	[1, 6, 2, 3, 9]	Testing that check_nums([1, 6, 2, 3, 9]) returns ([1, 6, 2, 3, 9])
You passed: 100.0% of the tests

//Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
#def sublist(L):
#    n = 0
#    list = []
#    while "STOP" not in L[n]:
#        list.append(L[n])
#        n = n + 1
#    return list



def sublist(L):
    l = []
    n = 0
    while L[n] != "STOP":
        l.append(L[n])
        n = n + 1
        if n == L[n]:
            break
    return l
    
 Result	Actual Value	Expected Value	Notes
Pass	"['bob...ucy']"	"['bob...ucy']"	Testing that sublist(['bob', 'joe', 'lucy', 'STOP', 'carol', 'james']) returns ['bob', 'joe', 'lucy']
Pass	[]	[]	Testing that sublist(['STOP']) returns []
Pass	"['jac...aul']"	"['jac...aul']"	Testing that sublist(['jackie', 'paul', 'STOP']) returns ['jackie', 'paul']

//Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(L):
    list = []
    n = 0
    while "z" != L[n]:
        list.append(L[n])
        n = n + 1
    return list

Result	Actual Value	Expected Value	Notes
Pass	"['c',... 'r']"	"['c',... 'r']"	Testing the function stop_at_z on the input ['c', 'b', 'd', 'zebra', 'h', 'r', 'z', 'm', 'a', 'k'].
Pass	"['zoo...azz']"	"['zoo...azz']"	Testing the function stop_at_z on the input ['zoo', 'zika', 'ozzie', 'pizzazz', 'z', 'pizza', 'zap', 'haze'].
Pass	[]	[]	Testing the function stop_at_z on the input ['z'].

//Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.
sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x

   
lst = [65, 78, 21, 33]
sum2 = 0
n = 0
while n < 4:
    sum2 = sum2 + lst[n]
    n = n + 1

Result	Actual Value	Expected Value	Notes
Pass	197	197	Testing that sum2 is assigned to correct value.
Pass	'while'	'\nsum1...+ 1\n\n'	Testing your code (Don't worry about actual and expected values)


//Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing














// Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.
But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(str, direction = True , d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if str in d:
            return True
        else:
            return False
    elif direction == False:
        if str not in d:
            return True
        else:
            return False
    return True
    

Result	Actual Value	Expected Value	Notes
Pass	True	True	Testing that checkingIfIn returns the correct boolean on input 'grapes'
Pass	False	False	Testing that checkingIfIn returns the correct boolean on input 'carrots'
Pass	False	False	Testing that checkingIfIn returns the correct boolean on input ('grapes', False)
Pass	True	True	Testing that checkingIfIn returns the correct boolean on input ('carrots', False)
Pass	False	False	Testing that checkingIfIn returns the correct boolean on input ('grapes', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
Pass	True	True	Testing that checkingIfIn returns the correct boolean on input ('peas', d = {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
Pass	False	False	Testing that checkingIfIn returns the correct boolean on input ('peas', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
Pass	True	True	Testing that checkingIfIn returns the correct boolean on input ('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
You passed: 100.0% of the tests


//Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(x, abool = True, dict1 = {2:3, 4:5, 6:8}):
    if abool == True:
        if x in dict1:
            return dict1[x]
    else:
        return False


Result	Actual Value	Expected Value	Notes
Pass	3	3	Testing that test(2) returns 3
Pass	False	False	Testing that test(4, False) returns False
Pass	4	4	Testing that test(5, dict1 = {5:4, 2:1}) returns 4
You passed: 100.0% of the tests


//Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(p1,p2 = 6):
    mvalue = p1 * p2
    return(mvalue)

Result	Actual Value	Expected Value	Notes
Pass	12	12	Testing that mult returns the correct value on input (2)
Pass	15	15	Testing that mult returns the correct value on input (3,5)
Pass	'hello...hello'	'hello...hello'	testing that mult returns the correct value on input (4, 'hello'
You passed: 100.0% of the tests


//The following function, greeting, does not work. Please fix the code so that it runs without error. This only requires one change in the definition of the function.

def greeting(greeting="Hello ", name, excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

Error
SyntaxError: non-default argument follows default argument on line 2

def greeting(name , greeting="Hello ",excl="!"):
    return greeting + name + excl


output :
Hello Bob!
Hello !
Hello Bob!!!
Result	Actual Value	Expected Value	Notes
Pass	'Hello Bob!'	'Hello Bob!'	Testing that greeting('Bob') returns 'Hello Bob!'.
Pass	'Hello !'	'Hello !'	Testing that greeting('') return 'Hello !'.
You passed: 100.0% of the tests


//Below is a function, sum, that does not work. Change the function definition so the code works. The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.
def sum(intz=5, intx):
    return intz + intx
    
def sum(intx, intz=5):
    sum = intz + intx
    return(sum)

Result	Actual Value	Expected Value	Notes
Pass	10	10	Testing the function sum on inputs 8, 2.
Pass	17	17	Testing the function sum on input 12.
You passed: 100.0% of the tests


//We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('')

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('', False)

# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('x', True , {'x': 8})--->using all 3 parameters

param_check = checkingIfIn('x', d ={'x': 8})---->using 1st and 3rd parameters

Result	Actual Value	Expected Value	Notes
Pass	8	8	Testing that param_check has the correct value
Pass	False	False	Testing that c_false has the correct value
Pass	19	19	Testing that fruit_ans has the correct value
Pass	True	True	Testing that c_true has the correct value
You passed: 100.0% of the tests












































































































num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
  print("Invalid operator")

// Turtle graphics :
import turtle             # allows us to use the turtles library
wn = turtle.Screen()      # creates a graphics window
alex = turtle.Turtle()    # create a turtle named alex
alex.forward(150)         # tell alex to move forward by 150 units
alex.left(90)             # turn by 90 degrees
alex.forward(75)          # complete the second side of a rectangle

// Turtle using Range function and for loop :
import turtle
wn = turtle.Screen()
elan = turtle.Turtle()
distance = 50
for _ in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10
    
// Turtle using Methods:
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
dist = 5
tess.up()                     # this is new
for _ in range(30):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(dist)          # move tess along
    tess.right(24)              # and turn her
    dist = dist + 2
wn.exitonclick()

//The slice Operator
singers = "Peter, Paul, and Mary"
print(singers[0:5])       #Peter
print(singers[7:11])      #Paul
print(singers[17:21])     #Mary
fruit = "banana"
print(fruit[:3])      #ban
print(fruit[3:])      #ana

//List Slices
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])    #['b', 'c']
print(a_list[:4])     #['a', 'b', 'c', 'd']
print(a_list[3:])     #['d', 'e', 'f']
print(a_list[:])      #['a', 'b', 'c', 'd', 'e', 'f']

//Tuple Slices
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2])     #1967
print(julia[2:6])   #(1967, 'Duplicity', 2009, 'Actress')
print(len(julia))   #7
julia = julia[:3] + ("Eat Pray Love", 2010) + julia[5:]
print(julia)        #('Julia', 'Roberts', 1967, 'Eat Pray Love', 2010, 'Actress', 'Atlanta, Georgia')

//Index
music = "Pull out your music and dancing can begin"
bio = ["Metatarsal", "Metatarsal", "Fibula", [], "Tibia", "Tibia", 43, "Femur", "Occipital", "Metatarsal"]
print(music.index("m"))         #14
print(music.index("your"))      #9
print(bio.index("Metatarsal"))  #0
print(bio.index([]))            #3
print(bio.index(43))            #6

//No.Of Items in the List:
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[len(sports) - 3:]

//Print each element of the list and the Type of Each elements:
several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for ch in several_things:
    print(ch)
for ty in ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]:
    print(type(ty))
    
//Print the length of each element:
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for ln in str_list:
   print(len(ln))
   
//Turtle drawing with speed
import turtle
wn = turtle.Screen()
hexn = turtle.Turtle()
for i in range(6):
    hexn.forward(100)
    hexn.left(360/6)
    hexn.speed(0)
wn.exitonclick()

//Accumulation pattern to count the no.of characters:
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for n in original_str:
    num_chars += 1
print(num_chars)

//Accumulation Pattern
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for n in original_str:
    num_chars += 1
print(num_chars)

//Compute avg
week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")
avg_temp = sum(float(i) for i in week_temps_f) / 7 
print(avg_temp)

//List of numbers 
nums = range(68)

//rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi_list = rainfall_mi.split(',')
print(rainfall_mi_list)
num_rainy_months = 0
for i in rainfall_mi_list:
    if float(i) > 3 :
        num_rainy_months += 1
print(num_rainy_months)


//The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
sentence_words = sentence.split(' ')
print(sentence_words)
same_letter_count = 0
for i in sentence_words:
    if (i[0] == i[-1]):
        same_letter_count += 1
print(same_letter_count)


//Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.
items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for i in items:
    if "w" in i:
        acc_num += 1
        print(acc_num)

		
//Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
Note 1: be sure to not double-count words that contain both an a and an e.
HINT 1: Use the in operator.
HINT 2: You can either use or or elif.
sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
s_w = sentence.split(" ")
print(s_w)
num_a_or_e = 0
for x in s_w:
    if ('a' in x) or ('e' in x):
        num_a_or_e += 1
    print(num_a_or_e)
	
//Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u. Hint: use the in operator with vowels.
s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
# Write your code here.
num_vowels = 0
for x in s:
    if x in vowels:
        num_vowels += 1
    print(num_vowels)
	
//Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. Each character in str1 should be its own element in the list chars.
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
chars[:0] = str1
print(chars)

//For each character in the string saved in ael, append that character to a list that should be saved in a variable app.
ael = "python!"
print(ael)
app = []
app.append(ael)
app[:] = ael
print(app)

//For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense). Save these past tense words to a list called past_wrds.
wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []
for item in wrds:
   past_wrds.append(item +"ed")
print(past_wrds)

//Below are a set of scores that students have received in the past semester. Write code to determine how many are 90 or above and assign that result to the value a_scores
scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
score = scores.split(" ")
print(score)
a_scores = 0
for item in score:
    if float(item) >= 90:
        a_scores += 1
print(a_scores)

//A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"
r_phrase = reversed(p_phrase)
r_phrase = ''.join(list(reversed(p_phrase)))

//Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item in inventory:
    i = item.split(',')
    name = i[0]
    stock = i[1]
    cost = i[2] 
    print("The store has{1} {0}, each for{2} USD." .format(name, stock ,cost))
