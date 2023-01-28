# Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.
# Soubor si ulož a načti do slovníku.
# Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".
# Výsledný slovník ulož jako JSON do souboru prospech.json.

import json
with open("python-1/body.json", mode="r", encoding="utf-8") as soubor:
    data = soubor.read()

body = json.loads(data)


# pro jednotlivého studenta:
#if body["Robert Pospíšil"] < 60:
#    body["Robert Pospíšil"] = "Fail"
#else:
#    body["Robert Pospíšil"] = "Pass"
#print(body["Robert Pospíšil"])

# pro celou skupinu studentů:
for student in body:
    if body[student] < 60:
        body[student] = "Fail"
    else:
        body[student] = "Pass"

print(body)

with open('python-1/prospech.json', mode='w', encoding='utf-8') as soubor:
    json.dump(body, soubor)