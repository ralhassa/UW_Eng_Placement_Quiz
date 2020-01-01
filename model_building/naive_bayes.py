import numpy as np
from sklearn.naive_bayes import MultinomialNB

from data_load import get_encoded_data

###=========================== NB Full Data Label Encoded Data =================

def naive_bayes(directory):
    # Returns a model built off of naive_bayes

    df = get_encoded_data(directory)[0]

    x_df = df.drop(axis=1,columns=["PLAY"])
    y_df = df["PLAY"]

    X = np.array(x_df) # convert dataframe into np array
    y = np.array(y_df) # convert dataframe into np array

    mnb = MultinomialNB()
    model = mnb.fit(x_df, y_df) # fit the model using training data

    cat = df.drop('PLAY',axis=1)
    index_dict = dict(zip(cat.columns,range(cat.shape[1])))

    return [model,index_dict]


def test_model(model):
    new_vector[0] = outlook[post_dict['OUTLOOK']]
    new_vector[1] = temperature[post_dict['TEMPERATURE']]
    new_vector[2] = humidity[post_dict['HUMIDITY']]
    new_vector[3] = windy[post_dict['WINDY']]

    print("Loading model")
    pkl_file = open('nb_model.pkl', 'rb')
    print(pkl_file)
    nb_model = pickle.load(pkl_file)
    print(nb_model)
    prediction = nb_model.predict(new_vector)
    print(prediction)
