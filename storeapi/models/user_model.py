class User:
    def __init__(self,userId,username,password,role):
        self.userId=userId
        self.username=username
        self.password=password
        self.role=bool(role)
        
admin = User(1, 'admin','pass', True )
attendant = User(2,'attendant','password', False)