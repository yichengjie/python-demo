import trees
import data_set 


dataSet , labels = data_set.createDataSet()

#print(dataSet)

#shan = trees.calcShannonEnt(dataSet)

#print('shan : ' , shan)

ret = trees.splitDataSet(dataSet,0,1)

print(ret)




