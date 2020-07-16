#Docker base Image for the GPIO container

# Python Base Image
FROM arm32v7/python:3.9.0b4-buster

# Intall the rpi.gpio and ircodec python module
RUN pip install --no-cache-dir rpi.gpio
RUN pip install ircodec

#Install nano
RUN apt-get update
RUN apt-get install nano

#Install Flask
RUN pip install flask

#Install pgpio daemon
RUN wget https://github.com/joan2937/pigpio/archive/master.zip && \
    unzip -qq master.zip && \
    cd pigpio-master && \
    make && \
    make install
CMD bash
