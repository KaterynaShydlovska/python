#1 Update Values in Dictionaries and Lists
#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)


#Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant';
print(students)


#In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)


#Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

z[0]['y'] =30
print(z)


#2.Iterate Through a List of Dictionaries
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#3. Get Values From a List of Dictionaries
def iterateDictionary(some_list):
    for item in some_list:
        print(item)

iterateDictionary(students) 


def iterateDictionary2(key_name, some_list):
    for item in range(0, len(students), 1):
        print(some_list[item][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key, val in dojo.items():
    print(len(key), key.upper(), "\n",  "\n".join(val))

printInfo(dojo)