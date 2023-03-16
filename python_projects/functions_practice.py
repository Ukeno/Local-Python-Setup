def hello():
    print("\n"'nothing') # prints nothing
    # whitespace
hello()

# --------------------------------------------------------------------

def pack():
    s = '-- Second'
    print(s)
    # whitespce             main program
print('First')       # prints before calling pack()
pack()               # prints (s)
print('Third')       # prints after calling pack()

# --------------------------------------------------------------------

def eat_lunch(list1):
  for x in list1:
    print(x)

list1 = ["First i eat apple", "Next i eat banana", "Last i eat cherry"]
    # whitespace
list2 = [] # If list2 is empty it will pass "if" on to "else"
    # whitespace
if list2:
    print("Lunchbox not empty!") 
else:
   print("Lunchbox empty!")   

eat_lunch(list2)