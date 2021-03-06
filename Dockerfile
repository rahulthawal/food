FROM python:3.7

WORKDIR /food/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]