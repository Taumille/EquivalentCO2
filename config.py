import numpy as np
import os

print("API_KEY ?")
API_KEY = input()
print("API_SECRET ?")
API_SECRET = input()
print("BEARER_TOKEN ?")
BEARER_TOKEN = input()
print("ACCESS_TOKEN ?")
ACCESS_TOKEN = input()
print("ACCESS_SECRET ?")
ACCESS_SECRET = input()

liste_token=np.array([API_KEY,API_SECRET,BEARER_TOKEN,ACCESS_TOKEN,ACCESS_SECRET])

try:
    os.mkdir("private")
except:
    print("Folder already exist")
np.save("private/tokens.npy",liste_token)