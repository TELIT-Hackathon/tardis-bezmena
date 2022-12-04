import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



json_input = open('smolsum.json')

arr = json.load(json_input)

from pprint import pprint

for key in arr["metric"].keys():
    print(key)

values=arr["metric"]["values"]
timestamps=arr["metric"]["timestamps"]

a = np.asarray([ timestamps, values])
pd.DataFrame(a).to_csv("sum.csv")
plt.plot(values,timestamps)