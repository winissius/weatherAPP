# Imagem oficial do python, versao slim mais leve
FROM python:3

# diretorio padrao
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala os requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copia o arquivo .env para o container
COPY .env .env

# Expoe porta 5000
EXPOSE 5000

# variavel de ambiente como dev, poe ser production
ENV FLASK_ENV=development

# Define o ponto de entrada para rodar a aplicação Flask
CMD ["python", "main.py"]
