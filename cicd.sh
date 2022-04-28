#!/usr/bin/env bash

nohup uwsgi --socket /opt/app/sclbuilder/sclbuilder.sock --module sclbuilder.wsgi --chmod-socket=666 &
while [[ 1 == 1 ]];
do
    git fetch
    git status |grep "Your branch is behind"
    if [[ $? == 0 ]];
    then
        git pull
        pkill -9 uwsgi
        nohup uwsgi --socket /opt/app/sclbuilder/sclbuilder.sock --module sclbuilder.wsgi --chmod-socket=666 &
    fi
    sleep 10
done

