import matplotlib.pyplot as plt
import seaborn as sns

def age_vs_risk(df, target_col, title):
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[target_col], y=df['age'])
    plt.title(title)
    plt.xlabel("Risk (0 = No, 1 = Yes)")
    plt.ylabel("Age")
    plt.show()
