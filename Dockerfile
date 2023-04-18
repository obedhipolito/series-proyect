FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /series
WORKDIR /series
COPY requirements.txt /series/
RUN pip install -r requirements.txt
COPY . /series/
RUN python3 manage.py makemigration --settings=settings.production
CMD python3 manage.py runserver --settings=settings.production 0.0.0.0:8080
