FROM ubuntu:22.04

# location in the container
ENV TA_DIR /home/app/

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 && apt-get install -y \
    python3-pip
WORKDIR ${TA_DIR}

# Copy sources into the container
COPY . .

#Install the pip3 requirements
RUN pip3 install .                                
RUN pip3 install -r requirements.txt
RUN pip3 install requests-toolbelt==0.10.1

#Expose the ports
EXPOSE 31000
