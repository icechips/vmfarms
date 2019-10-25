FROM python:3.6

RUN mkdir /vmfarms
WORKDIR /vmfarms
ADD . /vmfarms/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python3.6 /vmfarms/db_create.py
CMD python3.6 /vmfarms/vmfarms.py
