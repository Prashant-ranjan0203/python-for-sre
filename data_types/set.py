# Simple Set Example for SRE Use Case

# List with duplicate servers (common in logs or files)
servers = ["web01", "web02", "web01", "web03", "web02"]
print("original list :")
print(servers)

# Convert list to set (removes duplicates)
unique_servers = set(servers)
print("\n Unique_servers (duplicates removed): ")
print(unique_servers)

# Example: Compare two environments
prod_servers = {"web01", "web02", "web03"}
staging_servers = {"web02", "web03"}

# Find missing servers in staging
missing_servers = prod_servers - staging_servers

print("\nServers missing in staging:")
print(missing_servers)

# Find common servers
common_servers = prod_servers & staging_servers

print("\nCommon servers in both environments:")
print(common_servers)


 #Notes 
# Union (all unique)
a | b

# Intersection (common items)
#a & b

# Difference (what's in a but not in b)
a - b