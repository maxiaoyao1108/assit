import matplotlib.pyplot as plt


def visualize_data(data):
    plt.plot(data)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Data Visualization')
    plt.show()

    