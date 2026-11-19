import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(2026)
x = rng.uniform(-1, 1, 1000)
y = x**2
print("Sample␣correlation:", np.corrcoef(x, y)[0, 1])
plt.scatter(x, y, s=12)
plt.xlabel("X")
plt.ylabel("Y␣=␣X␣squared")
plt.title("Strong␣nonlinear␣relationship␣with␣near-zero␣correlation")
plt.tight_layout()
plt.savefig("nonlinear_zero_correlation.png", dpi=300)