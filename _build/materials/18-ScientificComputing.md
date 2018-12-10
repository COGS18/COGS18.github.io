---
interact_link: content/materials/18-ScientificComputing.ipynb
download_link: assets/downloads/18-ScientificComputing.ipynb.zip
pdf_link: assets/pdf/18-ScientificComputing.pdf
layout: materials
title: '18-ScientificComputing'
prev_page:
  url: /materials/17-APIs
  title: '17-APIs'
next_page:
  url: /materials/19-OpenSource
  title: '19-OpenSource'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Scientific Computing

## Scientific Computing

<div class="alert alert-success">
Scientific Computing is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
</div>

## Scientific Python: Scipy Stack

<div class="alert alert-success">
Scipy is an 'ecosystem', including a collection of open-source packages for scientific computing in Python.
</div>

## Homogenous Data

### numpy



{:.input_area}
```python
import numpy as np
```




{:.input_area}
```python
# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
```




{:.input_area}
```python
arr1
```





{:.output_data_text}
```
array([[1, 2],
       [3, 4]])
```



#### Indexing Arrays



{:.input_area}
```python
# Check out an array of data
arr1
```





{:.output_data_text}
```
array([[1, 2],
       [3, 4]])
```





{:.input_area}
```python
# Check the shape of the array
arr1.shape
```





{:.output_data_text}
```
(2, 2)
```





{:.input_area}
```python
# Index into a numpy array
arr1[1, 1]
```





{:.output_data_text}
```
4
```



#### Working with Arrays



{:.input_area}
```python
# Add arrays together
arr1 + arr2
```





{:.output_data_text}
```
array([[ 6,  8],
       [10, 12]])
```





{:.input_area}
```python
# Matrix mutliplication
arr1 * arr2
```





{:.output_data_text}
```
array([[ 5, 12],
       [21, 32]])
```



### Clicker Question #1

Given the following code, what will it print out?



{:.input_area}
```python
data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0, :], data[1, :]):
    output.append(d1 + d2)

print(output)
```


{:.output_stream}
```
[6, 8, 10, 12]

```

A) [1, 2, 3, 4] | B) [1, 2, 3, 4, 5, 6, 7, 8] | C) [6, 8, 10, 12] | D) [10, 26] | E) [36]

## Heterogenous Data

### pandas



{:.input_area}
```python
import pandas as pd
```




{:.input_area}
```python
# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
```




{:.input_area}
```python
# Create a dataframe 
df = pd.DataFrame([d1, d2], [0, 1])
```




{:.input_area}
```python
# Check out the dataframe
df
```





<div markdown="0">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Subj_ID</th>
      <th>condition</th>
      <th>group</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>001</td>
      <td>cognition</td>
      <td>2</td>
      <td>16</td>
    </tr>
    <tr>
      <th>1</th>
      <td>002</td>
      <td>perception</td>
      <td>1</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>
</div>



#### Working with DataFrames



{:.input_area}
```python
df.describe()
```





<div markdown="0">
<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>group</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.500000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.707107</td>
      <td>4.242641</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.250000</td>
      <td>17.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.500000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.750000</td>
      <td>20.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.000000</td>
      <td>22.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>





{:.input_area}
```python
# Take the average of all numeric columns
df.m ean()
```





{:.output_data_text}
```
Subj_ID    501.0
group        1.5
score       19.0
dtype: float64
```



### Clicker Question #2

Comparing them to standard library Python types, which is the best mapping for these new data types?

- A) DataFrames are like lists, arrays are like tuples
- B) DataFrames and arrays are like lists
- C) DataFrames are like tuples, arrays are like lists
- D) DataFrames and arrays are like dictionaries
- E) Dataframes are like dictionaries, arrays are like lists

## Plotting



{:.input_area}
```python
%matplotlib inline

import matplotlib.pyplot as plt
```




{:.input_area}
```python
# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])
```




{:.input_area}
```python
# Plot the data
plt.plot(dat)
```





{:.output_data_text}
```
[<matplotlib.lines.Line2D at 0x10fe68c18>]
```




![png](../images/build/materials/18-ScientificComputing_33_1.png)


## Analysis



{:.input_area}
```python
import scipy as sp
from scipy import stats
```




{:.input_area}
```python
# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)
```


### Analysis - Plotting the Data



{:.input_area}
```python
# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);
```



![png](../images/build/materials/18-ScientificComputing_38_0.png)


### Analysis - Statistical Comparisons



{:.input_area}
```python
# Statistically compare the two distributions
stats.ttest_ind(d1, d2)
```





{:.output_data_text}
```
Ttest_indResult(statistic=-9.8514621184205282, pvalue=2.1664258801374293e-22)
```



## COGS108: Data Science in Practice

<div class="alert alert-info">
If you are interested in data science and scientific computing in Python, consider taking [COGS108](https://github.com/cogs108/).
</div>
