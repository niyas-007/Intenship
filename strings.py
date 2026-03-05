# name="Niyas"
# print(type(name))

# numbers='00000007'
# print(type(numbers))

# special="*////+=-"
# print(type(special))

# imojjis="◀ ⏺ ▶ ⏸ ⏯ ⏮ ⏭"
# print(type(imojjis))
# print(imojjis)

# company="Quest innovative solutions"
# print(len(company))

# name="Niyas"
# for char in name:
#     print(char,end="-")

# print(ord("A"))
# print(ord("Z"))


# print(chr(65))

"""--------------------------------------------INDEXING-----------------------------------------"""

# s="hellooo"


# print(s[4])


# print(s[-3])


"""--------------------------------------------SLICING------------------------------------------"""


# x='python data types'
# print(x[1:5])


# x='python data types'
# print(x[1:])


# x='python data types'
# print(x[:6])


# x='python data types'
# print(x[::])


# x='python data types'
# print(x[::1])


# x='python data types'
# print(x[::2])

# x='python data types'
# print(x[-1:-5])

# x='python data types'
# print(x[-5:-1])

# x='python data types'
# print(x[-5:17])

# x='python data types'
# print(x[-1:-5:-1])

# x='python data types'
# print(x[::-1])




"""-----------------------------------------------STRING OPERATIONS----------------------------------------------"""

# place="Calicut"
# place+="dist"
# print(place)          # <--[Adding to String is called concatination eg is given  ]




# place="Calicut"
# print(place*2)          # [Repetition operation:-we cannot multiply two strings]




# place="Calicut"
# print(place-"cut")      # [we cannot perform minuse operation in string]



"""-----------------------------------------------STRING METHODS---------------------------------------------------"""


"""[1.Case convertion Methods]"""

# company="Quest"
# print(dir(company))


# company="Quest Calicut"
# print(company.upper())       #[--upper() used to change to uppercase--]


# company="QUEST CALICUT"
# print(company.lower())         #[--lower() used to change to lowercase--]


# company="my name is muhammed niyas"
# print(company.title())               #[--title() used to change first letter of a word to capitalize--]

# company="my name is muhammed niyas"
# print(company.capitalize())             #[--capitalize() used to change first letter of a string to capitalize--]

# name="Niyas"
# print(name.swapcase())                  #[--swapcase() is used to change capital into small and small into capital--]


"""[2.Searching and Finding ]"""

# stack="Python Django"
# print(stack.find("Django"))                  #[--find method used to find the index value of first letter when a word--]
# print(stack.find("Dngo"))                    #[--it will show -1 when the given value is not there or not in odered word--]
                              #[--when "find" is given it will check from left to right  and "rfind" is given from right to left--]

# stack="python Django"
# print(stack.index('h'))
# print(stack.index('ang'))
# print(stack.index('z'))   #[--diffrence between find and index is :-in find the not value is given it will show "-1" 
#                             # but in case of index it will show "error"]


# string="Hello world"
# print(string.count('o'))       #[--To check how many times the word is repeated in a string--]


"""[3.Validation / Checking]"""


"""[4.Modification / Replacement]"""

# a = 'Python Django'
# s=a.replace('D','d')
# print(s)                          #[--To replace any value in a string--]


# string="      Helloo   "
# print(string.strip())               #[--Used to remove the whitespaces in starting and Ending of a string--]


# s="-------helloo-------"
# print(s.strip('-'))        #[--We can also remove any characters before and after the given string using strip by specifing it in brackets--]


# string="----Helloo---"
# print(string.lstrip('-'))    #[--"lstrip() removes the left side spaces or given value--"]


# string="----Helloo---"
# print(string.rstrip('-'))    #[--"lstrip() removes the right side spaces or given value--"]


# name='Mr.Niyas'
# print(name.removeprefix('Mr.'))  #[--Remove the given prefix we want to pass atleast an argument--]


# name='Mr.Niyas'
# print(name.removesuffix('as'))  #[--Remove the given word from right to left we want to pass atleast an argument--]



"""[5.Formating and Alignment]"""


s="python"
print(s.center(25,'*'))