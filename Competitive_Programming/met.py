import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import make_interp_spline

# Dados de Indicação (Eixo X)
indicacao = np.array([16, 20, 24, 30, 36, 40, 44, 50, 60, 70, 80])

# Valores de Erro Máximo Observados
erro_maximo_constante = 1.85  # Valor constante do erro máximo (pode ser ajustado conforme o gráfico)

tendencia_central = np.array([0.266, 0.348, 0.766, 0.728, 0.870, 0.668, 0.890, 0.808, 0.796, 0.874, 0.824])

# Ajuste de Suavização: Interpolação com Respeito à Curvatura Desejada
x_smooth = np.linspace(indicacao.min(), indicacao.max(), 300)

# Interpolação cúbica para suavizar a curva de tendência
spl_tend = make_interp_spline(indicacao, tendencia_central, k=3)
tendencia_smooth = spl_tend(x_smooth)

# Calcular as faixas superior e inferior (com erro constante)
erro_superior = tendencia_smooth + erro_maximo_constante
erro_inferior = tendencia_smooth - erro_maximo_constante

# Criar o gráfico usando Plotly
fig = go.Figure()

# Linhas da faixa de erro (sem preenchimento)
fig.add_trace(go.Scatter(
    x=x_smooth, y=erro_superior,
    mode='lines',
    line_color='red',
    name='Erro Superior (+Emax)'
))

fig.add_trace(go.Scatter(
    x=x_smooth, y=erro_inferior,
    mode='lines',
    line_color='blue',
    name='Erro Inferior (-Emax)'
))

# Linha da Tendência Central
fig.add_trace(go.Scatter(
    x=x_smooth, y=tendencia_smooth,
    mode='lines',
    line=dict(color='green'),
    name='Tendência Central'
))

# Pontos Originais
fig.add_trace(go.Scatter(
    x=indicacao, y=tendencia_central,
    mode='markers', name='Tendência Central (Original)',
    marker=dict(color='green', size=8, line=dict(color='black', width=1))
))

# Configurações do Gráfico
fig.update_layout(
    title='Gráfico de Tendência Central com Faixa de Erro Máximo e Mínimo',
    title_font=dict(size=30),  # Aumentar o tamanho da fonte do título
    xaxis_title='Indicação [V]',
    yaxis_title='Erro [V]',
    showlegend=True,
    legend=dict(font=dict(size=18)),  # Aumentar o tamanho da fonte da legenda
    template="simple_white"
)

# Linha horizontal no 0
fig.add_hline(y=0, line_dash="solid", line_color='black')

# Mostrar o gráfico
fig.show()
