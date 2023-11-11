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

if __name__ == "__main__":
    plot1(40,10000)
    plot2(5,5)