
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Load automobile dataset
df = pd.read_csv(r"D:\HSL5013\auto.csv")

# Convert MPG into gallons per 100 miles
df["gpm"] = 100 / df["mpg"]

# Standardize the GPM variable
z = (df["gpm"] - df["gpm"].mean()) / df["gpm"].std(ddof=1)

# Remove missing values
z = z.dropna()

# Normal Q-Q plot
stats.probplot(z, dist="norm", plot=plt)

plt.title("Normal Q-Q Plot of Standardized Gallons per 100 Miles")
plt.xlabel("Theoretical Normal Quantiles")
plt.ylabel("Ordered Sample Quantiles")

plt.tight_layout()
plt.savefig("gpm_normal_qq.png", dpi=300)
plt.show()
