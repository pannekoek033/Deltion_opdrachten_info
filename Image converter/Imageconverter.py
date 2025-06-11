import os
import asyncio
import platform
from PIL import Image

FPS = 60

async def main():
    # Get user input
    source_dir = input("Voer het pad naar de map met afbeeldingen in: ")
    dest_dir = input("Voer het pad naar de uitvoermap in: ")
    max_size = int(input("Voer het maximale formaat (max 2000 pixels) in: "))

    if max_size > 2000:
        print("Fout: Maximale grootte mag niet groter zijn dan 2000 pixels.")
        return

    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Count and process images
    image_count = 0
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_count += 1
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, f"uitvoer-{filename}")
            print(f"Verwerken: {filename}")
            
            try:
                with Image.open(source_path) as img:
                    # Check and adjust size
                    width, height = img.size
                    if width > max_size or height > max_size:
                        ratio = min(max_size / width, max_size / height)
                        new_width = int(width * ratio)
                        new_height = int(height * ratio)
                        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        img_resized.save(dest_path)
                        print(f"Aangepast: {filename} naar {new_width}x{new_height}")
                    else:
                        img.save(dest_path)
                        print(f"Geen aanpassing nodig: {filename}")
            except Exception as e:
                print(f"Overgeslagen (geen afbeelding): {filename} - Fout: {e}")
        else:
            print(f"Overgeslagen (geen afbeelding): {filename}")

    print(f"Totaal aantal bestanden gevonden: {image_count}")

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())