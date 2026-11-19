import pandas as pd
data = pd.read_csv("poisson.csv")
x = data.select_dtypes(include="number").iloc[:, 0].dropna()
lambda_mom = x.mean()
lambda_mle = x.mean()
print("Sample␣size:", len(x))
print("MOM␣estimate:", lambda_mom)
print("MLE␣estimate:", lambda_mle)
print("Difference:", abs(lambda_mom - lambda_mle))