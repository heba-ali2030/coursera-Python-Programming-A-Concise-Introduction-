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


# def multiply():
#     numstr1 = input("Enter a number: ")
#     numstr2 = input("Enter another number: ")
#     num1 = float(numstr1)
#     num2 = float(numstr2)
#     print("Their product is ", num1 * num2)
#     print("Won't work: ", numstr1 * numstr2)
# multiply()    




# ## Libraries

# import random
# print(random.random())
# print(random.randint(3,8))

# import random

# verbs=["are","is","goes","cooks","shoots","faints","chews","screams"]
# nouns=["bear","lion","mother","baby","sister","car","bicycle","book"]
# adverbs=["handily","sweetly","sourly","gingerly","forcefully","meekly"]
# articles=["a","the","that","this"]

# def simple_poem():
#     for i in range(5):
#         article = random.choice(articles)    
#         noun = random.choice(nouns)
#         verb = random.choice(verbs)
#         adverb = random.choice(adverbs)
    
#         our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
#         our_sentence = our_sentence.capitalize()
#         print(our_sentence)
# simple_poem()


# def add_up():
#     sum = 0
#     while True:
#         num = int(input("enter a number, enter zero to quite: "))
#         if num == 0:
#             break
#         sum= sum + num
#     print(sum)


# add_up()



# def store_up():
#     numbers_list = []
#     while True:
#         nextnum = int(input("Enter a number, 0 to quit: "))
#         if nextnum == 0:
#             break
#         numbers_list.append(nextnum)
#     print(numbers_list)
# store_up()



# Exercise:
# Write a function diner_waitress() that asks for your order. First start an empty
# list, call it order. Then use a while loop and an input() statement to gather
# the order. Continue in the while loop until the customer says "that's all". 
# Onne way to end the loop is to use 'break' to break out of the loop when 
# "that's all" is entered. 
# Recall that you can add to a list by using the list's .append() method; suppose
# that your list is called order. To create an empty list you can use
# order = []. You are going to have to input one food at a time and append it
# to the order list.

def dinner_waitress():
    print('Hello, I will be your waitress, what will you have ?: ')
    order =[]
    while True:
        food= input(" menu item : ")
        if food.lower() == "that's all":
            break
        else:
            order.append(food)
    print(" you have ordered : ")
    print(order)

dinner_waitress()






# Then print out the order. Here is my run:

# diner_waitress()
# Hello, I'll be your waitress. What will you have?

# menu item: eggs

# menu item: bacon

# menu item: toast

# menu item: jelly

# menu item: that's all
# You've ordered:
# ['eggs', 'bacon', 'toast', 'jelly']
