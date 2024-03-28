FROM python:3.10

WORKDIR /brain-games

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1
RUN poetry install --without dev --no-interaction --no-ansi

RUN poetry build
RUN python3 -m pip install dist/*.whl
