import os

DATA_DIR = os.path.dirname(__file__)

def get_csv_path(filename):
    return os.path.join(DATA_DIR, filename)