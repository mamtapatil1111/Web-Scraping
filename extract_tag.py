#!/usr/bin/env python
# coding: utf-8

# Step 1: Importing the required libraries

# In[1]:


import requests
from bs4 import BeautifulSoup


# Step 2: Getting the URL and storing it in a variable.

# In[2]:


url = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=941931'


# Step 3: Making a request to the website using the requests library.

# In[3]:


page= requests.get(url)


# In[4]:


page


# Step 4: Using the Beautiful Soup library to get the HTML (raw) data from the website.

# In[5]:


soup= BeautifulSoup(page.text,"html.parser")


# Step 5: Using soup.findAll method to get the respected tag that we are looking for.

# In[6]:


proftags = soup.findAll("span", {"class": "Tag-bs9vf4-0" })


# In[7]:


proftags


# Step 6: Removing all the HTML tags and converting it to a plain text format.

# In[8]:


for mytag in proftags:
    print(mytag.get_text())


# In[ ]:





# In[ ]:




