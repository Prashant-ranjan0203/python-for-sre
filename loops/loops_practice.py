server = {
    "server1" : "running",
    "server2" : "stopped",
    "server3" :  "running"
}

running_count = 0
stopped_count = 0
for name,status in server.items() :
    if status == "running":
        print(f"{name} is UP")
        running_count += 1

    else:
        stopped_count += 1
print(f"\nTotal running servers are : {running_count}")
print(f"Total stopped servers are : {stopped_count}")



#### Retry connection 
print(f"\nRetry connection method")
count =1
while count <= 5:
    print(f"Trying....Attempt{count}")
    count+=1


####break method 
print(f"\nUsing BREAK method")

servers = ["app1", "app2", "db1"]
for server in servers:
    if server == "app2":
        print(f"found {server}, stopping check")
        break
    print(f"checking {server}")
    


