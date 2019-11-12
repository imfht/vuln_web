FROM python:3.7-alpine
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
ADD . /app/
WORKDIR /app/
CMD ["python3","/app/app.py"]