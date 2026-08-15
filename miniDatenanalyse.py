umsatzdaten = [
    ["Produkt A", 1200, 1350, 1100],
    ["Produkt B", 850, 920, 980],
    ["Produkt C", 1500, 1600, 1750],
    ["Produkt D", 400, 380, 450]
]

gesamtumsatz_daten = []

for zeile in umsatzdaten:
    produkt = zeile[0]
    umsatz = 0

    for wert in zeile[1:]:
        umsatz += wert

    gesamtumsatz_daten.append([produkt, umsatz])

for zeile in gesamtumsatz_daten:
    print(f"{zeile[0]}: {zeile[1]} Euro")

hoechstumsatz = 0
bestes_produkt = ""

for zeile in gesamtumsatz_daten:
    if zeile[1] > hoechstumsatz:
        hoechstumsatz = zeile[1]
        bestes_produkt = zeile[0]

print(f"Produkt mit höchstem Gesamtumsatz: {bestes_produkt}")
print(f"Gesamtumsatz: {hoechstumsatz} Euro")