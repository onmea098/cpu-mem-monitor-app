# official python image as base image
FROM python:3.9-slim-buster 

# set wrkdir in the container
WORKDIR /app

# copy req file to wrkdir
COPY requirements.txt .

# install req python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# copy app code to wrkdir
COPY . .

# set environ var for flask app
ENV FLASK_RUN_HOST=0.0.0

# exposes port on which flask app will run
EXPOSE 5000

# start flask app when container is run
CMD ["flask", "run"]