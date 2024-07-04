FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD exporter.py /
CMD [ "python", "exporter.py" ]
