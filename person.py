class Person:
    def __init__(self, fname, lname, address):
        self._fname = fname
        self._lname = lname
        self._address = address
    
    def update_first_name(self, fname):
        self._fname = fname
    
    def update_last_name(self, lname):
        self._lname = lname
                
    def get_first_name(self):
        return self._fname
    
    def get_last_name(self):
        return self._lname
        
    def update_address(self, addr):
        self._address = addr
    
    def get_address(self):
        return self._address
    
    def print_details(self):
        print(f"Name: {self._fname} {self._lname}")
        print("Address: ", " ".join(self._address))
