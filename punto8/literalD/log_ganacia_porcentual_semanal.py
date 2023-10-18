import sys
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

sys.path.append('../')

from literalB.ganancia_porcentual_semanal import meanAndStd,meanAndStdFromHist, calculate_weekly_percentage_gain, load_data,separarGananciaPositivaNegativa, plot_histograma_rangoDeGanancia, filterPercentGainByRange


def plot_histograma_rangoDeGanancia_log_no_log(rangoDeGananaciaSemanal, 
    mean, std, fig_name="ganancia_porcentual_semanal.png", 
    title="Histograma de ganancia porcentual semanal",
    xLabel="Ganancia porcentual semanal",
    directory="../data/literalD/",
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
    ax.text(0.05, 0.1, f"Porcentaje {percent:.2f}" , transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    ## Plot gaussian distribution with mean and std, wit latex label
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    ax.plot(x, stats.norm.pdf(x, mean, std), color='tab:orange', label=r'Distribucion normal($\mu$={mean:.2f}, $\sigma$={std:.2f})'.format(mean=mean, std=std));

    ## Plot mean and std from hist

    meanHist, stdHist = meanAndStdFromHist(N, bins)
    x = np.linspace(meanHist - 3*stdHist, meanHist + 3*stdHist, 100)
    #ax.plot(x, stats.norm.pdf(x, meanHist, stdHist), color='tab:purple', label=r'Distribucion normal($\mu$={mean:.2f}, $\sigma$={std:.2f})'.format(mean=meanHist, std=stdHist));


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
    fig.savefig(f'../data/literalD/{fig_name}.pdf')

def plot_log_histograma_rangoDeGanancia(rangoDeGananaciaSemanal, 
    mean, std, fig_name="ganancia_porcentual_semanal.png", 
    title="Histograma de ganancia porcentual semanal",
    xLabel="Ganancia porcentual semanal",
    directory="../data/literalD/",
    nBins=500):
    fig,ax = plt.subplots(figsize=(10, 5))

    datosGananciaPositiva, datosGananciaNegativa = separarGananciaPositivaNegativa(rangoDeGananaciaSemanal)


    ## Plot norm 

    ax.grid(True)
    #ax.hist([datosGananciaPositiva, datosGananciaNegativa], bins=150, color=['tab:blue', 'tab:red'], label=['Ganancia positiva', 'Ganancia negativa'], density=True)
    N, bins,patches = ax.hist(rangoDeGananaciaSemanal[:,2], bins=nBins, color='tab:blue', density=True)
    ax.semilogy()
    ax.set_title(title)
    ax.set_xlabel(xLabel)
    ax.set_ylabel('Frecuencia')


    #set percent of week with positive gain
    percent = len(datosGananciaPositiva) / len(rangoDeGananaciaSemanal)
    ax.text(0.05, 0.1, f"Porcentaje {percent:.2f}" , transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

    ## Plot gaussian distribution with mean and std, wit latex label
    x = np.linspace(mean - 5*std, mean + 5*std, 100)
    ax.plot(x, stats.norm.pdf(x, mean, std), color='tab:orange', label=r'Distribucion normal($\mu$={mean:.2f}, $\sigma$={std:.2f})'.format(mean=mean, std=std));

    ## Plot mean and std from hist

    meanHist, stdHist = meanAndStdFromHist(N, bins)
    x = np.linspace(meanHist - 3*stdHist, meanHist + 3*stdHist, 100)
    #ax.plot(x, stats.norm.pdf(x, meanHist, stdHist), color='tab:purple', label=r'Distribucion normal($\mu$={mean:.2f}, $\sigma$={std:.2f})'.format(mean=meanHist, std=stdHist));


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
    fig.savefig(f'../data/literalD/{fig_name}.pdf')




data = load_data()
gananciaPorcentualSemanal = calculate_weekly_percentage_gain(load_data())
mean, std = meanAndStd(gananciaPorcentualSemanal)
mean, std = meanAndStd(gananciaPorcentualSemanal - mean)
plot_histograma_rangoDeGanancia(
    gananciaPorcentualSemanal - mean,
    mean, 
    std,fig_name="ganancia_porcentual_semanal-minus-mean", 
    directory="../data/literalD/",
    nBins=300,
    title="Histograma de ganancia porcentual semanal menos la media")


plot_log_histograma_rangoDeGanancia(
    gananciaPorcentualSemanal - mean, 
    mean,
    std,fig_name="log-ganancia_porcentual_semanal-minus-mean", 
    directory= "../data/literalD/",
    nBins=200,
    title="Histograma log de ganancia porcentual semanal menos la media")

gananciaPorcentualSemanal = filterPercentGainByRange(gananciaPorcentualSemanal - mean, 12)


plot_log_histograma_rangoDeGanancia(
    gananciaPorcentualSemanal - mean, 
    mean,
    std,fig_name="log-ganancia_porcentual_semanal-minus-mean2", 
    directory= "../data/literalD/",
    nBins=200,
    title="Histograma log de ganancia porcentual semanal menos la media")
