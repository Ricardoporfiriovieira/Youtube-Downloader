# Use uma imagem oficial do Python como imagem base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o diretório de trabalho do contêiner
COPY . .

# Comando para rodar o script da aplicação
CMD ["python", "seu_script.py"]
