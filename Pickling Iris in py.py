# Pickling Iris

import pickle
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
response_text = response.text
data = response_text.splitlines()
read = [i for i in data]

# Pickling the python object
f = open("irisData.pkl", "wb")
pickle.dump(read, f)
f.close()

#Reading pickled file
f = open("irisData.pkl", "rb")
data = pickle.load(f)
print(data)
f.close()



