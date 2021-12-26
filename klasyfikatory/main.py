# 1
from sklearn.linear_model import LogisticRegression
# 2
from sklearn import tree
# 3
from sklearn.ensemble import RandomForestClassifier
# 4
from sklearn.svm import SVC
# 5
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [168, 75, 41], [168, 77, 41], [190, 70, 43],
     [154, 75, 38], [181, 65, 40]]

Y = ['x', 'x', 'y', 'y', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'y', 'y', 'x', 'y', 'x']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=41)

lReg_acc = 0
decisionTree_acc = 0
svc_acc = 0
kNeighbors_acc = 0
randomForest_acc = 0

for test in range(100):
    # 1. Logistic regression
    l_reg = LogisticRegression()
    l_reg.fit(x_train, y_train)
    l_reg_prediction = l_reg.predict(x_test)

    # 2. Decision tree
    decisionTree = tree.DecisionTreeClassifier()
    decisionTree.fit(x_train, y_train)
    decisionTree_prediction = decisionTree.predict(x_test)

    # 3. Random forest
    randomForest = RandomForestClassifier(n_estimators=100)
    randomForest.fit(x_train, y_train)
    randomForest_prediction = randomForest.predict(x_test)

    # 4. SVC
    svc = SVC()
    svc.fit(x_train, y_train)
    svc_prediction = svc.predict(x_test)

    # 5. k neighbours
    kNeighbors = KNeighborsClassifier()
    kNeighbors.fit(x_train, y_train)
    kNeighbors_prediction = kNeighbors.predict(x_test)

    lReg_acc += accuracy_score(l_reg_prediction, y_test)
    decisionTree_acc += accuracy_score(decisionTree_prediction, y_test)
    randomForest_acc += accuracy_score(randomForest_prediction, y_test)
    svc_acc += accuracy_score(svc_prediction, y_test)
    kNeighbors_acc += accuracy_score(kNeighbors_prediction, y_test)

print('logical regression = %f' % lReg_acc)
print('Decision tree = %f' % decisionTree_acc)
print('Random forest = %f' % randomForest_acc)
print('svc = %f' % svc_acc)
print('k neighbours = %f' % kNeighbors_acc)
