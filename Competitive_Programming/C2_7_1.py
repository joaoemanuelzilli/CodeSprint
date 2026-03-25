import numpy as np
import plotly.graph_objects as go

# Função f(x, y) = sqrt(x^2 - y)
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-1, 1, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# k1 = 1 para a função f(x, y)
Z_f = np.sqrt(X**2 - Y)

# Gráfico de f(x, y) = sqrt(x^2 - y) para k1 = 1
fig_f = go.Figure(data=[go.Surface(z=Z_f, x=X, y=Y)])
fig_f.update_layout(title="Conjunto de nível k1 = 1 de f(x, y) = sqrt(x^2 - y)",
                    scene=dict(
                        xaxis_title='x',
                        yaxis_title='y',
                        zaxis_title='f(x, y)'))
fig_f.show()

# Função g(x, y, z) = z - x^2 - y^2
x_vals = np.linspace(-2, 2, 100)
y_vals = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# k2 = 0 para a função g(x, y, z)
Z_g = X**2 + Y**2

# Gráfico de g(x, y, z) = z - x^2 - y^2 para k2 = 0
fig_g = go.Figure(data=[go.Surface(z=Z_g, x=X, y=Y)])
fig_g.update_layout(title="Conjunto de nível k2 = 0 de g(x, y, z) = z - x^2 - y^2",
                    scene=dict(
                        xaxis_title='x',
                        yaxis_title='y',
                        zaxis_title='g(x, y, z)'))
fig_g.show()
