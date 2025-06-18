import os
from deep_translator import GoogleTranslator
import pyttsx3

def vertaal_bestanden(input_map, output_map, bron_taal='en', doel_taal='nl'):
    if not os.path.exists(output_map):
        os.makedirs(output_map)

    for bestand in os.listdir(input_map):
        if bestand.endswith(".txt"):
            pad_oud = os.path.join(input_map, bestand)
            with open(pad_oud, 'r', encoding='utf-8') as f:
                tekst = f.read()

            # Chunk in stukken als het te groot is
            chunks = [tekst[i:i+4500] for i in range(0, len(tekst), 4500)]
            vertaalde_chunks = [GoogleTranslator(source=bron_taal, target=doel_taal).translate(chunk) for chunk in chunks]
            vertaalde_tekst = "\n".join(vertaalde_chunks)

            pad_nieuw = os.path.join(output_map, bestand)
            with open(pad_nieuw, 'w', encoding='utf-8') as f:
                f.write(vertaalde_tekst)
            print(f"Bestand vertaald: {bestand}")

def lijst_en_voorlezen(output_map):
    bestanden = [f for f in os.listdir(output_map) if f.endswith('.txt')]

    if not bestanden:
        print("Geen vertaalde bestanden gevonden.")
        return

    print("\nBeschikbare vertaalde bestanden:")
    for i, bestand in enumerate(bestanden):
        print(f"{i + 1}: {bestand}")

    while True:
        keuze = input("Kies een bestand om voor te lezen (nummer): ")
        if keuze.isdigit() and 1 <= int(keuze) <= len(bestanden):
            gekozen_bestand = bestanden[int(keuze) - 1]
            break
        else:
            print("Ongeldige invoer. Vul een geldig nummer in.")

    with open(os.path.join(output_map, gekozen_bestand), 'r', encoding='utf-8') as f:
        tekst = f.read()

    engine = pyttsx3.init()
    tekst = tekst[:1000]  # Alleen de eerste 1000 tekens
    engine.say(tekst)
    engine.runAndWait()

    bestanden = [f for f in os.listdir(output_map) if f.endswith('.txt')]

    print("\nBeschikbare vertaalde bestanden:")
    for i, bestand in enumerate(bestanden):
        print(f"{i + 1}: {bestand}")

    keuze = int(input("Kies een bestand om voor te lezen (nummer): "))
    gekozen_bestand = bestanden[keuze - 1]

    with open(os.path.join(output_map, gekozen_bestand), 'r', encoding='utf-8') as f:
        tekst = f.read()

    engine = pyttsx3.init()
    engine.say(tekst)
    engine.runAndWait()

# Voorbeeldgebruik
input_map = input("Geef het pad naar de bronmap met tekstbestanden: ")
output_map = input("Geef het pad naar de map voor vertaalde bestanden: ")

vertaal_bestanden(input_map, output_map)
lijst_en_voorlezen(output_map)

