#!/bin/bash

curl "http://localhost:8000/mangos/" \
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
