
print("themes.py is being loaded!")


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
            "color": "#6de3db"
        },
        "paper_bgcolor": "#dfeff0",  # Light grey for the paper background
        "plot_bgcolor": "#365469",   # White for the plotting area background
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
                "color": "#6de3db"
            }
        },
        "colorway": [
            "#64a8b0",  # Blue
            "#29808a",  # Red
            "#0d444a",  # Green
            "#012024",  # Purple
            "#617574"   # Orange
        ]  # Consistent colors for traces
    }
