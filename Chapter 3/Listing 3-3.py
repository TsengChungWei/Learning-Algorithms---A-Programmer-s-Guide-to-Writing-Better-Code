# Listing 3-3. Ineffective hashtable implementation

import hashlib

class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v

class Hashtable:
    def __init__(self, M=10):
        self.table = [None] * M     # 1
        self.M = M

    def get(self, k):            
        hc = hash(k) % self.M       # 2
        return self.table[hc].value if self.table[hc] else None
    
    def put(self, k, v):            # 3
        hc = hash(k) % self.M
        entry = self.table[hc]
        if entry:
            if entry.key == k:
                entry.value = v
            else:                   # 4
                raise RuntimeError('Key Collision: {} and {}'.format(k, entry.key))
        else:
            self.table[hc] = Entry(k, v)


# 1. Allocate a table to hold M Entry objects.
# 2. The get() function locates the entry associated with the hash code for k and
#    returns its value, if present.
# 3. The put() function locates the entry associated with the hash code for k, if
#    present, and overwrites its value; otherwise it stores a new entry.
# 4. A collision occurs when two different keys map to the same bucket identified by
#    its hash code value.

table = Hashtable(1000)
table.put('April', 30)
table.put('May', 31)
table.put('September', 30)

print(table.get('August'))      # Miss: should print None since not present
print(table.get('September'))   # Hit: should print 30
