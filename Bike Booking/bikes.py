from collections import defaultdict

class Shop:
    # CONSTANTS

    def __init__(self, name, stock = 0, rate = 5, rental = None, orders = None, discount = 0.3):
        self.name = name
        self.stock = stock
        self.rate = rate
        self.RENTAL = rental if rental else {'H':self.hour_rate, 'D':self.day_rate, 'W':self.week_rate}
        self.orderID = 0
        self.orders = orders if orders else defaultdict(tuple)
        self.discount = 1 - discount

    @property
    def hour_rate(self):
        return self.rate

    @property
    def day_rate(self):
        return self.rate*4

    @property
    def week_rate(self):
        return self.rate*12

    def displaystock(self):
        return f'The shop currently has {self.stock} bikes in stock'

    def rentBike(self, num, time, unit = 'H', receipt = False):
        '''
        Rent <num> bike(s) for <time> amount of time
        H -> Hours, D -> Days, W -> Weeks
        '''
        print(self.RENTAL)

        if num <= 0:
            print('You must rent at least one bike !')
            return None

        if num > self.stock:
            print(f'You have ordered {num} bikes, yet we only have {self.stock} remaining!')
            return None

        # Successfully rented bikes - display message

        cost = self.RENTAL[unit] * time

        print(f'You have rented {num} bikes for {time} {unit}')
        print(f'This will cost {cost} pounds !')
        print(f'Your order ID is {self.orderID} ! Don\'t forget it, it will be necessary!')

        self.orders[self.orderID] = (num, cost)
        self.orderID += 1

        if receipt:
            return f'{self.orderID:05d} : {num} bikes for {time} {unit}'

    def returnBike(self, orderID):
        if not orderID in self.orders.keys():
            print(f'Invalid orderID : {orderID}')
            return None
        
        order = self.orders[orderID]
        price = order[1]
        if order[0] <= 5 and order[0] >= 3:
            price *= self.discount

        self.stock += order[0]
        print(f'You owe {price} pounds for your trip')
        print(f'Thank you for using {self.name}!')
        
            
