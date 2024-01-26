#!/bin/bash
#cc
curl "$1" -sL -o /dev/null -w "%{http_code}"
