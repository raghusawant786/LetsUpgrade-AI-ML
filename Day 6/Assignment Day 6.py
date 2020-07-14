#!/usr/bin/env python
# coding: utf-8

# Question 1:
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program
# to print the company name of a given email address. Both user names and company names are composed of letters
# only.
# 

# In[13]:


txt = "username@companyname.com"
x = txt.split("@")
y = x[1].split(".")


# In[15]:


print(y[0])


# Question 2:
# Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma
# separated sequence after sorting them alphabetically.

# In[19]:


my_str = "without,hello,bag,world"
new_str=""
# breakdown the string into a list of words
words = my_str.split(",")

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    new_str = new_str + word+","

print(new_str)


# Question 3:
# Create your own Jupyter Notebook for Sets.

# In[20]:


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# Question 4:
# Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
# 

# In[33]:


def getMissingNo(A): 
    n = len(A) 
    total = (n + 1)*(n + 2)/2
    print(total)
    sum_of_A = sum(A) 
    print(sum_of_A)
    return total - sum_of_A 
  
# Driver program to test the above function 
A = [1, 2, 3, 5] 
miss = getMissingNo(A) 
print(miss)


# Question 5:
# With a given list L, write a program to print this list L after removing all duplicate values with original order reserved.
# 

# In[34]:


mylist = [12,24,35,24,88,120,155,88,120,155]
mylist = list(dict.fromkeys(mylist))
print(mylist)


# In[ ]:




