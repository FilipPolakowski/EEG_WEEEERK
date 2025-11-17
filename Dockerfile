FROM python:3.11-slim

# Do not generate .pyc files and use unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install needed system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements (your own dependencies)
COPY requirements.txt /app/

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# >>> Install DN3 (required for BENDR) <<<
RUN pip install dn3

# >>> Clone BENDR repo <<<
RUN git clone https://github.com/SPOClab-ca/BENDR.git /opt/BENDR

# Copy project files
COPY . /app/

# Default command
CMD ["python", "test2.py"]
