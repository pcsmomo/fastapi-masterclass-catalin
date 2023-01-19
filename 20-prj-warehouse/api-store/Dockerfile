FROM arm64v8/python:3.10-slim-bullseye

RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential 

ENV POETRY_VERSION=1.3.2
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src

# ENV PYTHONPATH="$PYTHONPATH:/src/app"

COPY poetry.lock pyproject.toml .

# This makes to be able to use "uvicorn" without `poetry shell`
RUN poetry config virtualenvs.create false
RUN poetry config installer.parallel false
RUN poetry install --no-interaction --no-ansi

COPY config.py ./config.py
COPY main.py ./main.py

# ENTRYPOINT ["uvicorn", "app.main:app", "--reload"]
# uvicorn app.main:app --host=0.0.0.0 --timeout-keep-alive=0 --port=8001 --reload
ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--timeout-keep-alive=0", "--port=8001", "--reload"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]