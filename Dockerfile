FROM python

EXPOSE 5000

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "flask", "run", "--host", "0.0.0.0" ]
