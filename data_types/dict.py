# Dictionary basics
server = {
    "name": "server1",
    "ip":   "10.1.1.1",
    "status": "active"
}

print(f"server details: {server}")

##Access values
print(f"Name: {server['name']}")
print(f"IP: {server['ip']}")
print(f"Status: {server.get('status')}")
print(f"Location: {server.get('location', 'Not found')}")