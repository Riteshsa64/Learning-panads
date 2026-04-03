import numpy as np
import pandas as pd
country = ['India','Pakistan','USA','Nepal','Srilanka']

pd.Series(country)
runs = [13,24,56,78,100]

runs_ser = pd.Series(runs)
print(runs_ser)



# custom index
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

a=pd.Series(marks,index=subjects)
print(a)
# setting a name
marks = pd.Series(marks,index=subjects,name='Nitish ke marks')
print(marks)