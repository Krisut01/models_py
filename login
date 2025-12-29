curl -X POST "http://localhost:5000/login" -H "Content-Type: application/json" -d '{"username":"testuser","password":"testpass123"}'

Response:
{"message":"Login successful","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3R1c2VyIiwiaWF0IjoxNzY2OTc0NDMyLCJleHAiOjE3NjcwNjA4MzJ9.nMPifSG4hHZfxG6aa1LR9GKFaA6ycoxrYEoi8Hkkw-Y"}
