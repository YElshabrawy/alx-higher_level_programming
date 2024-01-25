#!/bin/bash

curl -sI "$1" | grep -i Allow | awk -F': ' '{print $2}'
