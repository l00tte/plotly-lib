#%%
import sys
import os

# Add the project directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

#%%
import plotly.graph_objects as go
from lib_plotly.theme import get_default_theme

#%%

# Get the default theme
theme = get_default_theme()

# Create a sample figure
fig = go.Figure(data=[
    go.Bar(name='Category A', x=['X1', 'X2', 'X3'], y=[10, 15, 20]),
    go.Bar(name='Category B', x=['X1', 'X2', 'X3'], y=[5, 10, 15])
])

# Apply the theme to the figure
fig.update_layout(**theme)

# Show the figure
fig.show()

# %%
