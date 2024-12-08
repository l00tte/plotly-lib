
print("themes.py is being loaded!")

#%%

def get_default_theme():
    """
    Returns the default theme configuration for Plotly graphs.

    This includes settings for fonts, background colors, margins, and other
    layout elements for consistent and visually appealing plots.
    """
    return {
        "font": {
            "family": "PP Telegraf, Arial",
            "size": 12,
            "color": "#f0f0f2"
        },
        "paper_bgcolor": "#4d4d54",  # Light grey for the paper background
        "plot_bgcolor": "#4d4d54",   # White for the plotting area background
        "margin": {
            "l": 40,  # Left margin
            "r": 40,  # Right margin
            "t": 50,  # Top margin
            "b": 50   # Bottom margin
        },
        "title": {
            "x": 0.5,  # Center the title
            "xanchor": "center",
            "yanchor": "top",
            "font": {
                "size": 18,
                "color": "#f0f0f2"
            }
        },
        "colorway": [
            "#003f5c", 
            "#ff7c43",
            "#2f4b7c",  
            "#665191",  
            "#a05195",  
            "#d45087",
            "#f95d6a",
            "#ffa600"            
        ]  
    }


