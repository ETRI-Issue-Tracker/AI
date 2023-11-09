#!/usr/bin/env python
# coding: utf-8

# In[12]:


from fastapi import FastAPI
import domain
import os

path = "domain"
file_list = os.listdir(path)
print ("file_list: {}".format(file_list))
from domain import sentenceclassification
app = FastAPI()
app.include_router(sentenceclassification.router)