# Ultroid Extended - Heroku Optimized Version
# Based on Ultroid by TeamUltroid
# Modified for Heroku compatibility

FROM python:3.10-slim

WORKDIR /app

# Install required packages while keeping the image size small
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    ffmpeg \
    mediainfo \
    neofetch \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Set timezone
ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Define command to run on container start
CMD ["bash", "startup"]
