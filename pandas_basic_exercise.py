import pandas as pd
import numpy as  np

data = np.array(['a', 'b', 'c', 'd'])

s = pd.Series(data)

print s
print "--------------------"

data = [['Alex',10],['Bob',12],['Clarke',13]]
d = pd.DataFrame(data, columns=['Name', 'Age'])

print d
print "---------------------"

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
d = pd.DataFrame(data)

print d
print "---------------------"

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
d = pd.DataFrame(data)
print d
print "--------------------"

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print df1
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print df2
print "----------------------"


d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df['one']
print "-----------------------"


df['three'] = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print df.loc['b']
print df.iloc[2]