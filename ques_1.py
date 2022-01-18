# Name= Rithik
# SID= 21103054
# Branch= CSE

# question 1
input_string=("Python is a case sensitive language")
# part (a)
#finding length of string
length=len(input_string)
print("part (a)")
print("length of the string is ",(length))

# part (b)
#reversing the order of string
print("part (b)")
print(input_string[::-1])

# part (c)
# storing a part of a string in new string
print("part (c)")
new_string=(input_string[10:27])
print("new string =",(new_string))

# part (d)
# replacing "a case sensitive part" with "object oriented" 
replaced_string=(input_string.replace('a case sensitive', 'a object oriented'))
print("part (d)")
print("new replaced string=",(replaced_string))

# part (e)
# finding index of substring a
print("part (e)")
print(input_string.find("a"))

#part (f)
#removing white spaces
print("part (f)")
print(input_string.replace(" ", ""))


