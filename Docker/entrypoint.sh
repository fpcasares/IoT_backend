#!/bin/bash

# Start pigpiod process
pigpiod
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi

# Clone Necessary Repos if does not exists
bash -c "[ -d './webserver' ] || git clone https://github.com/fpcasares/IoT_backend.git"
bash -c "[ -d './GPIO' ] || git clone https://github.com/fpcasares/GPIO.git"



# Install requirements for webserver
pip install -r ./IoT_backend/requirements.txt

# Start webserver
python /IoT_backend/app.py



