
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

RUN pip install pandas altair 

EXPOSE 8080

COPY app.py .
COPY data data

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

CMD streamlit run app.py \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8080 \
    --server.enableCORS=false \


# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]