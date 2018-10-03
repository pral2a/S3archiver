FROM python:2.7-slim
COPY . /app
WORKDIR /app
RUN pip install boto urllib2_file apscheduler
CMD python ./run.py