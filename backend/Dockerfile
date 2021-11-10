FROM python:3

WORKDIR /usr/src/backend

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]