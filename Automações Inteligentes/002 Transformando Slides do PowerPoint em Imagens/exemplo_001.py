import os
import win32com.client

def ppt_to_images(ppt_path, output_folder):
    # Cria a pasta de saída, se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Inicia o PowerPoint
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)

    # Exporta cada slide como imagem
    for i, slide in enumerate(presentation.Slides, start=1):
        img_name = f"img_{i:03}.png"
        img_path = os.path.join(output_folder, img_name)

        # Exporta o slide em resolução 4K
        slide.Export(img_path, "PNG", 3840, 2160)
        print(f"Slide {i} salvo como {img_name}")

    # Fecha o PowerPoint
    presentation.Close()
    powerpoint.Quit()

ppt_file = r"C:\path\Slides_de_exemplo.pptx"
output_dir = r"C:\path\slides_images"
ppt_to_images(ppt_file, output_dir)
