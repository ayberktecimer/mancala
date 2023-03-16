FROM python:3.9.6-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80:80