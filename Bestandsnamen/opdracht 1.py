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

# Vraag om de mapnaam
mapnaam = input("Voer de mapnaam in met afbeeldingen: ").strip()

# Controleer of de map bestaat
if not os.path.isdir(mapnaam):
    print("Map bestaat niet.")
    exit()

# Alleen afbeeldingsbestanden
extensies = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
bestanden = [f for f in os.listdir(mapnaam) if f.lower().endswith(extensies)]

# Hernoem bestanden en schrijf naar tekstbestand
with open("bestanden.txt", "w", encoding="utf-8") as f:
    for i, oud in enumerate(bestanden, 1):
        _, ext = os.path.splitext(oud)
        nieuw = f"movie_poster_{i}{ext}"
        os.rename(os.path.join(mapnaam, oud), os.path.join(mapnaam, nieuw))
        f.write(nieuw + "\n")

print("Bestanden zijn hernoemd en opgeslagen in 'bestanden.txt'.")