# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy the .env file and the Python project files to the container's working directory
COPY .env pyproject.toml main.py ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the remaining project files
COPY . .

# Ensure static directory exists and copy the database file
RUN mkdir -p heatmap/api/static && mkdir -p data 

# Command to run the application
CMD ["poetry", "run", "python", "main.py"]

