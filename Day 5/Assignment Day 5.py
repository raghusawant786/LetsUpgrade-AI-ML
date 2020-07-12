#!/usr/bin/env python
# coding: utf-8

# Question 1 :
# Write a Python program to find the first 20 non-even prime natural numbers

# In[11]:


num =20
for num in range(2, num):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# Question 2 :
# Write a Python program to implement 15 functions of string.
# 

# In[21]:


user_string = "China"
print(user_string.isalnum())
    
user_string = "1974"
print(user_string.isdigit())
 
user_string = "Australia"
print(user_string.isalpha())
 
user_string = "   "
print(user_string.isspace())
 
user_string = "JAPAN"
print(user_string.isupper())
 
user_string = "Australia 1974"
print(user_string.islower())
 
user_string = "India 1974"
print(user_string.lower())
print(user_string.upper())

user_string = "America Russia Japan China"
print('\nStrip with Character A:', user_string.strip('A'))
print('Strip with Character a:', user_string.strip('a'))

user_string = "Columbia"
print(user_string.endswith('bia'))
print(user_string.endswith('mia'))

user_string = "Columbia"
print(user_string.startswith('Colum'))
print(user_string.startswith('Rolum'))
 
user_string = "Columbia"
print(user_string.find('lumbia'))
 
user_string = "Hello Columbia"
old = "Columbia"
new = "Russia"
print(user_string.replace(old, new))


# Question 3:
# Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
# Display the message accordingly to the user.
# 

# In[24]:


s1="ana"
s2="naa"
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")


# In[25]:


# Program to check if a string is palindrome or not

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# Question 4:
# Write a Python's user defined function that removes all the additional characters from the string
# and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle
# @AI-ML Trainer", then the output be "drdarshaningleaimltrainer".

# In[36]:


def sample(a_string):
    alphanumeric=""
    for character in a_string:
        if character.isalnum():
            alphanumeric += character
    print(alphanumeric.lower())


# In[37]:


sample("Dr. Darshan Ingle @AI-ML Trainer")


# In[ ]:




