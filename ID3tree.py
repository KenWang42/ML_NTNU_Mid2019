from math import log
import operator


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
# 給所有可能的分類創建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
# 以2為底計算墒
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


# 對離散變數劃分資料集, 取出特徵為value的所有樣本
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])  # 把axis項拔掉
            retDataSet.append(reducedFeatVec)  # 鑲嵌進去
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1  # 減掉label的column
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):  # 對每種Features
        featList = [example[i] for example in dataSet]  # 所有該Feature的example集
        uniqueVals = set(featList)  # 不重複變數集
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]  # 如果每個點的class都一樣 完成
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)  # 如果沒東西了 完成
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])  # 將做完的Feature刪掉
    featValue = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValue)
    for value in uniqueVals:
        subLabels = labels[:]  # 複製所有label
        subDataSet = splitDataSet(dataSet, bestFeat, value)
        myTree[bestFeatLabel][value] = createTree(subDataSet, subLabels)
    return myTree


fr = open('dataset.txt')
dataset = [inst.strip().split(',') for inst in fr.readlines()]
feat_name = ['Height', 'Weight', 'Temperature', 'Target']
myTree = createTree(dataset, feat_name)
print(myTree)


def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel


labels = ['Height', 'Weight', 'Temperature']
test1 = ['large', 'heavy', 'normal']
test2 = ['large', 'normal', 'cold']
test3 = ['medium', 'heavy', 'cold']
test4 = ['large', 'normal', 'hot']
test5 = ['small', 'normal', 'cold']

print(classify(myTree, labels, test1))
print(classify(myTree, labels, test2))
print(classify(myTree, labels, test3))
print(classify(myTree, labels, test4))
print(classify(myTree, labels, test5))