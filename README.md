# Covid-Plot-DE
#### Einführung
Ablage für Plot der aktuellen Covid-19-Fallzahlen in Deutschland mit der Plotly-Bibliothek (Python).
Der aktuelle Plot kann online unter https://v4dd3r.github.io/Covid-Plot-DE/index.html betrachtet werden.
#### Installation
Die benötigten Packages sind in der Datei requirements.txt hinterlegt.Diese können mit `pip install -r requirements.txt`
installiert werden.
Für Setup auf dem Raspberry Pi die Kommentare [hier](https://github.com/V4Dd3R/Covid-Plot-DE/issues/1) beachten. 
#### TODO:
- [x] Plot der aktuellen Fahlzahlen als HTML Datei erzeugen und bei github pages hosten
- [x] Automatisches Tägliches Update der index.html datei via cron job auf Raspberry Pi
- [ ] Neue Funktionen (Berechnung, wieviele Tage noch bis ganze Bevölkerung infiziert, R-Wert für letzte 14 Tage o.ä.)
- [ ] Training von Machine-Learning Prädiktionsalgorithmus
------------
#### Introduction
Repository for current covid-19 infection number plots via plotly. The current plot can be visited at 
https://v4dd3r.github.io/Covid-Plot-DE/index.html. 
#### Installation
The required packages can be installed via `pip install -r requirements.txt`.
For setup info regarding the raspberry pi refer to [this](https://github.com/V4Dd3R/Covid-Plot-DE/issues/1).
#### TODO:
- [x] Plot of daily infections as html file generated and hosted on github pages
- [x] Automatic daily update of index.html via cron job on raspberry pi
- [ ] New features (calculate how many days are left until whole population is infected etc.)
- [ ] Train AI to predict future development
