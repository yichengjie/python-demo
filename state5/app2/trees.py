from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for fectVec in dataSet:
		currentLabel = fectVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel]= 0
		labelCounts[currentLabel] += 1
	#print('labelCounts : ' , labelCounts)
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]/numEntries)
		#print('key : %s ,  prob : %f' %(key,prob))
		tmp = -prob * log(prob,2)
		print('tmp : ', tmp)
		#shannonEnt -= prob * log(prob,2)
		shannonEnt += tmp
	return shannonEnt


def splitDataSet(dataSet,axis,value):
	retDataSet = [] 
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			#print('xxx : ' , reducedFeatVec)
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet