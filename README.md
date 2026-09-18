Este projeto tem como objetivo realizar o pré-processamento das imagens do dataset Fruits-262, redimensionando as imagens para que possuam no máximo 300×300 pixels e adicionando transparência nas áreas restantes. Dessa forma, todas as imagens passam a possuir uma dimensão padronizada de 300×300 pixels, mantendo sua proporção original e evitando cortes na imagem.

Para instalar todas as bibliotecas utilizadas no projeto, abra o terminal na pasta onde estão os arquivos do projeto e execute o comando pip install -r ./requirements. Após a instalação, o projeto estará pronto para ser executado.

As bibliotecas utilizadas são python-dotenv, pathlib e Pillow. A biblioteca python-dotenv é utilizada para carregar o caminho do dataset a partir de uma variável de ambiente, evitando que o caminho absoluto dos arquivos fique diretamente definido no código. A biblioteca pathlib é utilizada para facilitar a navegação e manipulação dos diretórios e arquivos do dataset. Já a biblioteca Pillow é responsável pela leitura, redimensionamento, criação, manipulação e salvamento das imagens.

O projeto também utiliza a biblioteca os, que faz parte da biblioteca padrão do Python, para acessar a variável de ambiente que contém o caminho do dataset. Por esse motivo, ela não precisa ser instalada separadamente pelo pip.

O caminho do dataset é definido no arquivo .env por meio da variável path_pictures. Dessa forma, é necessário configurar essa variável antes de executar o programa, apontando para a pasta onde estão armazenadas as imagens do Fruits-262.

O processamento percorre as categorias existentes dentro da pasta do dataset e, posteriormente, cada imagem encontrada. Cada imagem é redimensionada proporcionalmente utilizando como limite máximo 300×300 pixels. Em seguida, é criada uma nova imagem com exatamente 300×300 pixels e fundo transparente. A imagem redimensionada é então posicionada no centro dessa nova área, preservando sua proporção original. Por fim, a imagem resultante é salva no mesmo local da imagem original no formato PNG.

O dataset utilizado neste projeto é o Fruits-262, disponibilizado no Kaggle por Mihai Minut. O dataset contém 225.640 imagens distribuídas entre 262 diferentes categorias de frutas. A página do dataset informa que ele está disponível sob a licença CC0: Public Domain. O dataset pode ser obtido diretamente pela plataforma Kaggle.

Para facilitar o download do dataset, também foi utilizado o KaggleHub. O script de download utiliza a identificação aelchimminut/fruits262 para baixar a versão mais recente disponível do dataset. Portanto, caso esse script de download também faça parte do projeto, a biblioteca kagglehub deve estar incluída no arquivo requirements, além das demais dependências mencionadas anteriormente.

Após o download, o caminho retornado pelo KaggleHub pode ser utilizado para localizar os arquivos do dataset e realizar o pré-processamento descrito neste projeto.