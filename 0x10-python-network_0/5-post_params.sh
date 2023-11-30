#!/bin/bash
# uses POST request on paseed URL and displys resp body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$"
