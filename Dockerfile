FROM python:3.6
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY python-requirements.txt python-requirements.txt
RUN pip install -r python-requirements.txt
COPY . .
CMD ["python", "index"]