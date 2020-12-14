import datetime as dt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import savgol_filter
#######################################
# Einlesen der Daten
data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv',
                   sep=','
                   )
# Für anderes Land anderen isocode verwenden
subset_DE = data[data.iso_code == 'DEU']                                        # Statistik für Deutschland
cases = subset_DE.new_cases                                                     # Neue Positivtests
deaths = subset_DE.new_deaths                                                   # Neue Todesfälle
dates_str = subset_DE.date                                                      # Datum (noch in str format)
dates = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in dates_str]   # Datum in datetime format
today = dt.date.today()                                                         # Heutiges Datum (für Titel)
# Plot (benötigt Plotly-Installation)
fig = make_subplots(specs=[[{"secondary_y": True}]])
config = {
    'displaylogo': False,
    'toImageButtonOptions': {
        'format': 'svg',  # png, svg, jpeg, webp
        'filename': 'Covid_DE ' + today.strftime("%d %b %Y"),
        'height': 771,
        'width': 1200,
        'scale': 1
    },
    'modeBarButtonsToAdd': ['drawline',
                            'drawopenpath',
                            'drawclosedpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape'
                            ]
}
# Glätten der Zahlen über Savitzky-Golay-Filter (Zeitraum von 3 Wochen, 2. Ordnung)
fig.add_trace(go.Scatter(
    x=dates,                                    # Daten für x-Achse
    y=round(cases),                             # Daten für y-Achse
    name='Tägliche Positivtests',               # Name der Datenreihe
    mode='lines+markers'),
    secondary_y=False)
fig.add_trace(go.Scatter(
    x=dates,                                    # Daten für x-Achse
    y=np.round(savgol_filter(cases, 21, 2)),    # Daten für y-Achse
    name='Tägliche Positivtests (geglättet)',   # Name der Datenreihe
    mode='lines'),
    secondary_y=False)
fig.add_trace(go.Scatter(
    x=dates,                                    # Daten für x-Achse
    y=round(deaths),                            # Daten für y-Achse
    name='Tägliche Todesfälle',                 # Name der Datenreihe
    mode='lines+markers'),
    secondary_y=True)
fig.add_trace(go.Scatter(
    x=dates,                                    # Daten für x-Achse
    y=np.round(savgol_filter(deaths, 21, 2)),   # Daten für y-Achse
    name='Tägliche Todesfälle (geglättet)',     # Name der Datenreihe
    mode='lines'),
    secondary_y=True)
fig.update_traces(hoverinfo='x+y')              # Hover-Verhalten
fig.update_yaxes(exponentformat='none', tickformat='{}',
                 title_text='Anzahl positiver Tests pro Tag', secondary_y=False)
fig.update_yaxes(exponentformat='none', tickformat='{}',
                 title_text='Anzahl Todesfälle pro Tag', secondary_y=True)
fig.update_layout(
    legend=dict(font_size=15,                   # Legendeneinstellungen
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor="white",
                ),
    title_font=dict(size=18),
    title=('<b>Covid-19 Übersicht Deutschland</b> <br>' +  # Titel des Plots
           'Stand: ' + today.strftime("%d %b %Y") +
           ' <a style="font-size:16px"; href="https://ourworldindata.org/coronavirus">(Datenquelle)</a>' +
           ' <a style="font-size:16px"; href="https://github.com/V4Dd3R/Covid-Plot-DE">(Quellcode)</a>'),
    title_x=0.5,                    # Titel zentrieren
    title_xanchor='center',
    xaxis_title='Datum',            # Achsenbeschriftung
    font=dict(                      # Schriftgröße und -Art
        family='Arial',
        size=16
    ),
    plot_bgcolor="LightGray",       # Hintergrundfarbe

)
fig.write_html('index.html',  # Erzeugt html file diesen Namens
               auto_open=True,  # File sofort öffnen (Browser)
               include_plotlyjs='True',  # Plotly-js in .html integrieren
               config=config)
