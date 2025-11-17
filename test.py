import sys
import os
import numpy as np
import scipy.signal
import mne
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
import torch

print("=== BASIC LIBRARY TESTS ===")

# Test numpy
a = np.array([1, 2, 3])
print("NumPy OK:", a * 2)

# Test scipy
b = scipy.signal.detrend(a)
print("SciPy OK:", b)

# Test pandas
df = pd.DataFrame({"x": [1, 2, 3], "y": [10, 20, 30]})
print("Pandas OK:\n", df)

# Test matplotlib
plt.plot([0, 1], [0, 1])
plt.title("Test plot")
plt.savefig("test_plot.png")
print("Matplotlib OK (saved plot)")

# Test scikit-learn
model = LogisticRegression()
model.fit([[0], [1]], [0, 1])
print("Scikit-learn OK:", model.coef_)

# Test torch
x = torch.tensor([1.0, 2.0, 3.0])
print("PyTorch OK:", x * 2)

# Test MNE
info = mne.create_info(ch_names=["Cz"], sfreq=1000, ch_types=["eeg"])
print("MNE OK:", info)


print("\n=== BENDR TEST ===")

# Show what's inside the cloned repo
print("Directory /opt:", os.listdir("/opt"))
print("Directory /opt/BENDR:", os.listdir("/opt/BENDR"))
print("Directory /opt/BENDR/dn3_ext:", os.listdir("/opt/BENDR/dn3_ext"))

# Add BENDR repo to path
sys.path.append("/opt/BENDR")

try:
    from dn3_ext.bendr.bendr import BENDREncoder
    print("BENDR import OK")
except Exception as e:
    print("BENDR import FAILED:", e)
    raise


# Try creating an encoder
try:
    model = BENDREncoder()
    print("BENDREncoder instantiated OK")
except Exception as e:
    print("Instantiation FAILED:", e)
    raise


# Create dummy EEG input: [batch, channels, samples]
fake_eeg = torch.randn(1, 32, 256)

try:
    output = model(fake_eeg)
    print("BENDR forward pass OK. Output shape:", output.shape)
except Exception as e:
    print("Forward pass FAILED:", e)
    raise

print("\n=== ALL TESTS PASSED INCLUDING BENDR ===")
