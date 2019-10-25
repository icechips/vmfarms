FROM python:3.6

RUN mkdir /vmfarms
WORKDIR /vmfarms
ADD . /vmfarms/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/vmfarms/db_create.py"]
CMD ["python", "/vmfarms/vmfarms.py"]
