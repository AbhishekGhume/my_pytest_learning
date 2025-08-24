# taking string input

name = input("name: ")
print(name)

# taking int input
age = int(input("age: "))
print(age)

# taking float input
cgpa = float(input("cgpa: "))
print(cgpa)





# conditional statements 

if(18<=age<=25):
    print("ergis")
elif(age>25):
    print("cvbn")
else:
    print("wert")





# ternery operator

isGoodBoy = "Yes" if name == "Abhishek" else "No"
print(isGoodBoy)




# type conversion
a = 20
b = 23.6
sum = a+b

# type casting
c = int(b)
print(c)



# list = similar to array but contains elements of different data types and it is mutable
my_list = ["hghj", 23, 56.66, "we"]



# tuple =  similar to list but immutable    
my_tuple = ("ewrt", 234, 33.7)
print(type(my_tuple))
print(my_tuple)



# dictonary = stores data in key-value pair
my_dict = {
    "name" : "Abhi",
    "age" : 22,
    "cgpa" : 8.46,
    "skills" : ["Java", "Flutter"]
}

print(my_dict["name"])



# set = collection of unordered items with unique elements and immutable
nums = {1, 2, "asd"}