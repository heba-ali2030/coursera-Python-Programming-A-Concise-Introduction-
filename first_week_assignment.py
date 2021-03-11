#Problem 1_1:
#Write a function problem1_1() that prints "Problem Set 1".
#def problem1_1():
    #print("problem set 1")
#problem1_1()


#Problem 1_2:
#Write a function problem1_2(x,y) that prints the sum and product of the
#numbers x and y on separate lines, the sum printing first
# def problem1_2(x,y):
#     sum= x + y
#     print('the sum of x and y =', sum)
#     product= x * y
#     print('product of the numbers x and y=', product)
# problem1_2(3,5)


#Problem 1_3:  
#Write a function problem1_3(n) that adds up the numbers 1 through n and
#prints out the result. You should use either a 'while' loop or a 'for' loop.
#Be sure that you check your answer on several numbers n.  Be careful that your
#loop steps through all the numbers from 1 through and including n

# def problem1_3(n):
#     total=0
#     for i in range(0, n+1):
#        total += i
       
#     print (total)
# problem1_3(6)


# Problem 1_4:
# Write a function 'problem1_4(miles)' to convert miles to feet. There are
# 5280 feet in each mile. Make the print out a statement as follows:
# "There are 10560 feet in 2 miles."  Except for the numbers this statement 
# should be exactly as written.



# def problem1_4(miles):
#     feet = 5280 * miles 
#     print("There are", feet, "feet in", miles, "miles.")

# problem1_4(5)

# Problem 1_5:
# Write a function 'problem1_5(age)'. This function should use if-elif-else
# statement to print out "Have a glass of milk." for anyone under 7; "Have
# a coke." for anyone under 21, and "Have a martini." for anyone 21 or older.

# age= int(input('please enter your age : '))
# def problem1_5(age):
#     if age < 7:
#         print('Have a glass of milk')
#     elif age >= 21:
#         print('Have a martini')
#     else:
#         print('Have a coke')
# problem1_5(age)


# Problem 1_6:
# Write a function 'problem1_6()' that prints the odd numbers from 1 through 100.
# Make all of these numbers appear on the same line (actually, when the line
# fills up it will wrap around, but ignore that.). In order to do this, your
# print statement should have end=" " in it. For example, print(name,end=" ") 
# will keep the next print statement from starting a new line. Be sure there is a
# space between these quotes or your numbers will run together. Use a single 
# space as that is what the grading program expects. Use a 'for' loop 
# and a range() function.

# def problem1_6():
#     for numbers in range(0,100):
#         if numbers%2 != 0:
#             print(numbers, end=' ')
        
# problem1_6()


# Problem 1_7:
# Write a function problem1_7() that computes the area of a trapezoid. Here is the
# formula: A = (1/2)(b1+b2)h. In the formula b1 is the length of one of the 
# bases, b2 the other. The height is h and the area is A. Basically, this 
# takes the average of the two bases times the height. For a rectangle b1 = b2, 
# so this reduces to b1*h. This means that you can do a pretty good test of the 
# correctness of your function using a rectangle (that way you can compute the 
# answer in your head). Use input statements to ask for the bases and the height.
# Convert these input strings to real numbers using float(). Print the output
# nicely EXACTLY like mine below.



def problem1_7():
    b1= float(input('enter the length of the first base: '))
    b2= float(input('enter the length of the second base: '))
    h= float(input('enter the length of the height: '))
    
    A= (1/2)*(b1+b2)*(h)
    print("The area of a trapezoid with bases",b1,"and", b2, "and height", h, "is", A)
problem1_7()