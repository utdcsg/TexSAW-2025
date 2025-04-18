admin_password="supersecret102394809823509812039840920100101039488482093dflksjfljthispasswordrocks"
curl -X POST http://127.0.0.1:5000/register \
     -H "Content-Type: application/json" \
     -d "{\"key\": \"$1\", \"name\": \"$2\", \"password\": \"$admin_password\"}"
