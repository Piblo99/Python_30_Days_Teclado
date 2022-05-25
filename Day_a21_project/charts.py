import matplotlib.pyplot as plt

def create_chart(x, y):
    plt.scatter(x, y)
    plt.savefig("graph.png")