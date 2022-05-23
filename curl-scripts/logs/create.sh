#!/bin/bash
##sh curl-scripts/logs/create.sh
TOKEN='5e89c360878d9e5e814a274134e396fc96f1c375'
GAME='wordle'
WORD='viney'
GUESSES='6'
AVERAGEGUESSES='6'
DATEGUESSED='2022-10-01'
curl "http://localhost:8000/logs/" \
  --include \
  --request POST \
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
