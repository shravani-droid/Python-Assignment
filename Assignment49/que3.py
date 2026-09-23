import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

data = [[25,20000],
        [30,40000],
        [35,40000]]

scalar = StandardScaler()

scalar.fit(data) # learns how to calculate mean and std

scaled_data = scalar.transform(data) # it applys the scaling

scaled_data = scalar.fit_transform(data) # performs scaling and learning togeather

print(scaled_data)