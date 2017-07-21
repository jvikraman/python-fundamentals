#Python basics

#Use the # character for single-line comments.

#Like other languages, there's no multi-line comment feature out of the box in python. A common workaround to that is using " character 3x

#here's an example of a multi-line comment
"""
   most of the IDEs treat whatever
   typed in here as a multi-line comment
   also python doesn't assign these to any variables
   it's just going to sit there like a comment!
"""

#Integers & Floats
"""
    number = 42
    pi = 3.14159
    number + pi = 45.14159
    int(pi) == 3
    float(number) == 42.0
"""

#Strings
#'Hello Python' == "Hello Python" == """Hello Python"""
"""
    "hello".capitalize() == "Hello"
    "hello".replace("e", "a") == "hallo"
    "hello".isaplha() == True
    "123".isdigit() == True
    "lets,split,this".split(",") == ["lets", "split", "this"]
"""

#String formatting
"""
    fruit = "apple"
    person = "doctor"
   "An {0} a day keeps the {1} away!".format(fruit, person)

   #starting python 3.6 you can use the following too...
   f"An {fruit} a day keeps the {person} away!" - the leading 'f' character indicates string interpolation

   #replace f with r to indicate a raw string
   #likewise use u to indicate a unicode string
   
"""

#Boolean & None data types
"""
    is_valid = True  #pay attention to caps T
    file_exists = False 
    int(is_valid) == 1
    int(file_exists) == 0
    str(is_valid) == "True"

    found_treasure = None #similar to null in other languages
"""

#If statements
"""
    #pay attention to indentations instead of curly  braces for code blocks & also the character : at the
    end of if & else blocks
    num = 5
    if num == 5:
        print("You 've got a 5!")
    else:
        print("You ain't got 5!")

    #checking truthy value
    num = 3
    if num:
        print("num is defined and truthy")

    text = "python"
    if text:
        print("text is defined and truthy")

    #using Boolean & None combination
    is_member = True
    if is_member: #similar to doing Not is_member == True
    print("Hello there Fella!")

    found_treasure = None
    if found_treasure:
        print("Care to give a dime??")

    #using Not If combination
    num = 5
    if num != 5:
        print("This won't print")
    
    is_member = True
    if not is_member:
        print("This won't print either!")

    #multiple if statements using and/or combinations
    is_member = True
    membership_level = 3
    if is_member and membership_level == 3:
        print("Congrats! You are eligible for priority boarding.")

    if is_member or membership_level == 3:
        print("You may use the lounge!")

    #Ternary If statements
    a = 1
    b = 2
    "bigger" if a > b else "smaller"
"""

#Lists
"""
    #list indexes start with 0
    employee_names = [] # an empty list
    employee_names = ["Jake", "Rob", "Mary"] #assigning values to list

    #accessing list items
    employee_names[0] == "Jake"
    employee_names[2] == "Mary"
    employee_names[-1] == "Mary" #accessing the last item in the list. Note that you can also access list elements from right to left in which case the index starts at 1 instead of 0

    employee_names[0] = "Shane" #replacing list item at a specific index

    employee_names.append("Kate") #adds a new list item at the end of the list

    "Mary" in employee_names == True #to check whether Mary is still in the list

    len(employee_names) == 4 #to figure out how many elements in the list

    del employee_names[1] #removes Rob from the list. Note that after a del operation elements to the right of the deleted list item shifts left.

    #list slicing
    note that slicing doesn't modify the original list
    it temporarily ignores list elements based on the type of operation.
    cars = ["Audi", "BMW", "Jaguar", "Infinity"]
    cars[1:] == ["BMW", "Jaguar", "Infinity"] #ignores the first list element
    cars[1:-1] == ["BMW", "Jaguar"] #ignores first & last element in the list
"""

#Loops
"""
    #iterating using a for loop
    fruits = ["Apple", "Orange", "Peach"]
    for fruit in fruits:
        print("Current fruit is {0}".format(fruit))
    
    #using range() function in loops
    x = 0
    for index in range(10):
        x += 10
        print("The value of x is {0}".format(x))

    #range(10) is similar to [1,2,3....9]
    #range(5,10) == [5,6,7,8,9]
    #range(5,10,2) == [5,7,9] - the last parameter is the increment value    

    #using Break & Continue to manipulate control flow
    student_names = ["Mark", "Kate", "John", "Ann"]
    for name in student_names:
        if name == "Kate":
            print("Found " + name)            
        print("Testing " + name) #this line will keep printing till end of list

    #break out of the iteration after finding 'Kate'
    for name in student_names:
        if name == "Kate":
            print("Found " + name) 
            break           
        print("Testing " + name) #this line will keep printing till end of the list

    #bypass an iteration using Continue
    for name in student_names:
        if name == "John":
            continue #whatever code below the continue block won't execute for 'John'
            print("Found " + name)
        print("Currently testing " + name)

    "using a while loop
    x = 0
    while x < 10:
        print("Count is {0}".format(x))
        x += 1

    #causing an infinite loop using while
    num = 10
    while True:
        if num == 42:
            break
        print("Hello World")
"""

#Dictionaries
"""
    #in other words key/value pairs
    student = {
        "name": "Mark",
        "student_id": 12345,
        "feedback": None
    }

    #creating a list of dictionaries
    all_students = [
        {"name": "Mark", "student_id": 12345},
        {"name": "Kate", "student_id": 67890},
        {"name": "Rob", "student_id": 34567},
    ]

    #getting values using key
    student["name"] == "Mark"
    student["last_name"] - will result in a KeyError because that key doesn't exist

    #here's a better way to handle those type of issues
    student.get("last_name", "Unknown") - will return "Unknown" if the key doesn't exist.

    student.keys() - to get all the keys
    student.values() - to get all the values

    student["name"] = "James" - to change a key value
    del student["name"] - to delete a key/value pair
"""

#Exceptions
"""
    student = {
        "name": "Mark",
        "student_id": 12345,
        "feedback": None
    }

    print(student["last_name"]) - will result in an exception

    #here's a better way to handle such exceptions
    try:
        print(student["last_name"])
    except KeyError:
        print("Error finding last_name")
    
    print("This piece of code will still execute due to graceful error handling!")

    #handling more exceptions - for e.g. TypeError
    student = {
        "name": "Mark",
        "student_id": 12345,
        "feedback": None
    }

    student["last_name"] = "Jones"

    try:
        last_name = student["last_name"]
        numbered_last_name = 3 + last_name #this line will cause a TypeError
    except KeyError:
        print("Error finding last_name")
    except TypeError as error:
        print("You can't add int & str together!")
        print(error)
    
    print("This piece of code will still execute due to graceful error handling!")
    
    #you could use a generic exception handler like
    #except: Exception - however, remember that's going to give less meaningful info about the errors!
"""

#Other Data Types
"""
    complex
    long #removed in python 3.x
    bytes & bytearray
    tuple = (3,5,1,"Mark") - immutable objects
    set & frozenset - handy when it comes to filtering duplicates & ordering lists
    for e.g. set([3,2,3,1,5]) == (1,2,3,5)
"""