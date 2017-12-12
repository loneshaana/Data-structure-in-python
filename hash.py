class HashItem:
    def __init__(self,key,value):
        self.key = key
        self.value = value
class HashTable:
    def __init__(self):
        self.size =256
        self.slots=[None for _ in range(self.size)]
        self.count =0

    def _hash(self,key):
        #assume key is a string value or character value
        mult =1
        hv =0
        for k in key:
            hv += mult * ord(k)
            mult += 1
        return hv % self.size

    # we will insert the item using the put() method and retrive the item
    # using the get() method

    def put(self,key,value):
        # first store the key value in HashItem
        item = HashItem(key,value) # object creation
        # calculate the hash of the key
        h = self._hash(key)
        # now find the empty slot
        # however if this slot is not empty and the key of the
        # slot is not same as our then we have met the collison
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                #raise KeyError('Key already present')
                break
            #else collison occurs generate new h
            h= (h+1) %256
        if self.slots[h] is None:
            self.count +=1
            self.slots[h] =item

    def get(self,key):
        h =self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key == key:
                return self.slots[h].value
            h=(h+1) % 256
        return None

    def __setitem__(self,key,value):
        self.put(key,value)

    def __getitem__(self,key):
        return self.get(key)

ht =HashTable()
ht['good'] ='eggs'  # calls to the __setitem__(self,key,value)
ht['better']='ham'
ht['best']='spam'
ht['ad']='do not'
ht['ga']='collide'
ht['a']='not know'

for key in ("good", "better", "best", "worst", "ad", "ga",'a'):
    v= ht[key]  # calls to __getitem__()
    print '{} :{}'.format(key,v)
print("The number of elements is: {}".format(ht.count))
