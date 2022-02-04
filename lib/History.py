
class History:
    
    def __init__(self):
        self.position = 0
        self.list = []
        self.data_type = None

    def append(self, data):
        if len(self.list) != 0:
            if type(data) != self.data_type:
                raise KeyError(f"Datatype Mistmatch of {type(data)}")
            else:
                self.list.append(data)
        else:
            self.list.append(data)
            self.data_type = type(data)
        
    def last(self):
        return self.list[-1]
    def first(self):
        return self.list[0]
        
    def print_last(self):
        print(self.list[-1])
    def print_first(self):
        print(self.list[0])
    def print_(self, index):
        try:
            print(self.list[index])
        except IndexError:
            print("INDEX ERROR")
    def print_all(self):
        for msg in self.list:
            print(msg)