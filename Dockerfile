# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Flask and gradio-client
RUN pip install Flask gradio_client

# Set the FLASK_APP environment variable
ENV FLASK_APP=index.py

# Make port 5555 available to the world outside this container
EXPOSE 5555

# Run the Flask app
CMD ["flask", "run", "--host", "0.0.0.0"]
