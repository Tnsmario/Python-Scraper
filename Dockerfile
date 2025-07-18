#   Base image with Python
FROM python:3.13-slim
#   Setting up the working directory
WORKDIR /app
#   Copy files to docker
COPY . /app
#   Install all the libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && playwright install --with-deps
#   Exposing the port
EXPOSE 5000
#   Command to start the app
CMD ["python", "app.py"]
