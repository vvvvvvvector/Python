import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

dataFrame = pd.read_csv(url, names=['sepal length', 'sepal width', 'petal length', 'petal width', 'target'])

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = dataFrame.loc[:, features].values
y = dataFrame.loc[:, ['target']].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
print(pca.explained_variance_ratio_.sum())
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
print(principalDf.head(5))
