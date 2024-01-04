# Automatische XML Extraktion für NRA Andalusien

also der code is ziemlich eklig geworden, die haben mehrmals in den Jahren die XML-Felder umbenannt.

zwei Dateien, weil ursprünglich nur Zusammenfassen der xml-Dateien in eine nach Ort gefilterte Excel-Tabelle gedacht war ( ich habs irgendwie ned hingebracht des in eine Datei zu kriegen)

### one.py

generiert ne csv Datei die nach einem Ort und einem Zeitraum gefiltert ist. da muss man manuell die gewünschten Felder und Parameter auskommentieren.

### two.py

fasst die Daten zusammen in Klimadiagramm-Tabellen-Form. auch hier muss man wieder manuell die Vairablen unten ändern je nach gewünschtem Zeitraum

die Ergebnis-Tabellen sind auch dabei:

dataforspecifiedlocation{yyyy} (gefilterte Zusammenfassung der xml dateien (keine Summen oder Durchschnitte))

climatedata{yyyy}.csv (die klimadaten je nach Jahr)
