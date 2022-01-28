
class History:
    
    def __init__(self, data_type):
        self.position = 0
        self.list = []
        self.data_type = type(data_type)

    def append(self, data):
        if type(data) == self.data_type:
            self.list.append(data)
