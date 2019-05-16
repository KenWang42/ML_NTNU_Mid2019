import pandas as pd
import math

data = pd.read_csv('dataset.txt')
resultCol = 'Target'
posValue = 'yes'
negValue = 'no'


def calEntropy(pos, neg):
    sum = pos + neg
    ent = 0
    if (sum > 0):
        p = pos/sum
        n = neg/sum
        if(p > 0.0)and(n > 0.0):
            ent = 0.0
            for x in [p, n]:
                ent = ent - x * math.log(x, 2)
    return ent


def calInfoGain(col):
    pos = len(data.loc[data[resultCol] == posValue])
    neg = len(data.loc[data[resultCol] == negValue])
    ig = calEntropy(pos, neg)
    total = len(data)
    allValue = data[col].unique()
    for curValue in allValue:
        posNum = len(data.loc[(data[col] == curValue) & (data[resultCol] == posValue)])
        negNum = len(data.loc[(data[col] == curValue) & (data[resultCol] == negValue)])
        size = (posNum + negNum) / total
        ent = calEntropy(posNum, negNum)
        print('Col', col, 'Value', curValue, 'pos', posNum, 'neg', negNum, 'Entropy', ent, 'Size', size)
        ig = ig - size * ent
    return ig


pos = len(data.loc[data[resultCol] == posValue])
neg = len(data.loc[data[resultCol] == negValue])
print('Entropy: ', calEntropy(pos, neg))
print('Information Gain of Attributes Size: ', calInfoGain('Size'))
print('Information Gain of Attributes Age: ', calInfoGain('Age'))