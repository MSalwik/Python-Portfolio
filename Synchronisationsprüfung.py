system_a = [
    ["K001", "Anna", "AKTIV", "DE"],
    ["K002", "Ben", "AKTIV", "AT"],
    ["K003", "Clara", "INAKTIV", "DE"],
    ["K004", "David", "AKTIV", "FR"],
    ["K005", "Elena", "AKTIV", "DE"],
    ["K006", "Finn", "AKTIV", "AT"]
]

system_b = [
    ["K001", "Anna", "AKTIV", "DE"],
    ["K002", "Ben", "INAKTIV", "AT"],
    ["K004", "David", "AKTIV", "FR"],
    ["K005", "Elena", "AKTIV", "CH"],
    ["K006", "Finn", "AKTIV", "AT"],
    ["K007", "Greta", "AKTIV", "DE"]
]

# [Kunden-ID, Name, Status, Ländercode]

in_beiden_systemen = []
fehlt_in_system_b = []
nur_in_system_b = []
abweichungen = []
unveraenderte_datensaetze = []

for benutzera in system_a:
    gefunden = False

    for benutzerb in system_b:
        if benutzera[0] == benutzerb[0]:
            gefunden = True
            in_beiden_systemen.append(benutzerb)

            hat_abweichung = False

            if benutzera[2] != benutzerb[2]:
                abweichungen.append([benutzera[0], benutzera[1], "Status", benutzera[2], benutzerb[2]])
                hat_abweichung = True
            if benutzera[3] != benutzerb[3]:
                abweichungen.append([benutzera[0], benutzera[1], "Land", benutzera[3], benutzerb[3]])
                hat_abweichung = True
            if not hat_abweichung:
                unveraenderte_datensaetze.append(benutzera)
            break

    if not gefunden:
        fehlt_in_system_b.append(benutzera)

for benutzerb in system_b:
    gefunden = False

    for benutzera in system_a:
        if benutzera[0] == benutzerb[0]:
            gefunden = True
            break

    if not gefunden:
        nur_in_system_b.append(benutzerb)



print(f"Benutzer in beiden Systemen: {in_beiden_systemen}, Anzahl Benutzer in beiden Systemen: {len(in_beiden_systemen)}")
print(f"Benutzer fehlt in System b: {fehlt_in_system_b}")
print(f"Benutzer in in System b: {nur_in_system_b}")
print(f"Anzahl unveränderter Datensätze: {len(unveraenderte_datensaetze)}")
print(f"Anzahl gefundener Abweichungen: {len(abweichungen)}")
print(f"Anzahl gefundener Abweichungen: {abweichungen}")

if len(abweichungen) > 0:
    print(f"ersten gefundenen Abweichungsdatensatz: {abweichungen[0]}")
if len(fehlt_in_system_b) > 0:
    print("Synchronisation unvollständig")
elif len(abweichungen) > 0:
    print("Synchronisation vollständig, aber inkonsistent")
else:
    print("Synchronisation vollständig und konsistent")