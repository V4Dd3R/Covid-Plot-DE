import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import savgol_filter
#######################################
# Einlesen der Daten
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
    name='Fallzahlen geglättet'                                                     # Name der Datenreihe
))
fig.add_trace(go.Scatter(
    x=subset_DE.dateRep,                                                            # Daten für x-Achse
    y=subset_DE.cases,                                                              # Daten für y-Achse
    name='Übermittelte Fälle'                                                       # Name der Datenreihe
))
fig.update_traces(hoverinfo='x+y', mode='lines')                                    # Hover-Verhalten und Line-Modus
fig.update_layout(
            legend=dict(y=0.5, font_size=16),                                       # Legende auf halber Höhe (y=0,5)
            title='<b>Tägliche Covid-19 Infektionen Deutschland</b> <br> <a style="font-size: 17px; href="https://opendata.ecdc.europa.eu/">Datenquelle</a>',   # Titel des Plots
            title_x=0.5,                                                            # Titel zentrieren
            xaxis_title='Datum',                                                    # Achsenbeschriftung
            yaxis_title='Anzahl Neuinfektionen pro Tag',
            font=dict(                                                              # Schriftgröße und -Art
                family='Arial',
                size=18
            ))
fig.update_xaxes(autorange="reversed", tickangle=45, dtick=28)
fig.write_html('index.html',                                                        # Erzeugt html file diesen Namens
               auto_open=True,                                                      # File sofort öffnen (Browser)
               include_plotlyjs='True')                                             # Plotly-js file in .html integrieren
