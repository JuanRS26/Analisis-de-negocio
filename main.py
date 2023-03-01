import yfinance as yf
import pandas as pd


def optDF(df):
    keysDF = ['Open', 'High', 'Low', 'Close']

    df = df.loc['1990-01-01':]
    df.reset_index(inplace = True)
    df[keysDF] = round(df[keysDF], 2)

    return df

ALK = yf.Ticker('ALK')
ALL = yf.Ticker('ALL')
DAL = yf.Ticker('DAL')
LUV = yf.Ticker('LUV')

alkDF = ALK.history(period = 'max')
allDF = ALL.history(period = 'max')
dalDF = DAL.history(period = 'max')
luvDF = LUV.history(period = 'max')

alkDF = optDF(alkDF)
allDF = optDF(allDF)
dalDF = optDF(dalDF)
luvDF = optDF(luvDF)

alkDF.to_csv('Datasets/ALK.csv', index = False, sep = ';')
allDF.to_csv('Datasets/ALL.csv', index = False, sep = ';')
dalDF.to_csv('Datasets/DAL.csv', index = False, sep = ';')
luvDF.to_csv('Datasets/LUV.csv', index = False, sep = ';')