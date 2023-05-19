import os
import shutil

# Pfad zum Ordner mit den Artikeln
artikel_ordner = '/pfad/zum/artikel_ordner'

# Pfad zum Zielordner für Zusammenhänge und Schlagwörter
ziel_ordner_zusammenhänge = '/pfad/zum/zusammenhänge_ordner'
ziel_ordner_schlagwörter = '/pfad/zum/schlagwörter_ordner'

# Überprüfen, ob die Zielordner bereits vorhanden sind, andernfalls erstellen
if not os.path.exists(ziel_ordner_zusammenhänge):
    os.makedirs(ziel_ordner_zusammenhänge)

if not os.path.exists(ziel_ordner_schlagwörter):
    os.makedirs(ziel_ordner_schlagwörter)

# Durchlaufe alle Dateien im Artikelordner
for datei in os.listdir(artikel_ordner):
    if datei.endswith('.txt'):
        # Lese den Inhalt der Artikel-Datei ein
        with open(os.path.join(artikel_ordner, datei), 'r') as f:
            artikel_inhalt = f.read()

        # Verarbeite den Artikelinhalt, um Zusammenhänge und Schlagwörter zu extrahieren
        # Hier kannst du deinen eigenen Code für die Verarbeitung und Extraktion implementieren

        # Speichere Zusammenhänge in separater Datei im Zielordner
        zusammenhänge_datei = os.path.join(ziel_ordner_zusammenhänge, datei)
        with open(zusammenhänge_datei, 'w') as f:
            # Schreibe den Zusammenhangsinhalt in die Datei
            f.write(zusammenhänge_inhalt)

        # Speichere Schlagwörter in separater Datei im Zielordner
        schlagwörter_datei = os.path.join(ziel_ordner_schlagwörter, datei)
        with open(schlagwörter_datei, 'w') as f:
            # Schreibe den Schlagwörterinhalt in die Datei
            f.write(schlagwörter_inhalt)

        print(f'Artikel "{datei}" verarbeitet und in Zusammenhänge und Schlagwörter aufgeteilt.')

print('Verarbeitung abgeschlossen.')
