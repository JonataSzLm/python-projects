import pickle
import base64

data = input(">>")
deserialized = pickle.loads(base64.b64decode(data))
print(deserialized)

