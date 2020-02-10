# # Loading test data
# model_name = temp_model_name
# model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
# test_data_t7_temp = test_data_t7.copy()[list(model_data.columns)]
#
# # Loading model files
# pkl_file = open('exported_model_files/metadata/'+model_name+'_cat', 'rb')
# index_dict = pickle.load(pkl_file)
# new_vector = np.zeros(len(index_dict))
#
# pkl_file = open('exported_model_files/models/'+model_name+'.pkl', 'rb')
# model = pickle.load(pkl_file)
#
# # Preparing Loading data
# test_array = np.array(test_data_t7_temp.drop(axis=1,columns=["program"]))
# test_actual = np.array(test_data_t7_temp["program"])
#
# def get_mclass_accuracy(temp_model_name,model,test_array,test_actual):
#     test_pred = []
#     for i in range(len(test_array)):
#         test_pred.append(model.predict([test_array[i]]))
#     accuracy = metrics.accuracy_score(test_pred,test_actual)
#     return accuracy
#
# def get_mclass_t3(temp_model_name,model,test_array,test_actual):
#     t3_scores = []
#     for i in range(len(test_array)):
#         prediction = model.predict_proba([test_array[i]])
#         probs = sort_probability_dict(retrieve_prediction_labels(model,prediction))[2][:3]
#         n_probs = []
#         for prob in probs:
#             n_probs.append(INDEX_PROGRAM[prob])
#         try:
#             t3 = (1/n_probs.index(test_actual[i]))
#         except:
#             t3 = 0
#         t3_scores.append(t3)
#
#     return mean(t3_scores)
#
# def get_mclass_rr(temp_model_name,model,test_array,test_actual):
#     rr_scores = []
#     for i in range(len(test_array)):
#         prediction = model.predict_proba([test_array[i]])
#         probs = sort_probability_dict(retrieve_prediction_labels(model,prediction))[2]
#         n_probs = []
#         for prob in probs:
#             n_probs.append(INDEX_PROGRAM[prob])
#         try:
#             rr = (1/n_probs.index(test_actual[i]))
#         except:
#             rr = 0
#         rr_scores.append(rr)
#     return mean(rr_scores)

model_name = temp_model_name

model_data = pd.read_csv('exported_model_files/dataframes/'+model_name+'.csv',dtype=str)
test_data_t7_temp = test_data_t7.copy()[list(model_data.columns)]

# Getting average accuracy score
test_array = np.array(test_data_t7_temp.drop(axis=1,columns=["program"]))
test_actual = np.array(test_data_t7_temp["program"])



def get_bclass_accuracy(test_array,model_name,test_actual):
    test_pred = []
    for i in range(len(test_array)):
        predicted = INDEX_PROGRAM[sort_probability_dict(binary_predict_proba(test_array[i],model_name))[2][0]]
        test_pred.append(predicted)

    accuracy = metrics.accuracy_score(test_pred,test_actual)

    return accuracy

def get_bclass_t3(test_array,model_name,test_actual):
    t3_scores = []
    for i in range(len(test_array)):
            probs = sort_probability_dict(binary_predict_proba(test_array[i],model_name))[2][:3]
            n_probs = []
            for prob in probs:
                n_probs.append(INDEX_PROGRAM[prob])
            try:
                t3 = (1/n_probs.index(test_actual[i]))
            except:
                t3 = 0
            t3_scores.append(t3)

    return mean(t3_scores)

def get_bclass_rr(test_array,model_name,test_actual):
    rr_scores = []

    for i in range(len(test_array)):
            probs = sort_probability_dict(binary_predict_proba(test_array[i],model_name))[2]
            n_probs = []
            for prob in probs:
                n_probs.append(INDEX_PROGRAM[prob])
            try:
                rr = (1/n_probs.index(test_actual[i]))
            except:
                rr = 0
            rr_scores.append(rr)

    return mean(rr_scores)
