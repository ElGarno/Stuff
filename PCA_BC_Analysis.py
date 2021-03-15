from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# from keras.datasets import cifar10
import numpy as np
import pandas as pd
import math


breast = load_breast_cancer()
breast_data = breast.data
breast_labels = breast.target

# reshape
labels = np.reshape(breast_labels, (569, 1))
final_breast_data = np.concatenate([breast_data, labels], axis=1)
print(final_breast_data.shape)
breast_dataset = pd.DataFrame(final_breast_data)
features = breast.feature_names
print(features)
features_labels = np.append(features, 'label')
breast_dataset.columns = features_labels
print(breast_dataset.head())

# change labels
breast_dataset['label'].replace(0, 'Benign', inplace=True)
breast_dataset['label'].replace(1, 'Malignant', inplace=True)

label_dict = {1: 'Benign',
              2: 'Malignant'}

feature_dict = {0: 'mean radius',
                1: 'mean texture',
                2: 'mean perimeter',
                3: 'mean area',
                4: 'mean smoothness',
                5: 'mean compactness',
                6: 'mean concavity',
                7: 'mean concave points',
                8: 'mean symmetry',
                9: 'mean fractal dimension',
                10: 'radius error',
                11: 'texture error',
                12: 'perimeter error',
                13: 'area error',
                14: 'smoothness error',
                15: 'compactness error',
                16: 'concavity error',
                17: 'concave points error',
                18: 'symmetry error',
                19: 'fractal dimension error',
                20: 'worst radius',
                21: 'worst texture',
                22: 'worst perimeter',
                23: 'worst area',
                24: 'worst smoothness',
                25: 'worst compactness',
                26: 'worst concavity',
                27: 'worst concave points',
                28: 'worst symmetry',
                29: 'worst fractal dimension'}

X = breast_dataset.loc[:, features].values
y = breast_dataset.iloc[:, 30].values
with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(8, 6))
    for cnt in range(30):
        plt.subplot(3, 10, cnt+1)
        for lab in ('Benign', 'Malignant'):
            plt.hist(X[y==lab, cnt],
                     label=lab,
                     bins=10,
                     alpha=0.3,)
        plt.xlabel(feature_dict[cnt])
    plt.legend(loc='upper right', fancybox=True, fontsize=8)

    plt.tight_layout()
    plt.show()

# print
print(breast_dataset.tail())

# CIFAR - 10
# (x_train, y_train), (x_test, y_test) = cifar10.load_data()

x = breast_dataset.loc[:, features].values
# normalizing the features
x = StandardScaler().fit_transform(x)

feat_cols = ['feature'+str(i) for i in range(x.shape[1])]
normalised_breast = pd.DataFrame(x, columns=feat_cols)
print(normalised_breast.tail())

pca_breast = PCA(n_components=2)
principalComponents_breast = pca_breast.fit_transform(x)
principal_breast_Df = pd.DataFrame(data=principalComponents_breast, columns=['principal component 1',
                                                                             'principal component 2'])
print(principal_breast_Df.tail())
print('Explained variation per principal component: {}'.format(pca_breast.explained_variance_ratio_))

plt.figure()
plt.figure(figsize=(10, 10))
plt.xticks(fontsize=12)
plt.yticks(fontsize=14)
plt.xlabel('Principal Component - 1', fontsize=20)
plt.ylabel('Principal Component - 2', fontsize=20)
plt.title("Principal Component Analysis of Breast Cancer Dataset", fontsize=20)
targets = ['Benign', 'Malignant']
colors = ['r', 'g']
for target, color in zip(targets, colors):
    indicesToKeep = breast_dataset['label'] == target
    plt.scatter(principal_breast_Df.loc[indicesToKeep, 'principal component 1'],
                principal_breast_Df.loc[indicesToKeep, 'principal component 2'], c=color, s=50)

plt.legend(targets, prop={'size': 15})
plt.show()