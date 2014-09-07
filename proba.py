import os
d = os.path.abspath(os.path.join(os.path.dirname(__file__), 'patterns'))
print(d)
os.listdir(d)