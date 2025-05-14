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

import os

def is_afbeelding(bestand):
    extensies = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    return bestand.lower().endswith(extensies)

def hernoem_en_nummer():
    mapnaam = input("Geef de naam van de map met afbeeldingen: ").strip()

    if not os.path.isdir(mapnaam):
        print("De opgegeven map bestaat niet.")
        return

    bestanden = [f for f in os.listdir(mapnaam) if os.path.isfile(os.path.join(mapnaam, f)) and is_afbeelding(f)]
    bestanden.sort()  # Optioneel: alfabetisch sorteren voor consistentie

    originele_namen = []

    for i, oud in enumerate(bestanden, 1):
        _, ext = os.path.splitext(oud)
        nieuw = f"movie_poster_{i}{ext}"
        os.rename(os.path.join(mapnaam, oud), os.path.join(mapnaam, nieuw))
        originele_namen.append((nieuw, oud))

    with open("originele_namen.txt", "w", encoding="utf-8") as f:
        for nieuw, oud in originele_namen:
            f.write(f"{nieuw}|{oud}\n")

    print(f"{len(originele_namen)} bestanden zijn hernoemd en opgeslagen in 'originele_namen.txt'.")

def herstel_bestandsnamen():
    mapnaam = input("Geef de naam van de map met afbeeldingen: ").strip()

    if not os.path.isdir(mapnaam):
        print("De opgegeven map bestaat niet.")
        return

    if not os.path.isfile("originele_namen.txt"):
        print("Het bestand 'originele_namen.txt' bestaat niet.")
        return

    met_open_fout = False
    with open("originele_namen.txt", "r", encoding="utf-8") as f:
        for regel in f:
            try:
                nieuw, oud = regel.strip().split("|")
                oud_pad = os.path.join(mapnaam, nieuw)
                nieuw_pad = os.path.join(mapnaam, oud)
                if os.path.isfile(oud_pad):
                    os.rename(oud_pad, nieuw_pad)
            except Exception as e:
                print(f"Fout bij hernoemen: {regel.strip()} ({e})")
                met_open_fout = True

    if not met_open_fout:
        print("Alle bestanden zijn teruggezet naar hun originele namen.")
    else:
        print("Er traden enkele fouten op bij het herstellen van bestandsnamen.")

def main():
    print("1. Hernoem en nummer bestanden")
    print("2. Hernoem bestanden naar originele naam")
    keuze = input("Keuze? ").strip()

    if keuze == "1":
        hernoem_en_nummer()
    elif keuze == "2":
        herstel_bestandsnamen()
    else:
        print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
