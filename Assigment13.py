
# coding: utf-8

# In[4]:


#Create a sql db from adult dataset and name it sqldb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

from pandas import DataFrame, Series
import sqlite3 as db
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

sqladb = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", names=[
    'age','workclass','fnlwgt','education','education-num','marital-status','occupation', 
    'relationship','race','sex','capital-gain','capital-loss','hoursPerWeek','native-country','x'])
sqladb


# In[7]:


#Select 10 records from the adult sqldb

pysqldf("""SELECT * FROM sqladb LIMIT 10 """)


# In[8]:


#Showme the average hours per week of all men who are working in private sector

#sqladb['workclass']

sqladb['hoursPerWeek'] = pd.to_numeric(sqladb['hoursPerWeek'])
sqladb['hoursPerWeek']
pysqldf("""SELECT workclass, MAX("sqladb.hours-per-week") FROM sqladb 
            WHERE sex NOT LIKE '%Female%' 
            GROUP BY workclass; """)

