# Simple Set Example for SRE Use Case

# List with duplicate servers (common in logs or files)
servers = ["web01", "web02", "web01", "web03", "web02"]
print("original list :")
print(servers)

# Convert list to set (removes duplicates)
unique_servers = set(servers)
print("\n Unique_servers (duplicates removed): ")
print(unique_servers)