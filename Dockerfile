# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the cloud
WORKDIR /app

# Copy your grocery list (requirements) and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all your agent code into the cloud
COPY . .

# The command to start your agent
CMD ["python", "outbound_agent.py"]
