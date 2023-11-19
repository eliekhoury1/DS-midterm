FROM python:latest
COPY main.py .
COPY prob_calculator.py .
ENTRYPOINT ["python3","main.py"]
