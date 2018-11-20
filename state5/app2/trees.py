from math import log
import operator

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
		#print('tmp : ', tmp)
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

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	#print('baseEntropy : ' , baseEntropy)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		#print('featList : ' , featList)
		uniqueVals = set(featList)
		#print('uniqueVals : ' , uniqueVals)
		newEntropy = 0.0
		for value in uniqueVals:
			#print('vlaue : ' , value)
			subDataSet = splitDataSet(dataSet,i,value)
			#print('subDataSet : ' , subDataSet)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain) :
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature


def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classList.keys():
			classCount[vote] = 0
		classCount[vote] += 1
		sortedClassCount = sorted(classCount.items,key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)

	
	pass







