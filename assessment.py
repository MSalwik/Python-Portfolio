mitarbeiter = [
    ["Anna", 42, 91],
    ["Ben", 37, 78],
    ["Clara", 45, 95],
    ["David", 29, 88],
    ["Elena", 41, 83],
    ["Finn", 33, 72]
]

temp = []

for zeile in mitarbeiter:
    if zeile[1] >= 30 and zeile[2] >= 75:
        temp.append(zeile)

ranking_liste = sorted(temp, key=lambda perf : perf[2], reverse=True)

print("Performance Ranking:")
for mitarbeiter in ranking_liste:
    print(f"Platz {ranking_liste.index(mitarbeiter) + 1} - {mitarbeiter[0]}: {mitarbeiter[2]}")

print(f"Anzahl ausgewerteter Mitarbeiter: {len(ranking_liste)}")
print(f"Beste Performance: {ranking_liste[0][0]} mit {ranking_liste[0][2]} Punkten")