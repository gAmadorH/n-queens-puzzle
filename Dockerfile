FROM python:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD src/ .
RUN pip install -r requirements.txt
CMD ["python", "index.py"]