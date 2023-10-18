import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_velocity_histogram(velocities):
    """
    Plots a histogram for a list of velocity values.
    """
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(velocities, bins=25, density=True, color='blue', alpha=0.5)
    ax.set_title('Histograma de velocidades')
    ax.set_xlabel('Velocidad')
    ax.set_ylabel('Frecuencia')
    ax.grid()

    plt.show()

    fig.savefig('../../data/puntoD/histoV.png', dpi=300)


df = pd.read_csv('../../data/puntoD/ValoresV.txt', header=None, names=['Velocity'])
velocities = df['Velocity'].to_numpy()


plot_velocity_histogram(velocities)
