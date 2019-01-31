import numpy as np
import pandas as pd
import random
from numpy.core.umath_tests import inner1d

df = pd.read_csv("bank_et1.csv",index_col=['Unnamed: 0'])
#print ("|".join(df.columns.values))

@profile
def h(x,w):
    #Perceptron model: the sign of the dot product of weights and input vector determines the class allocation
    bias = np.array([1])
    return np.sign(w.T.dot(np.concatenate((bias,x))))

@profile
def calc_error(training_in, training_out, weights):
    # Calculate the classification error as the fraction of training samples that are misclassified
    errors=0
    for x,y in zip(training_in, training_out):
        if (h(x,weights)!=y):
            errors+=1;
    return errors

@profile
def calc_error_np(training_in, training_out, weights):
    training_in = np.column_stack((np.ones(training_in.shape[0]),training_in))
    out = np.sign(inner1d(weights.T,training_in))
    return ((out != training_out).sum())

df_rnd = df.sample(frac=1)
X_in = df_rnd[['ratio_bal_ln', 'ratio_ln_inc']].values
y_in = df_rnd['subscribed'].map(dict(yes=1, no=-1)).values
w = np.array([random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)])

print (calc_error(X_in,y_in,w))
print (calc_error_np(X_in,y_in,w))
