#!/usr/bin/env python
# coding: utf-8

# In[3]:


#using if,elif,else conditional statements

n=int(input("enter a number:"))
if(n%2!=0):
    print("weird")
elif(2<=n<=5):
    print("not weird")
elif(6<=n<=20):
    print("weird")
elif(n>=20):
    print("not weird")

