# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./llama_cpu_server.py /app/llama_cpu_server.py
COPY **your gguf model here** /app/**your gguf model here**

# Install any needed packages specified in requirements.txt
RUN pip install llama-cpp-python
RUN pip install Flask

# Expose port 5000 to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "llama_cpu_server.py"]
