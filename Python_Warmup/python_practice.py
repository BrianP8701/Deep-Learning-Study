
# Variable Types & Basic Operators

#  - Numbers(int, long, float, complex)
#  - String
#  - List
#  - Tuple
#  - Dictionary
#
#  - Arithmetic Operators(+, -, /, %, //, **)
#  - Comparison Operators(==, !=, <, >, <=, >=)
#  - Assignment Operators(+=, -+, =, /=, *=)
#  - Membership Operators(in, not in)
#  - Identity Operators(is, is not)

variable_name = 6
variable_name = "It's a string now!"
my_first_list = ['list', 7, 's']
my_first_dict = {'studs':'birds', 69:"GDK"}
#print("The content of this variable is = ", variable_name)
#print("The content is {} of this variable" .format(variable_name))
#print("The content is, {}, {}, {} of these variables" .format(variable_name, my_first_dict, my_first_list))

number_1 = 5      #int
number_2 = 8.0    #float
#print("The number 1 is {}, and number 2 is {}" .format(number_1, number_2))

sentence = "This is my string. Just like Java!"   #String
#print(sentence[0])    # charAt
#print(sentence[0:10]) # substring
#print(len(sentence))  # length

list_1 = [1, 'dolphin', 4] # Can be seen as a vector
list_1.append(5.5)
#print(list_1[0])   # get
#print(list_1[0:4]) # subarray
#print(len(list_1)) # size

list_2 = [1, 2, 3] * 3  # Repeats list 3 times
list_2[0] = 9
#print(list_2)

number_of_columns = 4
number_of_rows = 3 
matrix_list = [[0]*number_of_columns] * number_of_rows # 2D Array
#print(matrix_list)

tuple_1 = (1, 2, 3)   # Tuple
# tuple_1[0] = 9   Tuple values can't be changed
#print(tuple_1)

dictionary_1 = {'goat' : "mwaaaa", "RPT" : 444}  # Hashmap

a = 5
b = 7
c = 1
#print(a**3)   # To the power of
#print(17//a)  # Divide, but gets rid of remainder

sports = True
#if(not not not sports):
     #print('gdkkk')
#else:
    #print('4 sev 4 sev')

sport = ['Football', 'Soccer', 'Basketball', 'Tennis']
#if 'Soccer' in sport:
    #print("Mandem got the tekkers")
#elif "Basketball" in sport:
    #print("Run down ima oottaaa")
#elif 'Football' in sport:
    #print("Typical americano")

#if "Football":
    #print("Like what like how??")

#for i in range(5):
    #print("I am at {}" .format(i+1))
#for i in range(10, 13):
    #print(i)

n = 5
#while(n > 0):
    #print("The flockas at {}".format(n))
    #n-=1    

#for i in range(len(sport)):
    #print(sport[i])

#for currSport in sport:
    #print(currSport)

print(sport)

def sum_and_product(a, b): # Returns two values!
    return a * b, a + b

g, d = sum_and_product(2, 3)
print(g)
print(d)

def print_name(name, age="70"):
    print("{} is {} years old".format(name, age))


print(print_name("Joseph"))

def musho_jumbo(*args): # Pass tuple to method
    print(type(args))

musho_jumbo("Grass", "On", "a ", "Hill", 4, 4.0, True)

def hashmap_as_input(first_arg, **kwarg): # Pass dictionary to method
    print("First parameter is {}".format(first_arg))
    print(kwarg)

hashmap_as_input("Flockaa", key1="gold", key2=44, key3=False)