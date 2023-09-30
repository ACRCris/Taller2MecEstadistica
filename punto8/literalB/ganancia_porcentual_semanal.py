import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Cargamos los datos
def load_data():
    data = pd.read_excel("../data/SandPConstantDollars.xlsx")
    ## introducir nombre de columna
    data.columns = ['dia', 'index']
    return data

# Calculamos la ganancia porcentual semanal
def calculate_weekly_percentage_gain(data):
    nparray = data.to_numpy()
    
    # proceso anterio en una linea
    sp = nparray[0:,1]
    #Calcula la ganancia porcentual semanal para los primeros 3 dias
    sp = sp[:2]
    sp5 = sp[2:5]

    #primeros3dias = 100 * (sp5 - sp) / sp 

    #Calcula la ganancia porcentual semanal para el resto de dias
    y = nparray[0:,1]
    x = nparray[0:,0]
    sp = y[2:]
    t = x[2:]
    ## remover por indice
    indices = np.linspace(0, len(sp)-1, len(sp), dtype=int)

    #borra los datos que no tiene imagen
    mask =  (indices %5 != 0) 
    mask2 =  (indices %4 != 0)
    sp = sp[mask][mask2[:len(sp[mask])]]
    t = t[mask][mask2[:len(t[mask])]]

    # calcula sp5 eliminado los que no tienen pre-imagen
    sp = y[5:]
    t5 = x[5:]
    #for i in t:
    #    print(i) 
    sp5 = sp[mask[:-3]][mask2[:len(sp[mask[:-3]])]]
    t5 = t5[mask[:-3]][mask2[:len(t5[mask[:-3]])]]

    for i in range(len(t)-1):
        print("t",t[i],"sp", sp[i], "t+5",t5[i], "sp+5", sp5[i])
        

data = load_data()
calculate_weekly_percentage_gain(data)