#!/usr/bin/env bash

systemctl start sclbuilder-ui

while [[ 1 == 1 ]];
do
    echo "Check for updates"
    git fetch
    git status |grep "Your branch is behind"
    if [[ $? == 0 ]];
    then
        git pull
        systemctl restart sclbuilder-ui
    fi
    sleep 10
done

