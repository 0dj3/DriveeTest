import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import random

# Координаты
class Coordinate():
    def __init__(self, x: float, y:float):
        self.x = x
        self.y = y

    def randCord(a, b):
        x = round(random.uniform(a, b), 3)
        y = round(random.uniform(a, b), 3)
        return (x, y)

    def getCord(self):
        return (self.x, self.y)
    
# Заказ
class Order():
    def __init__(self, cordA:Coordinate, cordB:Coordinate, cost:float, status:str):
        self.cordA = cordA
        self.cordB = cordB
        self.cost = cost
        self.status = 'Waiting'

    def getOrderInfo(self):
        return(self.cordA.getCord(), self.cordB.getCord(), self.cost)

    def setOrderStatus(self, status):
        self.status = status

def checkOrders(a:Order):
      for i in range(len(a)):
        if a[i].status == 'Waiting':
          return True
      return False

# Кура
class Courier():
    def __init__(self, cord:Coordinate, status:bool):
        self.cord = cord
        self.order = None
        self.status = status
        self.salary = 0

    def setCourierOrder(self,order: Order):
        self.cord = order.cordA
        self.order = order
        self.order.setOrderStatus('In Progress')
        self.status = True

    def delieveOrder(self):
        self.cord = self.order.cordB
        self.salary += self.order.cost
        self.order.setOrderStatus('Delivered')
        self.order = None
        self.status = False
        
    def getCourierOrder(self):
        return (self.order.getOrderInfo())

    def getCourierCord(self):
        return (self.cord.getCord())

def checkCourier(a:Courier):
    for i in range(len(a)):
        if a[i].status == False:
             return True
    return False

def randomOrders(count):
    orderArr = []
    for i in range(count):
        cordA = Coordinate.randCord(0, 10)
        cordB = Coordinate.randCord(0, 10)
        cost = round(random.uniform(1, 10000), 2)
        orderArr.append(Order(Coordinate(cordA[0],cordA[1]), Coordinate(cordB[0],cordB[1]), cost, False))
    return orderArr

def randomCourier(count):
    courierArr = []
    for i in range(count):
        cord = Coordinate.randCord(0, 10)
        courierArr.append(Courier(Coordinate(cord[0], cord[1]), False))
    return courierArr

def distancy(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closestOrder(a:Order, b:Courier):
    min_distance = float('inf')
    closest = None
    for i in range(len(a)):
        dist = distancy(a[i].cordA.getCord(), b.cord.getCord())
        if dist < min_distance and a[i].status == 'Waiting':
            min_distance = dist
            closest = i
    return closest

def get_cmap(n, name='hsv'):
    return plt.cm.get_cmap(name, n)

def screen(a, b):
    fig, ax = plt.subplots(1)
    cmap = get_cmap(len(a))
    for i in range(len(a)):
        if a[i].status != 'Delivered':
            ax.scatter(a[i].cordA.x, a[i].cordA.y, color=cmap(i))
            ax.scatter(a[i].cordB.x, a[i].cordB.y, color=cmap(i), marker='*')
            ax.plot([a[i].cordA.x, a[i].cordB.x],[a[i].cordA.y, a[i].cordB.y],color=cmap(i))
            ax.annotate(str(i), (a[i].cordB.x, a[i].cordB.y))
    for i in range(len(b)): 
        ax.scatter(b[i].cord.x, b[i].cord.y, color='black', marker=8)
        ax.annotate(str(i), (b[i].cord.x, b[i].cord.y))
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])
    ax.grid()

def deliveProcess():
    while checkOrders(orders):
        while checkCourier(couriers):
            for i in couriers:
                close = closestOrder(orders, i)
                i.setCourierOrder(orders[close])
            screen(orders, couriers)
        for i in couriers:
            i.delieveOrder()
        screen(orders, couriers)

orders = randomOrders(6)
couriers = randomCourier(1)
screen(orders, couriers)
deliveProcess()
      
