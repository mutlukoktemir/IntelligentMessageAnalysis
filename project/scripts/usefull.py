import csv
import pandas as pd
import random
from unicode_tr import unicode_tr


# Python program to convert a list 
# to string using join() function 
    
# Function to convert   
def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 





# with open('../data/TuPC_train_set.txt', 'r') as file:
#     dataString = file.read().replace('\t', '\n')

# dataStringTabed = dataString.split('\n')

# # print(dataStringTabed)

# # f_out = open('../output/mktrain_set.tsv', 'w')


# id=0
# counter = 0
# # f_out.write("label\tcomment\n")
# with open('../output/mktrain_set.tsv', 'wt') as out_file:
#     tsv_writer = csv.writer(out_file, delimiter='\t')
#     tsv_writer.writerow(['label', 'comment'])
#     while id != len(dataStringTabed):
#         if counter % 3 == 2:
#             counter = 0
#         else:
#             tsv_writer.writerow([0, dataStringTabed[id]])
#             # f_out.write(u"0\t{0}\n".format(dataStringTabed[id]))
#             counter += 1
#         id += 1



# read the data into pandas data frame
df_train = pd.read_csv('../data/hb.csv', header=0)
sizeDFTrain = len(df_train.Review)


# string1 = df_train.Review[1]
# string1 = string1[:-1]
# list1 = string1.split(" ")
# print(len(list1))
# print(list1)
# str1 = f.readline()
# str1 = str1[:-1]
# randIndex = random.randint(0,len(list1)-1)
# list1.insert(randIndex,str1)
# print(list1)
# print(len(str1))





# read the data into pandas data frame
df_train = pd.read_csv('../data/hb.csv', header=0)
sizeDFTrain = len(df_train.Review)

fObject = open("../data/blackListTurkish.txt", "r")

counter = 0
myindex = 0
# f_out.write("label\tcomment\n")
with open('../data/mk_train_set.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['label', 'comment'])
    str1 = ""

    while myindex != 200000:
        if myindex % 10 < 7:
            tsv_writer.writerow([ 0, unicode_tr(df_train.Review[myindex]).lower() ])
        else:
            stringTemp = df_train.Review[myindex]
            stringTemp = stringTemp[:-1]
            listTemp = stringTemp.split(" ")

            if counter % 3 == 0: 
                str1 = fObject.readline()
                if str1 == "":
                    fObject.close()
                    fObject = open("../data/blackListTurkish.txt", "r")
                    str1 = fObject.readline()

                str1 = str1[:-1]

            randIndex = random.randint(0,len(listTemp)-1)
            listTemp.insert(randIndex,str1)
            strAdd = listToString(listTemp)
            counter +=1
            tsv_writer.writerow([ 1, unicode_tr(strAdd).lower() ])

        myindex += 1

id = 0
# f_out.write("label\tcomment\n")
with open('../data/mk_test_set.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['test_id', 'comment'])

    while myindex != sizeDFTrain:
        if myindex % 20 < 17:
            tsv_writer.writerow([ id, unicode_tr(df_train.Review[myindex]).lower() ])
        else:
            stringTemp = df_train.Review[myindex]
            stringTemp = stringTemp[:-1]
            listTemp = stringTemp.split(" ")

            if counter % 3 == 0: 
                str1 = fObject.readline()
                if str1 == "":
                    fObject.close()
                    fObject = open("../data/blackListTurkish.txt", "r")
                    str1 = fObject.readline()

                str1 = str1[:-1]

            randIndex = random.randint(0,len(listTemp)-1)
            listTemp.insert(randIndex,str1)
            strAdd = listToString(listTemp)
            counter +=1
            tsv_writer.writerow([ id, unicode_tr(strAdd).lower() ])


        id += 1
        myindex += 1

