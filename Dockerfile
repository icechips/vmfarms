FROM python:3.6

COPY . /vmfarms
WORKDIR /vmfarms
RUN pip install -r requirements.txt

EXPOSE 5000
CMD python3.6 /vmfarms/vmfarms.py
