#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''Research on whether addition, subtraction, multiplication, division, floor division and modulo
operations be performed on complex numbers. Based on your study, implement a Python
program to demonstrate these operations'''

a= (4+3j)
b= (3-7j)
print("Addition of two complex numbers : ",a+b)

print("Subtraction of two complex numbers : ",a-b)
print("multiplication of two complex numbers : ",a*b)
print("division of two complex numbers : ",a/b)



# In[6]:


(3+6j) % (4+2j) # we cannot perfom modulos operation to complex number


# In[7]:


(3+6j) // (4+2j) # We cannot perform floor division operation to complex number


# 
# 2.) Research on range() function and its parameter,Create markdown cell and write in your own words what you understand aboutit. implement small program of your choice on the same.
# 
# i.) range(n) function it goes from 0 to n-1 to generate sequence of number ii.) it used with loops(eg. for loop) iii.) range() is a buit-in function of python iv.) used to perform user action v) range() have three parameter like range(start,end,stepsize)

# In[8]:


for i in range(3,20,2):
    print(i)


# 3.) consider two numbers.perform their substraction and if the result of substraction is greater than 25, print their multiplication result else print their division result.

# In[10]:


a=125
b=50
 
if((a-b)>25):
    print("multiplication result of a and b is : ",a*b)
else:
    print("division result of a and b is :",a/b)


# 4.) consider a list of 10 elements of integer values.if the number in the list is divisible by 2,print the result as " square of that number minus 2"

# In[11]:


L =[10,25,30,35,65,86,36,16,84,72]
for i in L:
    if(i%2==0):
        print("the square of no ",i,"is",(i**2)-2)


# 
# 5.) consider a list of 10 elements.print all the elements in the list which are greater than 7 when that number is divided 2.

# In[12]:


L =[10,25,30,35,8,5,36,9,84,72]
for i in L:
     if(i/2>7):
            print("The number ",i,"which is greater than 7 after it divided by 2")


# In[ ]:




