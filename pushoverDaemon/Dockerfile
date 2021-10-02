from ubuntu:20.04

run apt-get update
run apt-get upgrade

run apt-get install python3 -y 
run apt-get install python3-pip -y

run mkdir /pushoverDaemon
workdir /pushoverDaemon

copy requirements.txt /pushoverDaemon
copy main.py /pushoverDaemon
copy bootstrap.sh /pushoverDaemon
copy secrets.json /pushoverDaemon

run cd /pushoverDaemon
run ./bootstrap.sh
cmd ./main.py

