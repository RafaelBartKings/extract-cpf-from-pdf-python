# Extrator de CPFs de PDF

Este projeto em Python extrai os valores do campo CPF de arquivos PDF e salva-os em um arquivo JSON.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `main.py`: Arquivo principal que executa o processo de extração.
- `extractor.py`: Contém a função que realiza a extração dos CPFs do PDF.
- `requirements.txt`: Lista de bibliotecas Python necessárias para rodar o projeto.
- `pdfs/`: Diretório onde os arquivos PDF devem ser colocados.
- `cpfs.json`: Arquivo onde os CPFs extraídos serão salvos.

## Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado na sua máquina. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/extrai-cpf-python.git
    cd extrai-cpf-python
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    .\venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque os arquivos PDF que você deseja extrair os CPFs no diretório `pdfs/`.

2. Execute o script principal:
    ```bash
    python main.py
    ```

3. Após a execução, os CPFs extraídos serão salvos no arquivo `cpfs.json` no mesmo diretório.

## Customização

Se você desejar modificar o nome do diretório de entrada ou do arquivo JSON de saída, altere as variáveis `pdf_directory` e `json_path` no arquivo `main.py` conforme necessário.

## Contribuição

Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
