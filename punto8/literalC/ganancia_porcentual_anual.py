import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys
sys.path.append('../')

from literalB.ganancia_porcentual_semanal import meanAndStd, plot_histograma_rangoDeGanancia
# Cargamos los datos
def load_data():
    data = pd.read_excel("../data/SandPConstantDollars.xlsx", header=None)
    ## introducir nombre de columna
    data.columns = ['dia', 'index']
    return data

# Calculamos la ganancia porcentual anual
def calculate_annual_percentage_gain(data):
    nparray = data.to_numpy()

    sp = nparray[0:,1]
    days = nparray[0:,0]
    
              
    #calcular la ganancia porcentual semanal
    ganancia = 100*(sp[:-252] - sp[252:]) / sp[252:]
    rangoDeGananaciaAnual = np.array([sp[:-252], sp[252:],ganancia]).T

    return rangoDeGananaciaAnual





gananciaPorcentualSemanal = calculate_annual_percentage_gain(load_data())
mean, std = meanAndStd(gananciaPorcentualSemanal)
plot_histograma_rangoDeGanancia(
    gananciaPorcentualSemanal, mean, std,
    "ganancia_porcentual_anual", 
    "Histograma de ganancia porcentual anual",
    "Ganancia porcentual anual",
    200
    )

    


