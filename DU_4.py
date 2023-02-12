# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
## Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
## Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

# Tvůj program bude obsahovat dvě funkce:
## První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
## Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# ověření telefonního čísla:
def overeni_cisla(telefon):
    if len(telefon) == 9 or (len(telefon) == 13 and telefon[0:4] == "+420"):
        return(True)
    else:
        return(False)

# výpočet ceny za zprávu:
def cena_zpravy(zprava):
    if len(zprava)%180 == 0:
        cena = (len(zprava)//180)*3
    else:
        cena = (len(zprava)//180 + 1)*3
    return(cena)

# program:
telefon = (input("Zadejte telefonní číslo: "))

if overeni_cisla(telefon) == False:
    print("Litujeme, telefonní číslo není platné.")
else:
    zprava = input("Zadejte zprávu: ")
    print(f" Cena Vaší zprávy je {cena_zpravy(zprava)} Kč.")




