import os

DATA_FOLDER = "data"

if not os.path.exists(DATA_FOLDER):
    os.mkdir(DATA_FOLDER)
    print("📁 Creating the data folder")