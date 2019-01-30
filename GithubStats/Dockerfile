FROM python:3.6-slim

RUN pip install requests numpy  
COPY gitrepocheck.py /opt/
WORKDIR /opt

ENTRYPOINT ["python", "gitrepocheck.py"] 


