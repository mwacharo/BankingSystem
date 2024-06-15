from person import Person
class Admin(Person):
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        super().__init__(fname, lname, address)
        self._user_name = user_name
        self._password = password
        self._full_admin_rights = full_rights
    
    def set_username(self, uname):
        self._user_name = uname
        
    def get_username(self):
        return self._user_name
    
    def update_password(self, password):
        self._password = password
    
    def get_password(self):
        return self._password
    
    def set_full_admin_right(self, admin_right):
        self._full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self._full_admin_rights
