# Pickle Module
# --- kunai pai file lai pickle banaunu ko karan tyo file user le python IDE bahira bata open garna
#          nasakos bhanera ho... open/read nai garnu paryo bhane ni python bhitra batai garnu paraxa

import pickle

# Pickling a python object-------
# cars = ["BMW", "Lamborghini", "Audi", "Volkswagen"]
# file = "mycar.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()

# Depickling a python object
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)
