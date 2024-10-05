FROM python:3.11.3-slim-buster

WORKDIR /app

# Install packages
RUN apt-get update
RUN apt install git -y

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

EXPOSE 2034

CMD ["python3", "app.py"]