# Outlier detection with Isolation Forest
from sklearn.datasets import make_gaussian_quantiles
import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

X1, y1 = make_gaussian_quantiles(cov=1., n_samples=1000, n_features=3, n_classes=1, random_state=1)
X1 = pd.DataFrame(X1, columns=['x', 'y', 'z'])
mpl.use('macosx')

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X1['x'], X1['y'], X1['z'], c=X1['z'], cmap='Greens')
plt.show()

clf = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(.12),
                      max_features=1.0, bootstrap=False, n_jobs=-1, random_state=42, verbose=0)
# replace X1 by your dataset!
clf.fit(X1)
pred = clf.predict(X1)
# outliers are stored with anomaly column == -1
X1['anomaly'] = pred
outliers = X1.loc[X1['anomaly'] == -1]
outlier_index = list(outliers.index)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X1['x'], X1['y'], X1['z'], color='g')
ax.scatter3D(X1['x'][outlier_index], X1['y'][outlier_index], X1['z'][outlier_index], color='r')
plt.show()