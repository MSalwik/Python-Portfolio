bestehende_daten = [42, 55, 61, 48, 70]

quelle_a = [65, -10, 55, 80, 92, 0]
quelle_b = [48, 75, 88, -3, 100, 65]

abgelehnte_daten = []
neue_daten = []

temp_data = []

temp_data.extend(quelle_a)
temp_data.extend(quelle_b)

for data in temp_data:
    if data > 0 and data not in bestehende_daten and data not in neue_daten:
        neue_daten.append(data)
    else:
        abgelehnte_daten.append(data)

neue_daten.insert(0, 50)

bestehende_daten.extend(neue_daten)

sortierte_daten = sorted(bestehende_daten)


print("Management-Auswertung")
print(f"Neue akzeptierte Daten: {neue_daten}")
print(f"Abgelehnte Daten: {abgelehnte_daten}")
print(f"Gesamtdaten: {bestehende_daten}")
print(f"Sortierte Gesamtdaten: {sortierte_daten}")
print(f"Anzahl neuer Werte: {len(neue_daten)}")
print(f"Anzahl abgelehnter Werte: {len(abgelehnte_daten)}")
print(f"Gesamtanzahl: {len(sortierte_daten)}")
print(f"Niedrigster Wert: {sortierte_daten[0]}")
print(f"Höchster Wert: {sortierte_daten[-1]}")

#Plausibilitätsprüfung
unter_50 = 0
zwischen_50_79 = 0
ab_80 = 0

for zahl in sortierte_daten:
    if zahl < 50:
        unter_50 += 1
    elif zahl < 80:
        zwischen_50_79 += 1
    else:
        ab_80 += 1

print(f"Unter 50: {unter_50}")
print(f"50 bis 79: {zwischen_50_79}")
print(f"Ab 80: {ab_80}")

anzahl = unter_50 + zwischen_50_79 + ab_80

if anzahl == len(bestehende_daten):
    print("Plausibilitätsprüfung erfolgreich.")
else:
    print("WARNUNG: Plausibilitätsprüfung fehlgeschlagen.")