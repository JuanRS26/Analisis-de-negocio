import yfinance as yf
import pandas as pd

# Definimos una funcion para hacer las respectivas modificaciones y tener un set de deatos mas limpio 
def optDF(df):
    keysDF = ['Open', 'High', 'Low', 'Close']

    df = df.loc['1990-01-01':]          # Se selecciona el rango de fechas a extraer
    df.reset_index(inplace = True)      # Se cambia el indice del dataframe
    df[keysDF] = round(df[keysDF], 2)   # Se redondea los valores

    return df

# Instanciamos las empresas a las cuales queremos obtener el set de datos
ALK = yf.Ticker('ALK')
ALL = yf.Ticker('ALL')
DAL = yf.Ticker('DAL')
LUV = yf.Ticker('LUV')

# Solicitamos los datos de las empresas
alkDF = ALK.history(period = 'max')
allDF = ALL.history(period = 'max')
dalDF = DAL.history(period = 'max')
luvDF = LUV.history(period = 'max')

# Modificamos el set de datos 
alkDF = optDF(alkDF)
allDF = optDF(allDF)
dalDF = optDF(dalDF)
luvDF = optDF(luvDF)

# Guardamos los datos el archivos 'CSV'
alkDF.to_csv('Datasets/ALK.csv', index = False, sep = ';')
allDF.to_csv('Datasets/ALL.csv', index = False, sep = ';')
dalDF.to_csv('Datasets/DAL.csv', index = False, sep = ';')
luvDF.to_csv('Datasets/LUV.csv', index = False, sep = ';')