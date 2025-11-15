#%% Importa biblioteca do BC e importa base de desemprego
from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
unemployment_df = sgs.get(24369, start= '1996-03-01', end= dt.date.today())
unemployment_df.columns = ['Taxa de Desemprego']
print(unemployment_df)
# %%Monta dataframe com o mínimo dos últimos 12 meses e a média dos últimos 3 meses
unemployment_min_12m_df = unemployment_df.rolling(window= 12 ).min().dropna()
unemployment_min_12m_df.columns = ['Taxa mínima de Desemprego em 12m']
print(unemployment_min_12m_df)
unemployment_mean_3m_df = unemployment_df.rolling(window= 3).mean().dropna()
unemployment_mean_3m_df.columns = ['Média de desemprego 3m']
print(unemployment_mean_3m_df)
# %% Monta dataframe com gatilho da lei de Sahm
trigger_df = unemployment_min_12m_df + 0.5
trigger_df.columns = ['Gatilho']
print(trigger_df)
# %% Unificar os dataframes
unemployment_df = pd.concat([unemployment_df, unemployment_min_12m_df, trigger_df, unemployment_mean_3m_df], axis=1).dropna()
print(unemployment_df)
# %% Adicionar coluna com os meses em que a regra de Sahm foram acionadas
unemployment_df['Acionamento'] = (unemployment_df['Gatilho'] < unemployment_df['Média de desemprego 3m']).map({True: 'Yes', False: 'No'})
print(unemployment_df)
# %% Criar um dataframe apenas com os meses de ativação
active_df = unemployment_df[unemployment_df['Acionamento'] == 'Yes']
print(active_df)
# %% Criar um dataframe com o PIB do Brasil
# %% plotar os gráficos
plt.figure(figsize=(32, 16))
plt.plot(unemployment_df['Gatilho'], label='Gatilho da Regra de Sahm', color='grey')
plt.plot(unemployment_df['Média de desemprego 3m'], label= 'Média 3m', color='blue')
plt.grid(True)
plt.ylabel('%')
plt.xlabel('Time')
plt.legend()
plt.show()
# %%
