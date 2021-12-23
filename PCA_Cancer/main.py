import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

dataFrame = pd.read_csv('Files/Cancer.csv')

del dataFrame['id']
del dataFrame['diagnosis']
del dataFrame['Unnamed: 32']

# print(dataFrame)

x = dataFrame.values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=7)
principalComponents = pca.fit_transform(x)
principalDF = pd.DataFrame(data=principalComponents
                           , columns=['PC_1', 'PC_2', 'PC_3', 'PC_4', 'PC_5', 'PC_6', 'PC_7'])

print('zmiennosc calkowita = %f %%' % (pca.explained_variance_ratio_.sum() * 100))

print(principalDF)
