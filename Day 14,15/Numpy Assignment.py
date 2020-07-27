#!/usr/bin/env python
# coding: utf-8

# # 1. Create a 3x3x3 array with random values 

# In[1]:


import numpy as np
array3X3 = np.array([[1.07, 0.44, 1.5],[0.27, 1.13, 1.72],[0.27, 1.13, 1.72]])
array3X3


# # 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# In[2]:


x = np.diag([1, 2, 3, 4, 5])
print(x)


# # 3.Create a 8x8 matrix and fill it with a checkerboard pattern

# In[3]:


x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# # 4. Normalize a 5x5 random matrix

# In[6]:


array3X3 = np.array([[1.07, 0.44, 1.5],[0.27, 1.13, 1.72],[0.27, 1.13, 1.72],[0.55, 8.13, 1.72],[0.78, 3.5, 2.5]])

norm = np.linalg.norm(array3X3)
normal_array = array3X3/norm
print(normal_array)


# # 5.  How to find common values between two arrays?

# In[7]:


array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))


# # 6.How to get the dates of yesterday, today and tomorrow?

# In[8]:


from datetime import datetime, timedelta 
  
  
# Get today's date 
presentday = datetime.now() # or presentday = datetime.today() 
  
# Get Yesterday 
yesterday = presentday - timedelta(1) 
  
# Get Tomorrow 
tomorrow = presentday + timedelta(1) 
  
  
# strftime() is to format date according to 
# the need by converting them to string 
print("Yesterday = ", yesterday.strftime('%d-%m-%Y')) 
print("Today = ", presentday.strftime('%d-%m-%Y')) 
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))


# # 7. Consider two random array A and B, check if they are equal

# In[10]:


an_array = np.array([[1,2],[3,4]])
an_arrayb = np.array([[1,2],[2,4]])
another_array = np.array([[1,2],[3,4]])

comparison = an_array == another_array
comparisonb = an_arrayb == another_array

equal_arrays = comparison.all()
equal_arraysb = comparisonb.all()

print(equal_arrays)
print(equal_arraysb)


# # 8.Create random vector of size 10 and replace the maximum value by 0 

# In[11]:


x = np.random.random(15)
print("Original array:")
print(x)
x[x.argmax()] = -1
print("Maximum value replaced by -1:")
print(x)


# # 9. How to print all the values of an array?

# In[13]:


x = np.zeros((4, 4))
print(x)


# # 10.Subtract the mean of each row of a matrix

# In[14]:


X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# # 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? 

# In[ ]:





# In[ ]:





# # 12.How to get the diagonal of a dot product?

# In[19]:


X = np.array([[1.07, 0.44, 1.5],[0.27, 1.13, 1.72],[0.27, 1.13, 1.72],[0.55, 8.13, 1.72],[0.78, 3.5, 2.5]])
Y = np.array([[1, 0.44, 1.5],[0.5, 1.13, 1.2],[0.7, 1.03, 1.2],[0.65, 2.13, 1.2],[8.78, 3.52, 2.52]])
 
    Z = np.dot(X, Y)
    Z


# # 13.How to find the most frequent value in an array?

# In[22]:


x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())


# # 14.How to get the n largest values of an array

# In[23]:


x = np.arange(10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 1
print (x[np.argsort(x)[-n:]])


# # 15.How to create a record array from a regular array?

# In[21]:


arra1 = np.array([("Yasemin Rayner", 88.5, 90),
                 ("Ayaana Mcnamara", 87, 99),
             ("Jody Preece", 85.5, 91)])
print("Original arrays:")
print(arra1)
print("\nRecord array;")
result = np.core.records.fromarrays(arra1.T,
                              names='col1, col2, col3',
                              formats = 'S80, f8, i8')
print(result)


# In[ ]:




