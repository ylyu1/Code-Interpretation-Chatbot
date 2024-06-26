# Use an official Python runtime as a parent image
FROM python:3.11.9-slim

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# to run entrypoint.sh need to change the mode of the file to an executable
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
