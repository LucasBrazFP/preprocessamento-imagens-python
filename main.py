import os
from PIL import Image
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

raw_path = os.getenv("path_pictures")
path_pictures = Path(raw_path)

MAX_SIZE = (300, 300)

for i in path_pictures.iterdir():

    temp_path = Path(i.resolve())

    for j in temp_path.iterdir():
        imagem_atual = Image.open(j.resolve())
        imagem_atual.thumbnail(MAX_SIZE)
        imagem_nova = Image.new("RGBA", (300, 300), (0,0,0,0))

        width, height = imagem_atual.size

        position_x = (300 - width) // 2
        position_y = (300 - height) // 2

        Image.Image.paste(imagem_nova, imagem_atual, (position_x, position_y))

        imagem_nova.save(j.resolve(), format="PNG")