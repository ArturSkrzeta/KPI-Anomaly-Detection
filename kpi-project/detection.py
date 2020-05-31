import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def detect_outliers(data):

    outliers=[]

    threshold=3
    mean = np.mean(data)
    std = np.std(data)

    for nr,item in enumerate(networkdays):
        z_score= (item - mean)/std
        if np.abs(z_score) > threshold:
            outliers.append((nr,item))
    return outliers

def print_outliers(outliers):
    for outlier in outliers:
        print(prs[outlier[0]])

def plot(y,x):
    plt.style.use('seaborn-dark-palette')
    fig = plt.figure()
    plt.scatter(nr, networkdays)
    fig.suptitle('PR processing duration(days)')
    fig.savefig('images/plot.png')
    plt.xlabel('Pr count')
    plt.ylabel('Days')
    plt.show()

df = pd.read_csv('data.csv')
nr = df['NR'].tolist()
prs = df['Pr'].tolist()
networkdays = df['Diff'].tolist()

outliers = detect_outliers(networkdays)
print_outliers(outliers)
plot(nr, networkdays)
