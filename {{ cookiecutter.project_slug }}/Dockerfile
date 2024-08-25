FROM python:3.12-bookworm

RUN adduser --uid 999 --system appuser

ARG WORKDIR=/home/appuser
WORKDIR $WORKDIR

COPY ./requirements.txt $WORKDIR/requirements.txt

RUN pip install -U uv && uv pip sync --system $WORKDIR/requirements.txt

COPY ./app $WORKDIR/app

RUN chown -hvR appuser $WORKDIR
USER appuser

CMD ["fastapi", "run", "app/main.py", "--port", "3000"]