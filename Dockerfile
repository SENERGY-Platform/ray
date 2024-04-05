FROM rayproject/ray:2.9.0
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY run_task.py /opt/run_task.py
