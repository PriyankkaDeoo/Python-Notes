class BalanceException (Exception):
    #pass
    def __init__(self, arg):
        self.msg = arg
        
def checkbalance():
    money = 10000
    withdraw = 9000
    try:
        balance = money - withdraw
        if(balance<=2000):
            raise BalanceException('Insufficient Balance')
        print(balance)
    except BalanceException as be:
        print(be)
        
checkbalance() 
        
    