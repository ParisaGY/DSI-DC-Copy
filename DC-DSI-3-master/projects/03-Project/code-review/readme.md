## Code Review

J, Swara, and Phil provided their notebooks as a code review. Their notebooks are provided here for your reference.

Recall, we had a few specific points come up from the class.

### .format()

Ritika showed us the values of using `.format()` to "fill in {} blanks" easier:

```python
url_template = "http://www.indeed.com/jobs?q=data+scientist+%2420%2C000&l={}&limit=100&start={}"
max_results_per_city = 800 # Set this to a high-value (5000) to generate more results. 

for city in set(list_of_cities):
    for start in range(0, max_results_per_city, 100):       
        url = url_template.format(city, start)
```

### np.where

Kate talked about using `np.where()` to more efficiently find matching conditions.

```python
# Example of using np.where
data['binary_salari'] = np.where(data['salary'] >= median, 1,0)

# will put 1 if the salary is above median and 0 if the salary is below median in a new column called 'binary_salari'
```

### nan

We can create nan data types using `np.nan` or `float('NaN')`


### .partition('-')

Jay showed us using `partition()` in his notebook. It's available in this folder.


### del

Avinash told us about using the (scary) ability to drop a dataframe from memory. `del df`


### Functional Programming

Python is object-oriented. However, we should still make use of functional programming's speed as much as possible. Therefore, we should always err on the side of using functions in place of loops. (mapping, lamdba, apply, etc)

See [Python performance tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Loops)
