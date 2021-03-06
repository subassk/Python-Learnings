//Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision(str):
    noofchar =len(str)
    if(noofchar > 17):
        return("This is a long string")
    elif(noofchar <= 17):
        return("This is a short string")
 
Result	Actual Value	Expected Value	Notes
Pass	'This ...tring'	'This ...tring'	Testing the function decision with input 'Well hello dolly'
Pass	'This ...tring'	'This ...tring'	Testing the function decision with input 'In olden days a glimps of stocking was looked on a something shocking but heaven knows, anything goes'
Pass	'This ...tring'	'This ...tring'	Testing the function decision with input 'how do you do sir'

//Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.
def s_change(str):
    str = str + " for fun."
    return(str)

Result	Actual Value	Expected Value	Notes
Pass	'Coding for fun.'	'Coding for fun.'	Testing the function s_change with input coding
Pass	'We go... fun.'	'We go... fun.'	Testing the function s_change with input We go to the beach

//Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: “Hello, my name is Becky and I love SI 106.”
def intro(str):
    str = "Hello, my name is " +str + " and I love SI 106."
    return(str)
    
 Result	Actual Value	Expected Value	Notes
Pass	'Hello... 106.'	'Hello... 106.'	Testing the intro function on input 'Mike'

//Write a function called change that takes one number as its input and returns that number, plus 7.
def change(n):
    n = n + 7
    return(n)
    
  Result	Actual Value	Expected Value	Notes
Pass	12	12	Testing the function change with input 5
Pass	-3	-3	Testing the function change with input -10

//Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three.
def subtract_three(i):
    i = i-3
    return(i)

Result	Actual Value	Expected Value	Notes
Pass	6	6	Testing the subtract_three function on input 9.
Pass	-8	-8	Testing the subtract_three function on input -5

//Write a function called same_thing that returns the parameter, unchanged.
def same_thing(p):
    return(p)
    
Result	Actual Value	Expected Value	Notes
Pass	5	5	Testing the function same_thing with input 5
Pass	'Welcome'	'Welcome'	Testing the function same_thing with input 'Welcome'

//Write a function named same that takes a string as input, and simply returns that string.
def same(x):
    return(x)

Result	Actual Value	Expected Value	Notes
Pass	'hello'	'hello'	Testing the same function on input 'hello'.

//Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(list1):
    sum_val = sum(int(i) for i in list1)
    return(sum_val)
    
 Result	Actual Value	Expected Value	Notes
Pass	15	15	Testing the total function on input [1, 2, 3, 4, 5].
Pass	0	0	Testing the total function on input [0, 0, 0, 0].
Pass	0	0	Testing the total function on input [].
Pass	2	2	Testing the total function on input [2].

//Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(list):
    nos = len(list)
    return(nos)   
    
Result	Actual Value	Expected Value	Notes
Pass	0	0	Testing the function count with input []
Pass	6	6	Testing the function count with input [1, 5, 9, -2, 9, 23

//Write a function called int_return that takes an integer as input and returns the same integer.
def int_return(int):
    return(int)
 Result	Actual Value	Expected Value	Notes
Pass	10	10	Testing that function int_return(10) returns 10

//Write a function called add that takes any number as its input and returns that sum with 2 added.
def add(no):
    sum = no + 2
    return(sum)
Result	Actual Value	Expected Value	Notes
Pass	0	0	Testing that add(-2) returns 0
Pass	8	8	Testing that add(6) returns 8
Pass	6	6	Testing that add(4) returns 6

//Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(str):
    new_str = str + "Nice to meet you!"
    return(new_str)
Result	Actual Value	Expected Value	Notes
Pass	"I'm B... you!"	"I'm B... you!"	Tests that change('I'm Bob. '') returns 'I'm Bob. Nice to meet you!'
Pass	'Nice ... you!'	'Nice ... you!'	Tests that change() returns 'Nice to meet you!'

//Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(int):
    int = sum(int)
    return(int)
Result	Actual Value	Expected Value	Notes
Pass	5	5	Tests that accum([5]) returns 5
Pass	0	0	Tests that accum([]) returns 0
Pass	20	20	Tests that accum([2,4,6,8]) returns 20

//Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(str):
    length_str = len(str)
    if(length_str >= 5):
        return("Longer than 5")
    elif(length_str < 5):
        return("Less than 5")
Result	Actual Value	Expected Value	Notes
Pass	'Less than 5'	'Less than 5'	Tests that length([]) returns 'Less than 5'
Pass	'Less than 5'	'Less than 5'	Tests that length([2, 2]) returns 'Less than 5'
Pass	'Longer than 5'	'Longer than 5'	Tests that length([4, 4, 4, 3, 5, 6, 7, 8, 9]) returns 'Longer than 5'
Pass	'Longer than 5'	'Longer than 5'	Tests that length([1, 1, 1, 1, 1]) returns 'Longer than 5'

//You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.

def divide(x):
    x = x/2
    return(x)

def sum(y):
    z = divide(y) + 6
    return(z)
Result	Actual Value	Expected Value	Notes
Pass	2.0	2	Tests that divide(4) returns 2
Pass	8.0	8	Tests that sum(4) returns 8
Pass	7.0	7	Tests that sum(2) returns 7
Pass	3.0	3	Tests that sum(-6) returns 3
Pass	6.0	6	Tests that sum(0) returns 6

//Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(x):
    x = x + 5
    return(x)

def mult(y):
    y = addit(y) * y
    return(y)

Result	Actual Value	Expected Value	Notes
Pass	6	6	Testing the function mult with input 1 (should be 6)
Pass	-6	-6	Testing the function mult with input -2 (should be -6)
Pass	0	0	Testing the function mult with input 0 (should be 0)
Pass	6	6	Testing the function addit with input 1 (should be 6)
Pass	3	3	Testing the function addit with input -2 (should be 3)
Pass	5	5	Testing the function addit with input 0 (should be 5)

// Consider the following Python code.What does this function print?
def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)      #### 25

// Example : Passing Mutable Objects :    

def double(y):
    y = 2 * y
def changeit(lst):
    lst[0] = "Michigan"
    lst[1] = "Wolverines"
y = 5
double(y)
print(y)
mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)
###  Output :: 5
['Michigan', 'Wolverines', 'are', 'awesome']


//Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.
def info(name,gender,age,bday_month,hometown):
    info = (name,gender,age,bday_month,hometown)
    return(info)
    
 Result	Actual Value	Expected Value	Notes
Pass	"('Sue...bor')"	"('Sue...bor')"	Testing that info('Sue', 'Female', 20, 'March', 'Ann Arbor') returns('Sue', 'Female', 20, 'March', 'Ann Arbor')


//Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []
for medals in gold.items():
    num_medals.append(medals[1])
print(num_medals)

output : [31, 19, 19, 13, 12, 10, 8, 8]
Result	Actual Value	Expected Value	Notes
Pass	'[8, 8..., 31]'	'[8, 8..., 31]'	Testing that num_medals is assigned to correct values.
Pass	'.keys()'	'\ngold...s)\n \n'	Testing your code (Don't worry about actual and expected values).
Pass	'.items()'	'\ngold...s)\n \n'	Testing your code (Don't worry about actual and expected values).
Pass	'in gold:'	'\ngold...s)\n \n'	Testing your code (Don't worry about actual and expected values)
