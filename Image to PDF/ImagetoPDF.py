import os
from fpdf import FPDF
from PIL import Image

def convert_images_to_pdf(source_dir, output_pdf):
    pdf = FPDF()
    
    # Loop through files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith('.jpg'):
            file_path = os.path.join(source_dir, filename)
            
            # Add a new page
            pdf.add_page()
            
            # Get image dimensions using PIL
            with Image.open(file_path) as img:
                width, height = img.size
            
            # Set page size to match image dimensions
            pdf.set_page_size(width, height)
            pdf.image(file_path, 0, 0, width, height)
            
            print(f"Verwerkt: {filename}")
        else:
            print(f"Overgeslagen (geen jpg): {filename}")
    
    # Save the PDF
    pdf.output(output_pdf)
    print(f"PDF-bestand opgeslagen als: {output_pdf}")

if __name__ == "__main__":
    source_dir = input("Voer het pad naar de map met afbeeldingen in: ")
    if not os.path.exists(source_dir):
        print("Map bestaat niet, probeer opnieuw.")
        source_dir = input("Voer het pad naar de map met afbeeldingen in: ")
    
    output_pdf = input("Voer het pad voor het uitvoer-pdf-bestand in: ")
    if output_pdf.lower().endswith('.pdf'):
        convert_images_to_pdf(source_dir, output_pdf)
    else:
        print("Bestand moet eindigen op .pdf, probeer opnieuw.")
        output_pdf = input("Voer het pad voor het uitvoer-pdf-bestand in: ")