class portfolio:
    def __init__(self,username,password):
        self.owner = username
        self.password = password
        self.balance = 0
        self.stocks = {}  
