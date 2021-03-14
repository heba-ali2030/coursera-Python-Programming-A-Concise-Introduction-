# ##### 1- write a function 'average(numlis)' that uses a 'for' loop to sum up the numbers
#  in numlis and divide by the length of numlis.

# nlis = [2,4,8,105,210,-3,47,8,33,1]
# rlis = [3.14, 7.26, -4.76, 0, 8.24, 9.1, -100.7, 4]

# def average(numlis):
#     sum = 0
#     for numbers in numlis:
#         sum= sum + numbers
#         average = sum / (len(numlis))
#         print(average)

# average(rlis)

# 2- it is a list of states and we will simply be stepping 
# through the loop and printing out the states.

# newEngland = ["Maine","New Hampshire","Vermont", "Rhodes Island", 
# "Massachusetts","Connecticut"]

# def for_state(slis):
#     for state in slis:
#         print(state)
# for_state(newEngland)


#3-  Write a function 'print_list(lis)' that prints items of the list lis. Test it 
# by running the three tests that I give here.
# letter_list = ['a', 'b', 'c']
# cap_list = ['A', 'B', 'C', 'D']
# misc_list = ['ball', 3.14, -50, 'university', "course"]

# def print_list(lis):
#     for items in lis:
#         print(items)

# print_list(letter_list)      
# print_list(cap_list)
# print_list(misc_list)


# print(range(2,20,3))
# print(list(range(2,20,3)))

# newEngland = [["Massachusetts",6692824],["Connecticut",3596080],
#               ["Maine",1328302],["New Hampshire",1323459],
#               ["Rhode Island",1051511],["Vermont",626630]]
              
# def report1(state_data):
#     """ prints population report """
#     print("Population          State")
#     for state_item in state_data:
#         print(state_item[1], "        ", state_item[0])
# or
# for i in range(0,len(state_data)):
        # print(state_data[i][1], "        ", state_data[i][0])
# report1(newEngland)


def multiply():
    numstr1 = input("Enter a number: ")
    numstr2 = input("Enter another number: ")
    num1 = float(numstr1)
    num2 = float(numstr2)
    print("Their product is ", num1 * num2)
    print("Won't work: ", numstr1 * numstr2)
multiply()    



