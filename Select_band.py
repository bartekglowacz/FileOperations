print("Jaki zakres wypisać?")
Range = input()
Range = Range.split(" ")
down = int(Range[0])
up = int(Range[1])
range_tab = []
print(f"Zakres to: {Range}, a typ to: {type(Range)}")
print(f"Dolny zakres to: {down}, typ = {type(down)}\nGórny zakres to: {up}, typ = {type(up)})")
print("Jaki krok częstotliwości w megahertzach?")
step = int(input())

#tworzymy plik, w którym wypiszemy pożądane częstotliwości
f = open("f [MHz]", "w")
for x in range (down, up+step, step):
    f.write(f"{x}\n")
    range_tab.append(x)

f.close()
print(f"Tablica z częstotliwościami: {range_tab}")

f = open("Tablica z częstotliwościami", "w")
f.write(f"{range_tab}")
print("KONIEC")
