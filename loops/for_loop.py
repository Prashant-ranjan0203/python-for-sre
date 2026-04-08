servers = ["server1","server2","server3"]
for server in servers:
    print(server)
    print(type(server))


servers = ["app1","app2","db1"]
for server in servers :
    print(f"checking health of {servers}......")

server = {
    "server1": "running",
    "server2": "stopped",
    "server3": "running"

}

for name,status in server.items():
    if status == "running":
        print(f"{name} is UP")

    else:
        print(f"{name} is down")


# Break example
print("\n=== Break Example ===")
for server in servers:
    if server == "server2":
        print("Issue found! Stopping checks.")
        break
    print(f"{server} is OK")


# Continue example
print("\n=== Continue Example ===")
for server in servers:
    if server == "server2":
        continue
    print(f"Checking {server}")


# Range example
print("\n=== Retry Attempts ===")
for i in range(1, 6):
    print(f"Retry attempt {i}")