# Basic
import os, sys
# import io
# import base64
from pathlib import Path
import json

# Data
import pandas as pd

# Dash
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc

# Import Local tabs etc
from layout.tabs import layout as main_layout
from callbacks.timeline_callbacks import register_timeline_callbacks
from callbacks.compare_callbacks import register_compare_callbacks

# Set root path
script_dir = Path(__file__).resolve()
project_root = script_dir.parent.parent
sys.path.append(str(project_root))

# Import Local Modules
from src.utils.image_paths import get_imagery_reference_path, assemble_location_imagery
from src.utils.constants import DATA_PATH, REF_FILE_RELATIVE_PATH, AVAILABLE_YEARS
from scripts.test_compare_models import run_all_models
from src.viz.compare_images import create_comparison_figure
from src.viz.utils import load_images

location_15_images = assemble_location_imagery(15, DATA_PATH, AVAILABLE_YEARS, 20)

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Layout
app.layout = main_layout

register_timeline_callbacks(app)
register_compare_callbacks(app)

if __name__ == '__main__':
    app.run(debug=True)
