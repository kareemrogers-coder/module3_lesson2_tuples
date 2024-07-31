
#Question 1. Tuple Mastery in Python


# Objective: The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.


# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

"Itinerary 1: Alice - From New York to London"
"Itinerary 2: Bob - From Tokyo to San Francisco"


def new_tic(add_on):
    manifest = tuple(input(" Pleasee Enter Passenger Name, Orgin Location and Destination separated by spaces: ").split())
    add_on.append(manifest)
    print(tuple(add_on))
  

def display_manifest(manifest):
    for index, task in enumerate(manifest):
        print(f"Itinerary {index +1}: {task[0]} - From {task[1]} to {task[2]}")
    

def flt_int():
    manifest = []
    flag = True
    while flag:
        ans = input ('''
1- To add passenger information
2- View manifest
3- Quit

''')

        if ans == "1":
           print("Option 1 selected")
           manifest_update = new_tic(manifest)
        elif ans == "2":
            print("Option 2 selected")
            display_manifest(manifest)
        elif ans == "3":
            print('Exiting ticketing system...')
            break
        else:
            print('Invalid entry please select from one of the valid entries below:')


flt_int( )
       