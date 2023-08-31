### Task 1

""" text = "Berlin is a world city of culture, politics, media and science."

print(len(text))
 """


### Task 2

""" text = "Berlin is a world city of culture, politics, media and science."

first = text[0]
last = text[-1]
print(first,last,sep=' ') """


### Task 3

""" text = "Berlin is a world city of culture, politics, media and science."

text1 = text[:3]

print(text1.upper()) 
#or print(text[:3].upper())
"""

### Task 4
""" 
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print('B appears:',text.count('B'),'times') """


### Task 5

""" text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print('Last ten characters:', text[-10:]) """


### Task 6

""" text = '---Python  programming---'

text1 = text.replace('-','')
print(text1) """

# or
#print(text.strip('-')) for removing characters from left or right for right rstrip and for left lstrip

# slicing method
""" text = '---Python --- programming---'
print(text[0:9] + ' ' + text[14:])
 """
### Task 7

first_name = 'Shilpa'
last_name = 'Jordan'

print('Firstname:',first_name,'\n'+'Lastname:', last_name) 