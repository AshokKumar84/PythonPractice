# NumPy: This is a general-purpose library that provides numerical arrays, and
# functions to manipulate the arrays efficiently.

# SciPy: This is a scientific computing library that provides science and engineering
# related functions. SciPy supplements and slightly overlaps NumPy. NumPy and
# SciPy historically shared their code base but were later separated.

# Pandas: This is a data-manipulation library that provides data structures and
# operations for manipulating tables and time series data.

# Matplotlib: This is a 2D plotting library that provides support for producing
# plots, graphs, and figures. Matplotlib is used by SciPy and supports NumPy.

# IPython: This provides a powerful interactive shell for Python, kernel for Jupyter,
# and support for interactive data visualization. 

# Jupyter Notebook: This provides a web-based interactive shell for creating and
# sharing documents with live code and visualizations. Jupyter Notebook supports
# multiple versions of Python through the kernel provided by IPython.

# Reference: https://towardsdatascience.com/a-complete-yet-simple-guide-to-move-from-excel-to-python-d664e5683039

import numpy as np
import pandas as pd

df_excel = pd.read_csv('E:\Work\GitHub\PythonPractice\Data Science\StudentsPerformance.csv')
# df_excel.describe()
df_excel['gender'].value_counts()

df_excel.head()
df_excel["math score"]
df_excel.info()

df_excel['math score'].mean()
df_excel['math score'].max()
df_excel['math score'].min()
df_excel['math score'].count()

# In [1]: df_excel['math score'].mean()

# Average of 3 scores
df_excel['average'] = (df_excel['math score'] + df_excel['reading score'] + df_excel['writing score'])/3
df_excel['average'] = df_excel.mean(axis=1)
df_excel['average']

# IF formula in Excel
df_excel['pass/fail'] = np.where(df_excel['average'] > 70, 'Pass', 'Fail')
df_excel['pass/fail']

# Nested IF informula  Excel
conditions = [
    (df_excel['average']>=90),
    (df_excel['average']>=80) & (df_excel['average']<90),
    (df_excel['average']>=70) & (df_excel['average']<80),
    (df_excel['average']>=60) & (df_excel['average']<70),
    (df_excel['average']>=50) & (df_excel['average']<60),
    (df_excel['average']<50),
]
values = ['A', 'B', 'C', 'D', 'E', 'F']

df_excel['grades'] = np.select(conditions, values)
df_excel['average'], df_excel['grades']
df_excel[['average', 'pass/fail', 'grades']]
df_excel.head()

df_female = df_excel[df_excel['gender'] == 'female']    # Select the female gender and output to data frame
df_female.head()

# In case 2 conditions remember each condition should be in parenthesis
df_sumifs = df_excel[(df_excel['gender'] == 'female') & (df_excel['race/ethnicity'] == 'group B')]
df_sumifs.head()

df_sumifs = df_sumifs.assign(sumifs=df_sumifs['math score'] + df_sumifs['reading score'] + df_sumifs['writing score'])
df_sumifs.head()

df_excel['gender'].str.title()
df_excel['gender'].str.upper()
df_excel['gender'].str.title()

df_excel['gender'] = df_excel['gender'].str.title()
df_excel['gender'].str.title()
