#sh curl-scripts/logs/delete.sh
#!/bin/bash
TOKEN='5e89c360878d9e5e814a274134e396fc96f1c375'
ID='1'
curl "http://localhost:8000/logs/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
