# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import pickle
# from sklearn import metrics
# from sklearn.model_selection import cross_val_score,train_test_split,LeaveOneOut
# # import apyori as ap
# from data_load import *
# from dictionaries import *
#
#
# support = 0.1 # number of records containing a particular response divided by total number of responses
# confidence = 0.5 #  likelihood that an value B occurs when value A also occurs
# lift = support/confidence # the increase in the ratio of sale of B when A occurs.
# length = 2 # Number of products in rule
#
# data = get_clean_data('quiz_data.csv',True)
#
# records = []
# for i in range(0, len(data)):
#     records.append([str(data.values[i,j]) for j in range(0, len(data.columns))])
#
# association_rules = apriori(records, min_support=support, min_confidence=confidence, min_lift=lift, min_length=length)
# association_results = list(association_rules)
#
# print("Suppport: "+str(support))
# print("Confidence: "+str(confidence))
# print("Lift: "+str(lift))
# print("Length: "+str(length))
#
# print(association_results)
