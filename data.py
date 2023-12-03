import matplotlib.pyplot as plt
import numpy as np

def plot1(points=40, value=10000):
    plt.plot(range(points),np.random.poisson(value,points))
    plt.ylim(value*0.9,value*1.1)
    plt.xlabel("Time")
    plt.ylabel("Number of vehicles")
    plt.title("Vehicles on the road")
    # plt.show()
    plt.savefig("./assets/traffic_graph",dpi=85)
    plt.close()
    return "A"

def plot2(points=5, value=5):
    plt.bar(range(points),np.random.poisson(value,points))
    plt.xlabel("Date")
    plt.ylabel("Number of accidents")
    plt.title("Accidents in last 5 days")
    # plt.show()
    plt.savefig("./assets/accident_graph",dpi=85)
    plt.close()
    return "B"

def plot3():
    x = ["13/11","14/11","15/11","16/11","17/11","18/11","19/11"]
    y = [7,6,8,9,5,16,11]
    plt.bar(x,y)
    plt.xlabel("Date")
    plt.ylabel("Number of accidents")
    plt.title("Accidents in last 7 days")
    # plt.show()
    plt.savefig("./assets/accident_graph",dpi=200)
    plt.close()

    x = ["13/11","14/11","15/11","16/11","17/11","18/11","19/11"]
    y = [146,138,152,186,148,210,203]
    plt.plot(x,y)
    plt.ylim(100,250)
    plt.xlabel("Time")
    plt.ylabel("Number of vehicles")
    plt.title("Vehicles on the road")
    # plt.show()
    plt.savefig("./assets/traffic_graph",dpi=200)
    plt.close()

if __name__ == "__main__":
    # plot1(40,10000)
    # plot2(5,5)
    plot3()