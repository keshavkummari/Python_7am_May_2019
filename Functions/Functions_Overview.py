"""
A function is a block of organized, reusable code that is used to perform a single, related action.

Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc.
but you can also create your own functions.

These functions are called user-defined functions.
def function_name(parameters):
    function_suite
    return [expression]

def hello(a):
    print(a)
    return

abc = hello('Welcome to Python World')

def sum(var1,var2):
    # creating Variable inside the function
    total = var1 + var2
    #print(total)
    return total

a1 = sum(10,20)
print(a1)
"""

def centos(mylist):
    mylist=[1,2,3,4,5]
    print(mylist)
    return

_01 = [10,20,30,40,50]

centos(_01)

def centos(mylist):
    mylist.append([1,2,3,4,5])
    print(mylist)
    return

_01 = [10,20,30,40,50]

centos(_01)

"""
# Python Functions:

"""
A function is a block of organized, reusable code that is used to perform a single, related action.

Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc.
but you can also create your own functions.

These functions are called user-defined functions."""

# Defining a Function:

"""
You can define functions to provide the required functionality.

Here are simple rules to define a function in Python.

1. Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

2. Any input parameters or arguments should be placed within these parentheses.

3. You can also define parameters inside these parentheses.

4. The first statement of a function can be an optional statement
   - the documentation string of the function or docstring.

5. The code block within every function starts with a colon (:) and is indented.

6. The statement return [expression] exits a function,
   optionally passing back an expression to the caller.

7. A return statement with no arguments is the same as return None."""
"""*******************************************************************"""
# Syntax:

def function_name( parameters ):
   "function_docstring"
   function_suite
   return [expression]

"""Note: By default, parameters have a positional behavior
and you need to inform them in the same order that they were defined."""

# Example:
# The following function takes a string as input parameter and prints it on standard screen.

def printme( str ):
   "This prints a passed string into this function"
   print str
   return

"""*******************************************************************"""
# The return Statement:
'''
The statement return [expression] exits a function,
optionally passing back an expression to the caller.
A return statement with no arguments is the same as return None.

All the above examples are not returning any value.
You can return a value from a function as follows'''

#!/usr/bin/python

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them.
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

# Now you can call sum function
total = sum( 10, 20 );
print "Outside the function : ", total

Output:
Inside the function :  30
Outside the function :  30


"""*******************************************************************"""

# Calling a Function:
'''
Defining a function only gives it a name,
specifies the parameters that are to be included in the function
and structures the blocks of code.

Once the basic structure of a function is finalized,
you can execute it by calling it from another function or directly from the Python prompt.'''

# Following is the example to call printme() function :

#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function

printme("I'm first call to user defined function!")

printme("Again second call to the same function")

Output:
I'm first call to user defined function!
Again second call to the same function
"""*******************************************************************"""
# Pass by reference vs value:
"""
All parameters (arguments) in the Python language are passed by reference.

It means if you change what a parameter refers to within a function,
the change also reflects back in the calling function."""

# Example:
#!/usr/bin/python

# Function definition is here
def CentOS( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function

mylist = [10,20,30]

CentOS( mylist )

print ("Values outside the function: ", mylist)

'''Note: Here, we are maintaining reference of the passed object and appending values
in the same object.'''

Output:
Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]
"""*******************************************************************"""
"""Note: There is one more example where argument is being passed by reference and
the reference is being overwritten inside the called function."""

#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

'''Note: The parameter mylist is local to the function changeme.
Changing mylist within the function does not affect mylist. '''

Output:
Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]
"""*******************************************************************"""
# Function Arguments:
'''
You can call a function by using the following types of formal arguments:

1. Required arguments

2. Keyword arguments

3. Default arguments

4. Variable-length arguments
'''

# 1. Required arguments:
'''
Required arguments are the arguments passed to a function in correct positional order.
Here, the number of arguments in the function call should match exactly with the function definition.

To call the function printme(), you definitely need to pass one argument,
otherwise it gives a syntax error as follows:'''

#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
a=10
printme(a)

Output:
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    printme();
TypeError: printme() takes exactly 1 argument (0 given)

"""*******************************************************************"""

# 2. Keyword arguments:
'''
Keyword arguments are related to the function calls.
When you use keyword arguments in a function call, the caller identifies the arguments
by the parameter name.

This allows you to skip arguments or place them out of order because the
Python interpreter is able to use the keywords provided to match the values with parameters.'''

#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return

# Now you can call printme function
printme( str = "My string")

Example:

# My string:
#!/usr/bin/python

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return

# Now you can call printinfo function
printinfo( age=50, name="miki" )

Output:
Name:  miki
Age  50

"""*******************************************************************"""
# 3. Default arguments:
'''
A default argument is an argument that assumes a default value if a
value is not provided in the function call for that argument.

The following example gives an idea on default arguments,
it prints default age if it is not passed'''

#!/usr/bin/python

# Function definition is here
def info( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call info function
info( age=50, name="Guido" )
# Calling a Funtion
info(name="Rossum" )

Output:
Name:  miki
Age  50
Name:  miki
Age  35

"""*******************************************************************"""

# 4. Variable-length arguments:
'''
You may need to process a function for more arguments than you specified while defining the function.
These arguments are called variable-length arguments and are not named
in the function definition,
unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this :'''

def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]

'''Note: An asterisk (*) is placed before the variable name that
holds the values of all
nonkeyword variable arguments.

This tuple remains empty if no additional arguments are specified during the function call.'''

#!/usr/bin/python

# Function definition is here
def info( arg1, *vartuple ):
   #This prints a variable passed arguments
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print(var)
   return

# Now you can call printinfo function
info( 10 )
info( 70, 60, 50 )

Output:
Output is:
10
Output is:
70
60
50
"""