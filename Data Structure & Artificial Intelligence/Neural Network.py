from sklearn import neural_network
import pandas as pd

df = pd.read_csv("test2.csv")
L = df.values.tolist()

X=[]
Y=[]
for i in L:
    X.append(i[0:3])
    Y.append(i[3:4][0])

nclf=neural_network.MLPClassifier()
nclf=nclf.fit(X,Y)
predict=nclf.predict([[3,0,100]])
print(predict)
