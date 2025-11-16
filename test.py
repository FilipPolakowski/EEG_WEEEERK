import numpy as np
import scipy.signal
import mne
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
import torch

print("=== Imports OK ===")

# Test numpy
a = np.array([1, 2, 3])
print("NumPy OK:", a * 2)

# Test scipy
b = scipy.signal.detrend(a)
print("SciPy OK:", b)

# Test pandas
df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
print("Pandas OK:\n", df)

# Test matplotlib backend (no display required)
plt.plot([0, 1], [0, 1])
plt.title("Test plot")
plt.savefig("test_plot.png")
print("Matplotlib OK: test_plot.png saved")

# Test scikit-learn
model = LogisticRegression()
model.fit([[0], [1]], [0, 1])
print("Scikit-learn OK: model coefficient =", model.coef_)

# Test PyTorch
x = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch OK:", x * 2)

# Test MNE
info = mne.create_info(ch_names=["Cz"], sfreq=1000, ch_types=["eeg"])
print("MNE OK: info created")

print("\n=== All tests passed! ===")
