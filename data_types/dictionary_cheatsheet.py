# ==============================
# PYTHON DICTIONARY CHEATSHEET
# ==============================

# 1. Create dictionary
server = {
    "name": "web01",
    "ip": "10.0.0.1",
    "status": "running"
}

# 2. Access values
print(server["name"])            # direct (KeyError if missing)
print(server.get("ip"))          # safe access
print(server.get("os", "linux")) # default value

# 3. Add / Update values
server["env"] = "prod"           # add new key
server["status"] = "stopped"     # update existing key

# 4. Delete values
del server["ip"]                 # delete key
server.pop("env", None)          # safe delete

# 5. Loop through dictionary
for key in server:
    print(key)                  # keys

for value in server.values():
    print(value)                # values

for key, value in server.items():
    print(key, value)           # key-value pairs

# 6. Check if key exists
if "name" in server:
    print("Key exists")

# 7. Dictionary length
print(len(server))

# 8. Nested dictionary
servers = {
    "web01": {"ip": "10.0.0.1", "status": "running"},
    "web02": {"ip": "10.0.0.2", "status": "stopped"}
}

print(servers["web01"]["ip"])

# 9. Copy dictionary
new_server = server.copy()

# 10. Update dictionary
server.update({"region": "us-east"})

# 11. Clear dictionary
# server.clear()

# 12. Get all keys, values, items
print(server.keys())
print(server.values())
print(server.items())