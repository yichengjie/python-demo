import knn 
import classify0

group , labels = knn.createDataSet()

# print(group)

inX = (1,0.1)
dataSet = group 
k = 3

t = classify0.classify0(inX,dataSet,labels,k)
print('t : ' , t)

