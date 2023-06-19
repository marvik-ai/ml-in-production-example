# Sentiment Analysis App

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/memray)

This repository was built as an example on how to build an end-to-end Machine Learning solution for being deployed in cloud services. The problem being tackled is multilingual sentiment analysis (classification) given a sentence or a batch of sentences.

## Table of Contents

1. [Installation](#installation)
2. [Docker setup](#docker-setup)
3. [Running locally](#running-locally)
4. [Endpoints](#endpoints)
5. [Request examples](#request-examples)

## Installation

For working locally on your machine, clone the repository and install the dependencies from the [requirements.txt](https://github.com/ignacioaristimuno/property-type-prediction/blob/master/requirements.txt) file.

```bash
git clone https://github.com/marvik-ai/ml-in-production-example.git
```

Then, for installing the dependencies:

```bash
pip install -r requirements.txt
```

## Docker Setup

We recommend running this repository in Docker as we made sure these dependencies worked both on Mac and Windows. For setting up Docker, after cloning the repository, go to the root of the repository and follow these commands:

```bash
docker build -t <docker-username>/<project-name>:<tag> .   # build Docker
```

After the Docker image is built, you should be able to see the image id for running it locally (or in a cloud instance).

```bash
docker image ls -a   # show Docker images built
docker run -p 80:80 <image-id>   # run Docker image
```

For making `FastAPI` available to test locally, while running in Docker, we should expose the port in which the app is running. This had already been set in the `Dockerfile` anyway. As Gradio is mounted within FastAPI, we don't need to expose other ports.


## Running Locally

For running the app locally without Docker, just execute the following `uvicorn` command while being located at the root of the repository:

```bash
python -m uvicorn app.__main__:app --host 0.0.0.0 --port 8080
```

## Endpoints

These are the endpoints which can be accessed within the API:
- `/docs` shows the automatic documentation created by FastAPI. We've included docstrings along with `Pydantic BaseModel` classes and `Enum` so that relevant information is accesible via the documentation.

- `/ping` is a dummy endpoint for testing if the app is up.

- `/predict` the main endpoint for predicting the property type of a batch of propoerties. More detailes about the input and the output are shown in [Request samples](#request-samples)

## Request Examples

### Input Body

For the input request, the body is a JSON composed of a batch of texts within a list, of which we provide an id, the sentence (text), and the language.

```json
[
  {
    "text_id": "00001",
    "text": "I didn't like this movie so far",
    "language": "en"
  },
  {
    "text_id": "00002",
    "text": "No me gustó mucho, tenía una expectativa más alta",
    "language": "es"
  },
  {
    "text_id": "00003",
    "text": "Me cae muy bien, es una persona simpática",
    "language": "es"
  },
  {
    "text_id": "00004",
    "text": "It wasn't that bad, it was ok",
    "language": "en"
  }
]
```

### Response

The response should be another JSON composed of the same batch of texts, containing the predicted class and prediction score associated, along with metadata for every text in the batch.

```json
{
  "preds": [
    {
      "text_id": "00001",
      "text": "I didn't like this movie so far",
      "language": "en",
      "pred_label": "negative",
      "pred_score": 0.08438669331371784,
      "metadata": {
        "negative_score": 0.8389085531234741,
        "neutral_score": 0.15340954065322876,
        "positive_score": 0.007681939750909805
      }
    },
    {
      "text_id": "00002",
      "text": "No me gustó mucho, tenía una expectativa más alta",
      "language": "es",
      "pred_label": "negative",
      "pred_score": 0.1557785803452134,
      "metadata": {
        "negative_score": 0.708398699760437,
        "neutral_score": 0.2716454863548279,
        "positive_score": 0.019955860450863838
      }
    },
    {
      "text_id": "00003",
      "text": "Me cae muy bien, es una persona simpática",
      "language": "es",
      "pred_label": "positive",
      "pred_score": 0.9575374978594482,
      "metadata": {
        "negative_score": 0.012536236084997654,
        "neutral_score": 0.05985251069068909,
        "positive_score": 0.927611231803894
      }
    },
    {
      "text_id": "00004",
      "text": "It wasn't that bad, it was ok",
      "language": "en",
      "pred_label": "neutral",
      "pred_score": 0.5504207164049149,
      "metadata": {
        "negative_score": 0.14649784564971924,
        "neutral_score": 0.6061628460884094,
        "positive_score": 0.24733927845954895
      }
    }
  ]
}
```