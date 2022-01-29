
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
        

