FROM python:3.9

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .
CMD ["python", "cpu_bound_multiprocess.py"]