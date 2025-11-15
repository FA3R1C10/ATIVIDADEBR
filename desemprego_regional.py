# %% Bibliotecas
import pandas_datareader as pdr
import datetime as dt
# %% Importar dataframes
gdpUS = pdr.DataReader("GDPC1", "fred", "2020-01-01", dt.datetime.today())
gdpBR = pdr.DataReader("NGDPRSAXDCBRQ", "fred", "2020-01-01", dt.datetime.today())
gdpJP = pdr.DataReader("JPNRGDPEXP", "fred", "2020-01-01", dt.datetime.today())
gdpCH = pdr.DataReader("MKTGDPCNA646NWDB ", "fred", "2020-01-01", dt.datetime.today())
gdpCA = pdr.DataReader("NGDPRSAXDCCAQ", "fred", "2020-01-01", dt.datetime.today())