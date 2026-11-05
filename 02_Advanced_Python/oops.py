
class laptop:                                  #class
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")     #atributes

l1 = laptop("16gb", "512gb")                   #classes
l2 = laptop("8gb", "256gb")

l1.get_info()





























