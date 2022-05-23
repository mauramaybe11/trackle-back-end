#!/bin/bash
ID='1'
TOKEN='5e89c360878d9e5e814a274134e396fc96f1c375'
GAME='wordle'
WORD='wings'
GUESSES='5'
AVERAGEGUESSES='6'
DATEGUESSED='2022-10-01'
curl "http://localhost:8000/logs/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "log": {
      "game": "'"${GAME}"'",
      "word": "'"${WORD}"'",
      "guesses": "'"${GUESSES}"'",
      "average_guesses": "'"${AVERAGEGUESSES}"'",
      "date_guessed": "'"${DATEGUESSED}"'"
    }
  }'

echo
