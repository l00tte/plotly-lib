#%%
import sys
import os
import pandas as pd

# Add the project directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

#%%
import plotly.graph_objects as go
import plotly.express as px
import importlib  

import lib_plotly.theme as theme

# Reload the theme module to apply changes
importlib.reload(theme)

#%%


#%%
import pandas as pd 
import plotly.express as px

default_theme = theme.get_default_theme()

# Create a sample figure

data = {
    "category": ["cat1", "cat2", "cat1", "cat2", "cat2"],  # Categories
    "x": [1, 2, 3, 4, 5],  # X-axis values
    "y": [10, 20, 25, 30, 40]  # Y-axis values
}



df = pd.DataFrame(data)


fig = px.bar(df, x = "x", y = "y" ,color = "category",color_discrete_sequence=default_theme["colorway"],title = "Testing")

# Apply the theme to the figure
fig.update_layout(**default_theme)

# Show the figure
fig.show()


# %%
