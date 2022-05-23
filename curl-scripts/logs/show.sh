#!/bin/bash
ID='1'
TOKEN='5e89c360878d9e5e814a274134e396fc96f1c375'
curl "http://localhost:8000/logs/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
