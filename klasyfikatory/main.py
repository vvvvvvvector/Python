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

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43], [168, 77, 41]]

Y = ['x', 'x', 'y', 'y', 'x', 'x', 'y', 'y', 'y', 'x', 'x', 'y']

test_data = [[190, 70, 43], [154, 75, 38], [181, 65, 40], [168, 75, 41]]
test_labels = ['x', 'y', 'x', 'y']

lReg_acc = 0
decisionTree_acc = 0
svc_acc = 0
kNeighbors_acc = 0
randomForest_acc = 0

for test in range(100):
    # 1. Logistic regression
    l_reg = LogisticRegression()
    l_reg.fit(X, Y)
    l_reg_prediction = l_reg.predict(test_data)

    # 2. Decision tree
    decisionTree = tree.DecisionTreeClassifier()
    decisionTree.fit(X, Y)
    decisionTree_prediction = decisionTree.predict(test_data)

    # 3. Random forest
    randomForest = RandomForestClassifier(n_estimators=100)
    randomForest.fit(X, Y)
    randomForest_prediction = randomForest.predict(test_data)

    # 4. SVC
    svc = SVC()
    svc.fit(X, Y)
    svc_prediction = svc.predict(test_data)

    # 5. k neighbours
    kNeighbors = KNeighborsClassifier()
    kNeighbors.fit(X, Y)
    kNeighbors_prediction = kNeighbors.predict(test_data)

    lReg_acc += accuracy_score(l_reg_prediction, test_labels)
    decisionTree_acc += accuracy_score(decisionTree_prediction, test_labels)
    randomForest_acc += accuracy_score(randomForest_prediction, test_labels)
    svc_acc += accuracy_score(svc_prediction, test_labels)
    kNeighbors_acc += accuracy_score(kNeighbors_prediction, test_labels)

print('logical regression = %f' % lReg_acc)
print('Decision tree = %f' % decisionTree_acc)
print('Random forest = %f' % randomForest_acc)
print('svc = %f' % svc_acc)
print('k neighbours = %f' % kNeighbors_acc)
