import os
for root, dirs, files in os.walk("logs/fit"):
    print(root, files)