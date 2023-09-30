import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Cargamos los datos
def load_data():
    data = pd.read_excel("../data/SandPConstantDollars.xlsx", header=None)
    ## introducir nombre de columna
    data.columns = ['dia', 'index']
    return data

# Calculamos la ganancia porcentual semanal
def calculate_weekly_percentage_gain(data):
    nparray = data.to_numpy()

    sp = nparray[0:,1]
    days = nparray[0:,0]
    
              
    #borrar los elementos de days tales que days + 5 no esta en days
    daysD = np.delete(days, np.where(np.isin(days + 5, days) == False))
    #borrar los elementos de sp tales que days + 5 no esta en days
    spD = np.delete(sp, np.where(np.isin(days + 5, days) == False))
    #borrar los elementos de days tales que days - 5 no esta en days
    days5I = np.delete(days, np.where(np.isin(days - 5, days) == False))
    #borrar los elementos de sp tales que days - 5 no esta en days
    sp5I = np.delete(sp, np.where(np.isin(days - 5, days) == False))

    #calcular la ganancia porcentual semanal
    ganancia = 100*(sp5I - spD[0:len(sp5I)]) / spD[0:len(sp5I)] 
    rangoDeGananaciaSemanal = np.array([daysD[:len(days5I)], days5I,ganancia]).T

    for i in rangoDeGananaciaSemanal:
        print(f"dia: {i[0]}, dia+5: {i[1]}, ganancia: {i[2]}")

    print(f"Min: {np.min(ganancia)}")
    print(f"Max: {np.max(ganancia)}")

    return rangoDeGananaciaSemanal

# Mean and std of weekly percentage gain
def meanAndStd(data):
    y = data[:,2]
    return np.mean(y), np.std(y)


# Graficamos histograma de ganancia porcentual semanal

def plot_histograma_rangoDeGananciaSemana(rangoDeGananaciaSemanal, mean, std, fig_name="ganancia_porcentual_semanal.png"):
    fig,ax = plt.subplots(figsize=(10, 5))

    ## Plot norm 

    ax.grid(True)
    ax.hist(rangoDeGananaciaSemanal[:,2], bins=300, color='tab:blue', density=True)
    ax.set_title('Histograma de ganancia porcentual semanal')
    ax.set_xlabel('Ganancia porcentual semanal')
    ax.set_ylabel('Frecuencia')

    ## Plot gaussian distribution with mean and std
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    ax.plot(x, stats.norm.pdf(x, mean, std), color='tab:red')



    plt.show()
    fig.savefig(f'../data/literalB/{fig_name}.png')







gananciaPorcentualSemanal = calculate_weekly_percentage_gain(load_data())
mean, std = meanAndStd(gananciaPorcentualSemanal)
plot_histograma_rangoDeGananciaSemana(gananciaPorcentualSemanal, mean, std)

    


data = load_data()
calculate_weekly_percentage_gain(data)