import pandas as pd

def read_file(file):
    df = pd.read_csv(file)
    return df

df = read_file('exam_scores.csv')
print(df.head())
