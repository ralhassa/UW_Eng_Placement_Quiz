import pickle

from naive_bayes import naive_bayes

if __name__ == '__main__':
    nb_model = naive_bayes('quiz_data.csv')[0]
    with open('nb_model.pkl', 'wb') as fid:
        pickle.dump(nb_model, fid,2)

    '''
    We need to create our feature vector of exact same dimension as our training set. To convert our user input into dummy variables, we should save a dict of the the dummy variables. Later we can populate our feature vector for prediction using this dict.
    '''
    index_dict = naive_bayes('golf_data.csv')[1]

    with open('cat', 'wb') as fid:
        pickle.dump(index_dict, fid,2)


'''
Links:
https://www.datacamp.com/community/tutorials/naive-bayes-scikit-learn

https://xcitech.github.io/tutorials/heroku_tutorial/

Options:

option 1
- create a model
- save data in repo
- model is built every time its called
- resposne made every time

this is dumb, do option 2 + option 2 is proven

option 2
- create a model
- make a pickle file
- use pickle file to load model
- website will read fron the pickle file, build the model, and
'''
