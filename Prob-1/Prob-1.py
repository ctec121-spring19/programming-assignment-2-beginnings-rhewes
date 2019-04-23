# Module 2
#   Programming Assignment 2
#     Prob-1.py

# Riley Hewes

# Purpose: define some variables and print them out

def main():
    # some example code

    # define a variable
    classTitle = "Intro to Programming and Problem Solving"

    # print the output
    # print a blank line
    print()
    # print section heading
    print("Example Output")
    # print the variable indented with a tab
    print("\tTitle:\t\t", classTitle, sep="")
    
    # Problem
    '''
    From the syllabus
        Title:	        Intro to Programming and Problem Solving
        Location:	    SHL 125
        Time:	        MW 10:30A – 12:50P
        Quarter:	    Spring 2019
        Item/Section:	Item 6485, Section A
    
    The assignment is for you to recreate the text above. The steps are 
    outlined as comments below. After each commnent write your code in the
    blank line provided.
    '''

    # create variables and set values for:
    # location
    classLocation = "SHL 125"
    # time
    classTime = "MW 10:30A - 12:50P"
    # quarter
    classQuarter = 'Spring 2019'
    # item - bonus points if you define item as a number
    classItem = "Item 6485"
    # section - bonus points if you use "A" as the value
    classSection = "Section A"
    # print the output
    print(classTitle)
    # print a blank line
    print('')
    # print section heading - replace <name> with your name - no angle brackets. 
    # Ex: Bill's Output
    print("Riley's Output")
    # print the title - copy the code above
    print(classTitle)
    # print the location
    print(classLocation)
    # print the time
    print(classTime)
    # print the quarter
    print(classQuarter)
    # print item/section
    print(classItem,classSection)
    # print a blank line
    print('')

main()