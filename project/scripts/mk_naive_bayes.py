from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import csv



# read the data into pandas data frame
df_train = pd.read_csv('../data/mktrain_set5.tsv', sep='\t', header=0)

# tokenizing
# transform the comment column into feature vectors
count_vec = CountVectorizer()
x_train_counts = count_vec.fit_transform(df_train.comment)

# from occurences to frequencies (tf idf)
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

# training a classifier
clf = MultinomialNB().fit(x_train_tfidf, df_train.label)

################################### TRAINING COMPLETE ###################################

df_test = pd.read_csv('../data/mktest5.tsv', sep='\t', header=0)

# transform test data into feature vectors
x_new_counts = count_vec.transform(df_test.comment)
x_new_tfidf = tfidf_transformer.transform(x_new_counts)

predicted = clf.predict(x_new_tfidf)
print(predicted)
# f_out = open('../output/output.txt', 'w')

# f_out.write("label\tcomment\n")
with open('../output/output_mk_nb4.tsv', 'wt') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    tsv_writer.writerow(['Id', 'Category'])

    # writing results to a file
    id=0
    for item in predicted:
        tsv_writer.writerow([id, item])
        id += 1

# for doc, category in zip(df_test.comment, predicted):
#     print('%r => %s' % (doc, category))