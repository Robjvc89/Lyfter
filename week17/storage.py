# storage.py

import json
import os
from models import Transaction

DATA_FILE = 'finances.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {"categories": [], "transactions": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_transactions(data):
    return [Transaction.from_dict(t) for t in data['transactions']]
