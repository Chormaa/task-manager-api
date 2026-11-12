# what environment does mi application need
FROM python:3.14-slim

# where i will work inside my container
WORKDIR /app

# which files do i need to copy
COPY requirements.txt .

# what should i install or execute during construction
RUN pip install --no-cache-dir -r requirements.txt

# copy all project files into the working directory
COPY . .

# what should be executed when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

