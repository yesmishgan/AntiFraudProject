from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
import sys
import time
import os
import requests
import json
import pandas as pd


if __name__ == "__main__":
    test_trans = pd.read_csv('../data/test_transaction.csv')
    test_identity = pd.read_csv('../data/test_identity.csv')
    print("Files succesfully loaded!")
    test_df = test_trans.merge(test_identity, how='left', left_index=True, right_index=True)
    print("Test shape  : "+str(test_df.shape))
    test_df = test_df.fillna(-999)
    for f in test_df.columns:
        if test_df[f].dtype=='object':
            lbl = preprocessing.LabelEncoder()
            lbl.fit(list(test_df[f].values))
            test_df[f] = lbl.transform(list(test_df[f].values))
    test_df.reset_index()
    clf = CatBoostClassifier()
    clf.load_model("CBmodel4.cbm")
    predictions = clf.predict(test_df)

    url = "http://127.0.0.1:8000/fraud_monitor/upload/"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'id': '123',
            'amt': 1000,
            'card1': 1,
            'card2': 1,
            'card6': 'debit',
            'fraud': True
    }
    for i in range(len(predictions)):
        data['fraud'] = bool(predictions[i])
        data['id'] = str(int(test_df.iloc[i].to_list()[0]))
        data['amt'] = int(test_df.iloc[i].to_list()[2])
        data['card1'] = int(test_df.iloc[i].to_list()[4])
        data['card2'] = int(test_df.iloc[i].to_list()[5])
        if test_df.iloc[i].to_list()[9] == 3:
            data['card6'] = 'debit'
        elif test_df.iloc[i].to_list()[9] == 2:
            data['card6'] = 'credit'

        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
        time.sleep(0.1)
