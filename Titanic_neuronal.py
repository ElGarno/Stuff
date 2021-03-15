# module for plotting
import matplotlib.pyplot as plt
# module for efficient linear algebra computations
import numpy as np
# module for convenient handling of tabular data
import pandas as pd

x = np.linspace(-1,1,1500)
relu = [x if x > 0 else 0 for x in x]
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$ReLU(x)$', fontsize=14)
plt.plot(x, relu)


titanic = pd.read_csv('titanic.csv')
print(titanic.describe())

titanic.info()

# Print the first 5 elements of our dataset
titanic.head()
#Check for missing entries
titanic.isnull().sum()

#Feature selection
titanic = titanic[['Survived', 'Pclass', 'Sex', 'Fare']]

titanic = titanic.dropna()
titanic.info()