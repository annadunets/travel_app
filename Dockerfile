FROM python:3

WORKDIR /usr/src/my_app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/usr/src/my_app/manage.py", "runserver", "0.0.0.0:8000"]