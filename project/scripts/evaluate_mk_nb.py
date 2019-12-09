import csv
import pandas as pd

truePositive = 0
falsePositive = 0
trueNegative = 0
falseNegative = 0


df_train = pd.read_csv('../output/mk_output_svm.tsv', sep='\t', header=0)

sizeDFTrain = len(df_train.Category)

id=0
while id < sizeDFTrain:
    item = df_train.Category[id]
    if id % 20 < 17:
        if item == 0:
            trueNegative += 1
        else:
            falsePositive += 1
    else:
        if item == 1:
            truePositive += 1
        else:
            falseNegative += 1
    id += 1

print("{} {}".format("truePositive:", truePositive))
print("{} {}".format("trueNegative:", trueNegative))
print("{} {}".format("falsePositive:", falsePositive))
print("{} {}".format("falseNegative:", falseNegative))
print("{} {}".format("Accuracy:",(truePositive+trueNegative)/(float)(falseNegative+falsePositive+trueNegative+truePositive)))
print("{} {}".format("Precision:",truePositive/(float)(falsePositive+truePositive)))
print("{} {}".format("Recall:",truePositive/(float)(falseNegative+truePositive)))

