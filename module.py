import time

def col_symbol(text):
    """Counting symbols"""

    fso = {}

    for symbol in text:
        fso[symbol] = fso.get(symbol, 0) + 1
    
    for key in sorted(fso):
        print(f'{key} : {fso[key]}')
    time.sleep(2)

def write_to_file(data):
    """Write in file"""
    with open("./text.txt","wb") as f:
        f.write(data)
        
def read_from_file(filename="./text.txt"):
    """Reading a file"""
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data
