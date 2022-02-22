FROM python:3.10

# 
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv uvicorn
RUN pipenv install --deploy --system
COPY apis ./apis
COPY sql_app.db .
COPY runserver.py .

# 

# 
RUN ls
CMD ["uvicorn", "runserver:app", "--host", "0.0.0.0", "--port", "8000"]