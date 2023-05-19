import os
import shutil

# Pfad zum Ordner mit den Artikeln
artikel_ordner = 'C:\\Users\\'

# Pfad zum Zielordner für Zusammenhänge und Schlagwörter
ziel_ordner_zusammenhänge = 'C:\\Users\\'
ziel_ordner_schlagwörter = 'C:\\Users\\'

# Überprüfen, ob die Zielordner bereits vorhanden sind, andernfalls erstellen
if not os.path.exists(ziel_ordner_zusammenhänge):
    os.makedirs(ziel_ordner_zusammenhänge)

if not os.path.exists(ziel_ordner_schlagwörter):
    os.makedirs(ziel_ordner_schlagwörter)

# Durchlaufe alle Dateien im Artikelordner
for datei in os.listdir(artikel_ordner):
    if datei.endswith('.txt'):
        # Lese den Inhalt der Artikel-Datei ein
        with open(os.path.join(artikel_ordner, datei), 'r', encoding='utf-8') as f:
            artikel_inhalt = f.read()

        # Verarbeite den Artikelinhalt, um Zusammenhänge und Schlagwörter zu extrahieren
        # Hier kannst du deinen eigenen Code für die Verarbeitung und Extraktion implementieren
        
        # Beispiel: Annahme, der Inhalt der Zusammenhänge ist "Zusammenhänge"
        zusammenhänge_inhalt = "Zusammenhänge"

        # Speichere Zusammenhänge in separater Datei im Zielordner
        zusammenhänge_datei = os.path.join(ziel_ordner_zusammenhänge, datei)
        with open(zusammenhänge_datei, 'w', encoding='utf-8') as f:
            # Schreibe den Zusammenhangsinhalt in die Datei
            f.write(zusammenhänge_inhalt)

        # Beispiel: Annahme, der Inhalt der Schlagwörter ist "Schlagwörter"
        schlagwörter_inhalt = "Schlagwörter"

        # Speichere Schlagwörter in separater Datei im Zielordner
        schlagwörter_datei = os.path.join(ziel_ordner_schlagwörter, datei)
        with open(schlagwörter_datei, 'w', encoding='utf-8') as f:
            # Schreibe den Schlagwörterinhalt in die Datei
            f.write(schlagwörter_inhalt)

        print(f'Artikel "{datei}" verarbeitet und in Zusammenhänge und Schlagwörter aufgeteilt.')

print('Verarbeitung abgeschlossen.')
