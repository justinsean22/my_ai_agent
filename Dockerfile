# Use Python 3.10 (more stable for 2026)
FROM python:3.10-slim

# Create a user so we don't run as root
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

WORKDIR /home/user/app

# Copy and install requirements
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of your code
COPY --chown=user . .

# Tell Hugging Face which port to look at (standard for Spaces)
EXPOSE 7860

# Run your specific agent file
CMD ["python", "outbound_agent.py"]
