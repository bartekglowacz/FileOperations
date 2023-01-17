import Select_band

print("Program liczy długość fali elektromagnetycznej")
Select_band  # Odpalam moduł z deklaracją zakresu
Lambda = []

for x in range(0, len(Select_band.range_tab), 1):
    # print(f"Sprawdzenie: {Select_band.range_tab[x]}")
    Lambda.append(300/Select_band.range_tab[x])
print(f"Lambda: {Lambda}")

f = open("Lambda", "w")
f.write(f"{Lambda}")
