from numpy import *
import operator


def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0] # 返回4

	# 矩阵相减
	difMat = tile(inX,(dataSetSize,1)) - dataSet #
	# 矩阵平方
	sqDiffMat = difMat **2
	# 矩阵元素按行相加
	sqDistances = sqDiffMat.sum(axis=1)
	# 矩阵开平方
	distances = sqDistances **0.5
	# 获取值大小排序的index，返回 2，0，1等
	sortedDistIndicies = distances.argsort()
	classCount = {}
	#print(sortedDistIndicies)
	for i in range(k):
		# 距离最近的index
		si = sortedDistIndicies[i] 
		# A | B
		voteIlabel = labels[si]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	# classCount 最终的集合为	{'A':2,'B':1}等
	# 然后将按照value排序
	print(classCount.items())
	#sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	sortedClassCount = sorted(classCount.items(),key= lambda s : s[1], reverse=True)

	return sortedClassCount[0][0]


