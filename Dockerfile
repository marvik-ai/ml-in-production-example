# https://github.com/tensorflow/tensorflow/issues/52845
FROM --platform=linux/arm64/v8 python:3.8-slim

WORKDIR app

# Dependencies
RUN apt-get update && yes | apt-get upgrade
RUN python3 -m pip --no-cache-dir install --upgrade pip && \
    python --version && \
    pip3 --version

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy local folders
ADD app app
ADD core core

# Run API
EXPOSE 80
CMD ["uvicorn", "app.__main__:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
