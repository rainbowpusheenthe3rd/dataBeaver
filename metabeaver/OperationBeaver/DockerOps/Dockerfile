# Run this command in the cmd / shell. Will build a Dockerfile named python-app. -t flag means "tag".
#docker build -t python-app .

# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container startup
CMD ["python", "app.py"]