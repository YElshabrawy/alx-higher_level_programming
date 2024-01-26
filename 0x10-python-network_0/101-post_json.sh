#!/bin/bash
# dd
curl -X POST "$1" -d @"$2" -H "Content-Type: application/json"
