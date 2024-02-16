# Listing 3-3. # Listing 3-3. neffective hashtable implementation

import hashlib

class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v

class Hashtable:
    def __init__(self, M=10):
        self.table = [None] * M
        self.M = M
        self.N = 0

    def get(self, k):
        hc = hash(k) % self.M           
        while self.table[hc]:
            if self.table[hc].key == k:   
                return self.table[hc].value
            hc = (hc + 1) % self.M        
        return None
  
    def put(self, k, v):
        hc = hash(k) % self.M           
        while self.table[hc]:
            if self.table[hc].key == k:   
                self.table[hc].value = v
                return
            hc = (hc + 1) % self.M        
        if self.N >= self.M - 1:        
            raise RuntimeError ('Table is Full.')
        self.table[hc] = Entry(k, v)    
        self.N += 1
