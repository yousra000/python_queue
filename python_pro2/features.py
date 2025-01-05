import json

def read_data(file_param):
    try:
        file = open(file_param, "r")
    except FileNotFoundError:
        print(f"File '{file_param}' not found. Creating a new file.")
        return [] 
    except Exception as e:
        print(f"Error: {e}")
        return []
    else:
        try:
            data = json.load(file)
        except Exception as e:
            print(f"Error loading JSON data: {e}")
            data = []
        file.close()
        return data

def write_data(file_name, data: list):
    try:
        file = open(file_name, "w")
    except Exception as e:
        print(f"Error opening file: {e}")
        return False
    else:
        json.dump(data, file, indent=2)
        file.close()
        return True
    
class QueueOutOfRangeException(Exception):
    pass

class Queue():
    def __init__(self):
        self.arr=[]
    
    def insert(self,ele):
        self.arr.append(ele)

    def is_empty(self):
        return len(self.arr) == 0

    def pop(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            self.arr.pop()
            return None
    def print_queue(self):
        print(self.arr)

class Enhanced_queue(Queue):

    Queues ={}
    
    def __init__(self,name,Msize):
        super().__init__()
        self.name=name
        self.Msize = Msize
        Enhanced_queue.Queues[name] = self
        
    def insert(self, value):
        if len(self.arr) >= self.Msize:
            raise QueueOutOfRangeException(f"the size will be more than the size of the queue")
        else:
            super().insert(value)
    
    @classmethod        
    def save(cls,file):
        data =""
        for  n,q in cls.Queues.items():
            data= ",".join(map(str,q.arr))
            data += f"{n}:{data}\n"
        write_data(file,data)


    @classmethod
    def load(cls, file):
        file_data = read_data(file)  
        print(f"Loaded:\n{file_data}") 

