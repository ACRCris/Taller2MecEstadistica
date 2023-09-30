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

    print(len(rangoDeGananaciaSemanal))
    return rangoDeGananaciaSemanal

# Mean and std of weekly percentage gain
def meanAndStd(data):
    y = data[:,2]
    return np.mean(y), np.std(y)

def meanAndStdFromHist(N, bins):
    mids = 0.5*(bins[1:] + bins[:-1])
    mean = np.average(mids, weights=N)
    variance = np.average((mids - mean)**2, weights=N)
    std = np.sqrt(variance)
    return mean, std


#Separa en dos arreglos de ganancia positiva y negativa
def separarGananciaPositivaNegativa(data):
    ganancia = data[:,2]
    gananciaPositiva = ganancia[ganancia > 0]
    gananciaNegativa = ganancia[ganancia < 0]
    return gananciaPositiva, gananciaNegativa

# Graficamos histograma de ganancia porcentual semanal

def plot_histograma_rangoDeGanancia(rangoDeGananaciaSemanal, 
    mean, std, fig_name="ganancia_porcentual_semanal.png", 
    title="Histograma de ganancia porcentual semanal",
    xLabel="Ganancia porcentual semanal",
    nBins=500):
    fig,ax = plt.subplots(figsize=(10, 5))

    datosGananciaPositiva, datosGananciaNegativa = separarGananciaPositivaNegativa(rangoDeGananaciaSemanal)


    ## Plot norm 

    ax.grid(True)
    #ax.hist([datosGananciaPositiva, datosGananciaNegativa], bins=150, color=['tab:blue', 'tab:red'], label=['Ganancia positiva', 'Ganancia negativa'], density=True)
    N, bins,patches = ax.hist(rangoDeGananaciaSemanal[:,2], bins=nBins, color='tab:blue', density=True)
    ax.set_title(title)
    ax.set_xlabel(xLabel)
    ax.set_ylabel('Frecuencia')


    #set percent of week with positive gain
    percent = len(datosGananciaPositiva) / len(rangoDeGananaciaSemanal)
    ax.text(0.05, 0.1, f"Porcentaje +: %1.2f" % percent + "%", transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    ## Plot gaussian distribution with mean and std
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    ax.plot(x, stats.norm.pdf(x, mean, std), color='tab:orange', label='Distribucion normal')

    ## Plot mean and std from hist

    meanHist, stdHist = meanAndStdFromHist(N, bins)
    x = np.linspace(meanHist - 3*stdHist, meanHist + 3*stdHist, 100)
    ax.plot(x, stats.norm.pdf(x, meanHist, stdHist), color='tab:purple', label='Distribucion normal (hist)')


    ## paint patches with color depending on the sign of the gain with legend
    addLabelToPositive = True
    addLabelToNegative = True
    for i in range(len(patches)):
        if patches[i].get_x() < 0:#add legend to only one patch
            if addLabelToNegative:
                ax.plot([],[], color='tab:blue', label='Ganancia negativa')
                addLabelToNegative = False
            
            patches[i].set_facecolor('tab:blue')
            patches[i].set_edgecolor('tab:blue')
            patches[i].set_alpha(0.5)
        else:
            if addLabelToPositive:#add legend to only one patch
                ax.plot([],[], color='tab:red', label='Ganancia positiva')
                addLabelToPositive = False
            patches[i].set_facecolor('tab:red')
            patches[i].set_edgecolor('tab:red')
            patches[i].set_alpha(0.5)

    ax.legend(loc='upper left')

    plt.show()
    fig.savefig(f'../data/literalB/{fig_name}.png')







gananciaPorcentualSemanal = calculate_weekly_percentage_gain(load_data())
mean, std = meanAndStd(gananciaPorcentualSemanal)
plot_histograma_rangoDeGanancia(gananciaPorcentualSemanal, mean, std)

    


data = load_data()
calculate_weekly_percentage_gain(data)