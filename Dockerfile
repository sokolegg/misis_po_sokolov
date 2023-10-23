FROM python:3.10

RUN pip install fastapi[uvicorn]
RUN pip install uvicorn

COPY ./ ./

EXPOSE 8000:8000

CMD ["python3", "main.py"]