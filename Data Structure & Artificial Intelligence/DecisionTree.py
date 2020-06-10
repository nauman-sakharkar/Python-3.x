from sklearn import tree
import pandas as pd

df = pd.read_csv("test2.csv")
L = df.values.tolist()

X=[]
Y=[]
for i in L:
    X.append(i[0:3])
    Y.append(i[3])
print(X,Y)
clf=tree.DecisionTreeClassifier(criterion="entropy")
clf=clf.fit(X,Y)
predict=clf.predict([[3,0,100]])
print(predict)
