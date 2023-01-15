jmeno_a_prijmeni = input("Zadejte své jméno a příjmení")

print(jmeno_a_prijmeni)

# Všechna velká
print(jmeno_a_prijmeni.upper())

# Všechna malá
print(jmeno_a_prijmeni.lower())

rozdelene = jmeno_a_prijmeni.split(" ")

# Pouze iniciály
print(f"{rozdelene.upper()[0][0]}. {rozdelene.upper()[1][0]}.")

# U křestních jmen delších než 5 znaků zkrátit na iniciálu
if len(rozdelene[0]) > 5:
    print(f"{rozdelene[0][0]}. {rozdelene[1]}")
else:
    print(jmeno_a_prijmeni)


#jmeno = jmeno_a_prijmeni.split(" ")[0]
#prijmeni = jmeno_a_prijmeni.split(" ")[1]
#print(f"{jmeno.upper()[0]}. {prijmeni.upper()[0]}.")