# Python test script.

import pandas as pd
import numpy as np

# Using pandas to create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)

# Using numpy for numerical operations
array = np.array([1, 2, 3, 4, 5])
squared_array = np.power(array, 2)
print(f"\nSquared array using numpy: {squared_array}")