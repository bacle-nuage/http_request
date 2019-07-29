# coding: UTF-8

def readlines(path):
    with open(path, 'r') as f:
        reader = csv.readlines(f)
    return reader

def write(data, path):
    with open(path, mode='w') as f:
        f.write(data)

def add(data, path):
    with open(path, mode='a') as f:
        f.write(data)