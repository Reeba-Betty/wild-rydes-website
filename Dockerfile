FROM python:3.8-slim


WORKDIR /app


COPY . /app

RUN pip install --upgrade pip

RUN pip install flask


EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]