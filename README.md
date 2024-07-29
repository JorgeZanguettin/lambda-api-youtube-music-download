# API - AWS Lambda - Youtube Music Download

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [AWS Deploy ](#aws-deploy)
  - [Run Project ](#run-project)

## About the Project

**[PT]** Projeto desenvolvido com o propósito de construir uma API para realizar download de videos do Youtube
em .mp3, utilizando Python e a infraestrutura Lambda AWS.

**[EN]** Project developed with the aim of building an API to download videos from Youtube
in .mp3, using Python and AWS Lambda infrastructure.

### Built With

- [Python](https://www.python.org/)
    - [YT_DLP](https://pypi.org/project/yt-dlp/)
- [AWS Lambda](https://aws.amazon.com/pt/pm/lambda/)

### Prerequisites

- Python 3.10
- PIP (Python package manager)
- AWS account

### Installation

1. **[PT]** Clone o repositório: | **[EN]** Clone the repository:
    ```bash
    git clone git@github.com:jorgezanguettin/lambda-api-youtube-music-download.git
    ```
2. **[PT]** Navegue para o diretório do projeto: | **[EN]**  Navigate to the project directory:
    ```bash
    cd lambda-api-youtube-music-download
    ```
3. **[PT]** Crie um ambiente virtual: | **[EN]** Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. **[PT]** Instale as dependencias: | **[EN]** Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### AWS Deploy

**[PT]**

Para configurar seu Github, você precisa previamente ter um acesso e credenciais na AWS.

1. Crie um fork deste repositório e adicione os seguintes **[secrets](https://docs.github.com/pt/actions/security-guides/using-secrets-in-github-actions)**:
    - **AWS_ACCESS_KEY_ID** - Access Key da sua AWS
    - **AWS_SECRET_ACCESS_KEY** - Secret Key da sua AWS
    - **AWS_REGION** - Regiao da sua AWS
2. Execute o Workflow **deploy_lambda.yml**
3. Pronto! O Workflow deve dar conta de configurar o restante


**[EN]**

To set up your Github, you must first have access and credentials to AWS.

1. Fork this repository and add the following **[secrets](https://docs.github.com/pt/actions/security-guides/using-secrets-in-github-actions)**:
    - **AWS_ACCESS_KEY_ID** - Your AWS access key
    - **AWS_SECRET_ACCESS_KEY** - Your AWS secret key
    - **AWS_REGION** - Your AWS region
2. Run the **deploy_lambda.yml** workflow
3. Done! The Workflow must have a configuration account for the remainder

### Run Project

**[PT]**

1. Implemente a função presente nesse repositorio em sua Lambda Functions, não só substituindo o código, mas tambem dando as devidas permissões e vinculando a camada de dependencias na mesma
2. Após o processo de configuracão, basta realizar uma chamada HTTP para a função passando como argumento um **video_id** ou um **video_url**

**[EN]**

1. Implement the function present in this repository in your Lambda Functions, not only replacing the code, but also giving the necessary permissions and linking the dependency layer to it
2. After the configuration process, simply make an HTTP call to the function passing a **video_id** or a **video_url** as an argument
