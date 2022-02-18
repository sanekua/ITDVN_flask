FROM python:3.8
RUN useradd --create-home userapi
WORKDIR /ITDVN_flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /ITDVN_flask .
RUN chown -R userapi:userapi ./
USER userapi

EXPOSE 8000

CMD ["python", "/wsgi.py"]

