#!/bin/bash
# send a POST request to the passed URL, and display the body of the response
curl -sLX POST "$1" -H "email: test@gmail.com" -H "subject: I will always be here for PLD"
