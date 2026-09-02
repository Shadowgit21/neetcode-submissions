class MyHashMap:
    def __init__(self):
        self.data = []
    def put(self,key,value):
        for i, (k,v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key,value)
                return
        
        self.data.append((key,value))
    def get(self, key):
        for k, v in self.data:
            if k == key:
                return v
        return -1
    def remove(self,key):
        for i, (k,v) in enumerate(self.data):
            if k == key:
                self.data.pop(i)
                return

            