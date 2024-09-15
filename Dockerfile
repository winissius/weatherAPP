# Imagem oficial do python, versao slim mais leve
FROM python:3

# diretorio padrao
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala os requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# se provou nao necessario, o COPY . . já faz tudo isso.
# COPY .env .env

# Expoe porta 5000
# EXPOSE 5000

# Define o ponto de entrada para rodar a aplicação Flask
CMD ["python", "main.py"]