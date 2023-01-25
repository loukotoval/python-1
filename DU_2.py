# Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. Následně naprogramuj následující varianty:

# Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
# Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
# Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod = input("Zadejte číslo součástky:")
mnozstvi = int(input("Zadejte požadované množství:"))

if kod not in sklad:
    print("Součástka není skladem.")
elif kod in sklad and mnozstvi >= sklad[kod]:
    print(f"Požadované součástky je možné prodat pouze {sklad[kod]} ks, tj. o {mnozstvi - sklad[kod]} ks méně než je požadavek.")
    sklad.pop(kod)
else:
    print("Poptávku lze uspokojit v plné výši.")
    sklad[kod] = sklad[kod] - mnozstvi
    print(f"Na skladě zbývá {sklad[kod]} ks součástky {kod}.")

