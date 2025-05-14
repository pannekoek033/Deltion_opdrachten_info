import os

def main():
    # Vraag de gebruiker om de mapnaam
    mapnaam = input("Voer de naam of het pad in van de map met afbeeldingen: ").strip()

    # Controleer of de map bestaat
    if not os.path.isdir(mapnaam):
        print("De opgegeven map bestaat niet.")
        return

    # Verkrijg alle bestanden in de map
    bestanden = os.listdir(mapnaam)

    # Filter alleen bestanden (geen submappen)
    bestanden = [f for f in bestanden if os.path.isfile(os.path.join(mapnaam, f))]

    # Schrijf de bestandsnamen naar een tekstbestand
    with open("bestanden.txt", "w", encoding="utf-8") as f:
        for bestand in bestanden:
            f.write(bestand + "\n")

    print(f"{len(bestanden)} bestandsnamen zijn opgeslagen in 'bestanden.txt'.")

if __name__ == "__main__":
    main()
