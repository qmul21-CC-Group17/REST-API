FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
ENV FLASK_APP /app/run.py
EXPOSE 80
CMD ["python", "run.py"]
