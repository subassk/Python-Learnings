//The variable nested contains a nested list. Assign ‘snake’ to the variable output using indexing.
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]
print(output)

Output : snake
Result	Actual Value	Expected Value	Notes
Pass	'snake'	'snake'	Testing that output is assigned to correct value
You passed: 100.0% of the tests


//Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow = 'yellow' in lst[2]
print(yellow)
#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = 4 in lst
four = '4' in lst
print(four)
#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = 'orange' in lst[0]
print(orange)

Output :
True
False
True

Result	Actual Value	Expected Value	Notes
Pass	True	True	Testing that yellow is assigned to correct value
Pass	False	False	Testing that four is assigned to correct value
Pass	True	True	Testing that orange is assigned to correct value
You passed: 100.0% of the tests


//Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L
print(test1)
# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5,8,7] in L
print(test2)
# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]
print(test3)

output:
False
True
True

Result	Actual Value	Expected Value	Notes
Pass	False	False	Testing that test1 has the correct value.
Pass	True	True	Testing that test2 has the correct value.
Pass	True	True	Testing that test3 has the correct value.
You passed: 100.0% of the tests


//The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

# london_gold = nested_d['London']['Great Britain']
#london_gold = list(nested_d[list(nested_d)[1]].values())[2]
london_gold = list(list(nested_d.values())[1].values())[3]
#print(nested_d.values())
print(list(nested_d.values())[1].values())

output : [38, 46, 22, 29]--->intergchanged values
Result	Actual Value	Expected Value	Notes
Pass	29	29	Testing that london_gold is assigned to correct value
You passed: 100.0% of the tests


//Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
x = sports['swimming']
v1 = x[2]
print(v1)

v = list(sports.values())[0]
v1 = v[2]
print(v1)

v1 = v1 = (list(sports.values())[0])[2]
print(v1)

# Assign the string 'platform' to the name v2
y = sports['diving']
v2 = y[1]
print(v2)
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = list(list(sports.values())[3].values())[0]
print(v3)
# Assign the string 'rings' to the name v4
a = list(list(sports.values())[3].values())[1]
v4 = a[3]
print(v4)


output : 
backstroke
backstroke
backstroke
platform
['vault', 'floor', 'uneven bars', 'balance beam']
rings

Result	Actual Value	Expected Value	Notes
Pass	'backstroke'	'backstroke'	Testing that v1 was created correctly.
Pass	"v1 = ...roke'"	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'v1 = ...roke"'	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'platform'	'platform'	Testing that v2 was created correctly.
Pass	'v2 = "platform"'	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	"v2 = 'platform'"	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	"['vau...eam']"	"['vau...eam']"	Testing that v3 was created correctly.
Pass	"v3 = ...eam']"	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'rings'	'rings'	Testing that v4 was created correctly.
Pass	"v4 = 'rings'"	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
Pass	'v4 = "rings"'	'\nspor...v4)\n\n'	Testing your code (Don't worry about actual and expected values).
You passed: 100.0% of the tests


//Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for key in nested_d.keys():
    # key -> Beijing...London...Rio
    us_count_year = nested_d[key]['USA']
    US_count.append(us_count_year)
print(US_count)

Output :
[36, 46, 35]

Result	Actual Value	Expected Value	Notes
Pass	[35, 36, 46]	[35, 36, 46]	Testing that US_count is assigned to correct values.
You passed: 100.0% of the tests


//Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for x in l_of_l:
    third.append(x[2])
print(third)

Output:
['blue', 'blood orange', 'lavender', 'mac n cheese']
Result	Actual Value	Expected Value	Notes
Pass	"['blu...ese']"	"['blu...ese']"	Testing that third has the correct list assigned to it.
You passed: 100.0% of the tests


//Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for x in athletes:
    for y in x:
        if 't' in y:
            t.append(y)
        else:
            other.append(y)
print(t)
print(other)

Output:
['Lochte', 'Bolt', 'Eaton', 'Dalton']
['Phelps', 'Schooling', 'Ledecky', 'Franklin', 'Felix', 'Gardner', 'Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak']

Result	Actual Value	Expected Value	Notes
Pass	"['Loc...ton']"	"['Loc...ton']"	Testing that t is assigned to correct values.
Pass	"['Phe...lak']"	"['Phe...lak']"	Testing that other is assigned to correct values.
You passed: 100.0% of the tests


//Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = 'data' in nested.keys()
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = 24 in nested['data']
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = 'whole' in nested.keys()
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = 'physics' in nested

Result	Actual Value	Expected Value	Notes
Pass	False	False	Testing that physics has the correct value.
Pass	True	True	Testing that data has the correct value.
Pass	False	False	Testing that whole has the correct value.
Pass	False	False	Testing that twentyfour has the correct value.
You passed: 100.0% of the tests








