import requests
import json
from config import Config as cfg

def pull_pyzel():
    response = requests.get(cfg.unofficial_endpoint_pyzel)
    jdata = json.loads(response.text)
    X = []
    Y = []
    for row in jdata:
        X.append(row['img']['deck'])
        Y.append(row['img']['bottom'])

    X = list(filter(None, X))
    Y = list(filter(None, Y))

    for i in range(len(X)):
        with open("assets/board{}.jpg".format(str(i)), "wb") as f:
            f.write(requests.get(X[i]).content)
    j = len(X)
    for i in range(len(Y)):
        with open("assets/board{}.jpg".format(str(j)), "wb") as f:
            f.write(requests.get(Y[i]).content)
            j+=1

    f.write(requests.get(Y[i]).content)

pull_pyzel()
