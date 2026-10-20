pelaaja = input("Mikä on nimesi? ")
terveys = 100

print(f"Tervetuloa seikkailuun, {pelaaja}!")
print(f"Terveytesi on {terveys}.")
print("Edessäsi on synkkä metsä.")
print("Matkasi alkaa nyt.")
print("Metsän polku haarautuu kahteen suuntaan.")
print("Löydät metsästä salaperäisen sivupolun.")
print("Kuulet kaukaa salaperäistä ääntä.")

vastaus = input("Tutkitko salaperäisen sivupolun? (kyllä/ei) ")

if vastaus.lower() == "kyllä":
    print("Löydät polun päästä vanhan arkun.")
    avaa_arkku = input("Avataanko arkku? (kyllä/ei) ")

    if avaa_arkku.lower() == "kyllä":
        print("Arkun sisältä löytyy kultakolikoita!")
    else:
        print("Jätät arkun paikoilleen ja jatkat matkaa.")
else:
    print("Jatkat matkaasi metsän läpi.")