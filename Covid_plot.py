import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import savgol_filter
from datetime import date
#######################################
# Einlesen der Daten
today = date.today()
data = pd.read_csv('https://opendata.ecdc.europa.eu/covid19/casedistribution/csv',
                   sep=','
                   )
# Für anderes Land andere geoId verwenden
subset_DE = data[data.geoId == 'DE']
# Plot (benötigt Plotly-Installation)
fig = make_subplots()
# Glätten der Zahlen über Savitzky-Golay-Filter (Zeitraum von 3 Wochen, 2. Ordnung)
fig.add_trace(go.Scatter(
    x=subset_DE.dateRep,                                                            # Daten für x-Achse
    y=savgol_filter(subset_DE.cases, 21, 2),                                        # Daten für y-Achse
    name='Fallzahlen geglättet',                                                    # Name der Datenreihe
    mode='lines'
))
fig.add_trace(go.Scatter(
    x=subset_DE.dateRep,                                                            # Daten für x-Achse
    y=subset_DE.cases,                                                              # Daten für y-Achse
    name='Übermittelte Fälle',                                                      # Name der Datenreihe
    mode='lines+markers'
))
fig.update_traces(hoverinfo='x+y')                                                  # Hover-Verhalten
fig.update_yaxes(exponentformat='none', tickformat='{}')
fig.update_layout(
            legend=dict(font_size=16),                                              # Legende
            title_font=dict(size=18),
            title=('<b>Tägliche Covid-19 Infektionen Deutschland</b> <br>' +        # Titel des Plots
                   'Stand: ' + today.strftime("%d %b %Y") +
                   ' <a style="font-size:16px"; href="https://opendata.ecdc.europa.eu/">(Datenquelle)</a>' +
                   ' <a style="font-size:16px"; href="https://github.com/V4Dd3R/Covid-Plot-DE">(Quellcode)</a>'),
            title_x=0.5,                                                            # Titel zentrieren
            xaxis_title='Datum',                                                    # Achsenbeschriftung
            yaxis_title='Anzahl Neuinfektionen pro Tag',
            font=dict(                                                              # Schriftgröße und -Art
                family='Arial',
                size=16
            ),
            plot_bgcolor="LightGray"
)
fig.update_xaxes(autorange="reversed", tickangle=45, dtick=28)
fig.write_html('index.html',                                                        # Erzeugt html file diesen Namens
               auto_open=True,                                                      # File sofort öffnen (Browser)
               include_plotlyjs='True')                                             # Plotly-js in .html integrieren
