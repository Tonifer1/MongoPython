from pymongo import MongoClient
from bson import ObjectId

# Yhteys MongoDB:hen
client = MongoClient("mongodb://localhost:27017/")
db = client["jasenrekisteri"]
collection = db["jasenet"]

# Lisää uusi jäsen
def lisaa_jasen(etunimi, sukunimi, osoite, postinumero, puhelin, sahkoposti, jasenyydenAlkuPvm):
    jasen = {
        "etunimi": etunimi,
        "sukunimi": sukunimi,
        "osoite": osoite,
        "postinumero": postinumero,
        "puhelin": puhelin,
        "sahkoposti": sahkoposti,
        "jasenyydenAlkuPvm": jasenyydenAlkuPvm
    }
    collection.insert_one(jasen)
    print("Jäsen lisätty onnistuneesti.")

# Lue jäsenet
def hae_jasenet():
    jasenet = collection.find()
    for jasen in jasenet:
        print(jasen)

# Päivitä jäsenen tietoja
def paivita_jasen(jasen_id, paivitykset):
    result = collection.update_one({"_id": jasen_id}, {"$set": paivitykset})
    if result.matched_count > 0:
        print("Jäsenen tiedot päivitetty.")
    else:
        print("Jäsentä ei löytynyt.")

# Poista jäsen
def poista_jasen(jasen_id):
    result = collection.delete_one({"_id": jasen_id})
    if result.deleted_count > 0:
        print("Jäsen poistettu.")
    else:
        print("Jäsentä ei löytynyt.")



while True:
    print("\nValitse toiminto:")
    print("1: Lisää jäsen")
    print("2: Hae kaikki jäsenet")
    print("3: Päivitä jäsen")
    print("4: Poista jäsen")
    print("0: Lopeta")
    valinta = input("Syötä valintasi: ")

    match valinta:
        case "1":
            etunimi = input("Etunimi: ")
            sukunimi = input("Sukunimi: ")
            osoite = input("Osoite: ")
            postinumero = input("Postinumero: ")
            puhelin = input("Puhelin: ")
            sahkoposti = input("Sähköposti: ")
            jasenyydenAlkuPvm = input("Jäsenyyden alkamispäivämäärä (YYYY-MM-DD): ")
            lisaa_jasen(etunimi, sukunimi, osoite, postinumero, puhelin, sahkoposti, jasenyydenAlkuPvm)

        case "2":
            print("Kaikki jäsenet:")
            hae_jasenet()

        case "3":
            jasen_id = input("Syötä jäsenen _id (kopioi MongoDB:stä): ")
            paivitykset = {}
            osoite = input("Uusi osoite (jätä tyhjäksi, jos ei muutosta): ")
            puhelin = input("Uusi puhelin (jätä tyhjäksi, jos ei muutosta): ")
            if osoite:
                paivitykset["osoite"] = osoite
            if puhelin:
                paivitykset["puhelin"] = puhelin
            paivita_jasen(ObjectId(jasen_id), paivitykset)

        case "4":
            jasen_id = input("Syötä jäsenen _id (kopioi MongoDB:stä): ")
            poista_jasen(ObjectId(jasen_id))

        case "0":
            print("Ohjelma lopetetaan.")
            break

        case _:
            print("Virheellinen valinta. Yritä uudelleen.")
     


