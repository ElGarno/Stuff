import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

import scipy
import scipy.stats as st

from scipy.stats import norm

# read the file
titanic = pd.read_csv('titanic.csv')
# Convert categorical variable to numeric
titanic["Gender"] = np.where(titanic["Sex"] == "male", 0, 1)

titanic = titanic[["Survived", "Pclass", "Gender", "Age", "SibSp", "Parch", "Fare"]].dropna(axis=0, how='any')
titanic.count(axis=0)  # how many rows are left?

# display the first lines
print(titanic.head(10))
print(titanic.describe())
# plot pairs to see the correlation between the data
sns.pairplot(titanic[["Survived", "Gender", "Age", "Pclass", "Fare"]], diag_kind="kde", kind="reg")
plt.show()
# subset only women
titanic_women = titanic.loc[titanic.Gender == 1]
titanic_men = titanic.loc[titanic.Gender == 0]
print(titanic_women)
print(titanic_women.describe())
print(titanic_men.describe())

