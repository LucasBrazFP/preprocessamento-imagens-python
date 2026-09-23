
import os
import io
import time
from pathlib import Path

from dotenv import load_dotenv
from PIL import Image, ImageEnhance
from rembg import remove, new_session


load_dotenv()

raw_path = os.getenv("path_pictures")

if not raw_path:
    raise ValueError(
        "A variável path_pictures não foi encontrada no .env"
    )

path_pictures = Path(raw_path)

MAX_SIZE = (300, 300)

IMAGENS_POR_FRUTA = 2

PASTA_SAIDA = (
    path_pictures.parent / "Processed_Images"
)

PASTA_PREVIEW = (
    path_pictures.parent / "Segmentation_Previews"
)

EXTENSOES_VALIDAS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}


PASTA_SAIDA.mkdir(
    parents=True,
    exist_ok=True
)

PASTA_PREVIEW.mkdir(
    parents=True,
    exist_ok=True
)


print("Carregando modelo de segmentação...")
print("Isso acontece apenas uma vez.")

inicio_modelo = time.time()

session = new_session("u2netp")

tempo_modelo = time.time() - inicio_modelo

print(
    f"Modelo carregado em "
    f"{tempo_modelo:.1f} segundos."
)

print()


def remover_fundo(caminho):

    with open(caminho, "rb") as arquivo:

        imagem_original = arquivo.read()

    imagem_sem_fundo = remove(
        imagem_original,
        session=session
    )

    return Image.open(
        io.BytesIO(imagem_sem_fundo)
    ).convert("RGBA")


def preparar_imagem(imagem):

    imagem.thumbnail(
        MAX_SIZE,
        Image.Resampling.LANCZOS
    )

    fundo = Image.new(
        "RGB",
        (300, 300),
        (255, 255, 255)
    )

    largura, altura = imagem.size

    x = (
        300 - largura
    ) // 2

    y = (
        300 - altura
    ) // 2

    fundo.paste(
        imagem,
        (x, y),
        imagem
    )

    fundo = ImageEnhance.Contrast(
        fundo
    ).enhance(1.10)

    return fundo


pastas_frutas = []

total = 0


for pasta_fruta in sorted(
    path_pictures.iterdir()
):

    if not pasta_fruta.is_dir():
        continue

    imagens = [
        imagem
        for imagem in pasta_fruta.iterdir()
        if (
            imagem.is_file()
            and imagem.suffix.lower()
            in EXTENSOES_VALIDAS
        )
    ]

    imagens = imagens[
        :IMAGENS_POR_FRUTA
    ]

    if imagens:

        pastas_frutas.append(
            (
                pasta_fruta,
                imagens
            )
        )

        total += len(imagens)


print(
    f"Classes encontradas: "
    f"{len(pastas_frutas)}"
)

print(
    f"Imagens por fruta: "
    f"{IMAGENS_POR_FRUTA}"
)

print(
    f"Total de imagens: "
    f"{total}"
)

print()
print("Iniciando processamento...")
print()


processadas = 0
erros = 0

inicio_processamento = time.time()


for pasta_fruta, imagens in pastas_frutas:

    pasta_saida_fruta = (
        PASTA_SAIDA /
        pasta_fruta.name
    )

    pasta_saida_fruta.mkdir(
        parents=True,
        exist_ok=True
    )


    for caminho_imagem in imagens:

        try:

            imagem = remover_fundo(
                caminho_imagem
            )

            imagem_processada = preparar_imagem(
                imagem
            )

            nome_saida = (
                caminho_imagem.stem
                + ".png"
            )

            caminho_saida = (
                pasta_saida_fruta /
                nome_saida
            )

            imagem_processada.save(
                caminho_saida,
                "PNG"
            )

            processadas += 1


            tempo_atual = (
                time.time()
                - inicio_processamento
            )

            media_por_imagem = (
                tempo_atual
                / processadas
            )

            restantes = (
                total - processadas
            )

            tempo_restante = (
                media_por_imagem
                * restantes
            )

            minutos = int(
                tempo_restante // 60
            )

            segundos = int(
                tempo_restante % 60
            )


            if (
                processadas == 1
                or processadas % 5 == 0
                or processadas == total
            ):

                porcentagem = (
                    processadas
                    / total
                ) * 100

                print(
                    f"[{processadas}/{total}] "
                    f"{porcentagem:.2f}% | "
                    f"Tempo restante estimado: "
                    f"{minutos}m "
                    f"{segundos}s"
                )


        except Exception as erro:

            erros += 1

            print(
                f"ERRO: "
                f"{caminho_imagem}"
            )

            print(
                f"Motivo: {erro}"
            )


tempo_total = (
    time.time()
    - inicio_processamento
)

print()
print("==============================")
print("PROCESSAMENTO CONCLUÍDO")
print("==============================")

print(
    f"Processadas: {processadas}"
)

print(
    f"Erros: {erros}"
)

print(
    f"Tempo total: "
    f"{tempo_total / 60:.1f} minutos"
)

print()
print(
    f"Resultado: {PASTA_SAIDA}"
)

