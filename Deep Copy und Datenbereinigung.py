import copy

daten = [
    ["Sensor_A", 18, 21, 150, 19],
    ["Sensor_B", 20, 22, 24, 300],
    ["Sensor_C", 17, 18, 19, 20]
]

bereinigte_daten = copy.deepcopy(daten)

for zeile in bereinigte_daten:
    for wert in zeile[1:]:
        if wert > 100:
            zeile.remove(wert)

print("Originaldaten:")
for zeile in daten:
    print(zeile)

print("Bereinigte Daten:")
for zeile in bereinigte_daten:
    print(zeile)