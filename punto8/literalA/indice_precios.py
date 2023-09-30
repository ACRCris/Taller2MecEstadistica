import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos los datos
def load_data():
    data = pd.read_excel("../data/SandPConstantDollars.xlsx")
    ## introducir nombre de columna
    data.columns = ['year', 'index']
    return data

# Graficamos los datos
def plot_data(data, fig_name="indice_precios.png"):
    fig,ax = plt.subplots(figsize=(10, 5))

    ## Grafico basico
    nparray = data.to_numpy()
    x = nparray[:,0]
    y = nparray[:,1]
    ax.plot(x, y, color='tab:blue')
    ax.set_title('Indice de precios al consumidor')
    ax.set_xlabel('Año')
    ax.set_ylabel('Indice de precios')
    ax.grid(True)

    ## Min y max
    min = np.min(y)
    max = np.max(y)

    print(f"Min: {min}")

    ## get pos min
    posMin = np.where(y == min)[0][0]
    ## get pos max
    posMax = np.where(y == max)[0][0]

    ## get pos x 6902
    posxInarray = np.where(x == 6.902e+03)[0][0]
    ## get min between 6902 and 6905
    minInRange = np.min(y[posxInarray:posxInarray+10])
    ## get pos min
    posMinInRange = np.where(y == minInRange)[0][0]    
    ## Linea vertical divida en dos en dia 6903 (2001)
    ax.vlines(x[posMinInRange], min-10, y[posMinInRange], color='tab:red', linestyle='--')
    ## Linea verticual desde y[posMin] hasta 
    ax.vlines(x[posxInarray],y[posxInarray],max, color='tab:red', linestyle='--')


    plt.show()

    fig.savefig(f'../data/literalA/{fig_name}.png')




dataIndices = load_data()
plot_data(dataIndices)

## Grafica entre 6800 y 7000
dataIndices = dataIndices[(dataIndices['year'] >= 6800) & (dataIndices['year'] <= 7000)]
plot_data(dataIndices, "indice_precios_6800_7000.png")
