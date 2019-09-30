FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /crag_service

# Set the working directory to /music_service
WORKDIR /crag_service

# Copy the current directory contents into the container at /music_service
ADD . /crag_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt