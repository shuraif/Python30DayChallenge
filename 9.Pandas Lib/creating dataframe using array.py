import pandas as pd
import numpy as np


#creating dataframe using ARRAY
print("-----------------CREATING DATAFRAME FROM ARRAY------------------------")
seq_arr = np.arange(0, 100, 7)
df = pd.DataFrame(seq_arr)
print(df)
