import pandas as pd

def preprocess_stroke(path):
    df = pd.read_csv(path)

    # Drop unnecessary columns
    df = df.drop(columns=['id', 'ever_married'], errors='ignore')

    # Handle missing values
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df


def preprocess_anemia(path):
    df = pd.read_csv(path)

    df = df.drop(columns=['Patient_ID'], errors='ignore')

    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
