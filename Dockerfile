FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-devel

# Set environment variables
ENV PATH=/opt/conda/bin:$PATH

# Install dependencies
RUN apt-get update && \ 
    apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    vim\
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists*

RUN conda create -y -n dl python=3.12 jupyter

# Activate the environment
SHELL ["conda", "run", "-n", "dl", "/bin/bash", "-c"]

# Set the working directory
WORKDIR /src

# Copy your project files into the Docker image
COPY . /src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888


