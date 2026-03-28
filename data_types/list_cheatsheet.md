# Python List Cheat Sheet (SRE)

Quick reference for Python list operations commonly used in automation and SRE scripts.

---

## Key Rules

1. Modify list → returns `None` (DO NOT assign)

```python
my_list.append("x")
my_list.extend(["a", "b"])
my_list.insert(1, "z")
my_list.remove("x")
my_list.sort()
my_list.reverse()
my_list.clear()
```

❌ Wrong:

```python
my_list = my_list.append("x")  # becomes None
```

---

### 2. Modify + return value

```python
item = my_list.pop()     # last item
item = my_list.pop(0)    # first item
```

---

### 3. Create new list → returns new object

```python
new_list = sorted(my_list)
new_list = my_list + ["x"]
new_list = my_list.copy()
```

---

## ⚡ Important Differences

### append vs +

```python
my_list.append("x")        # modifies same list
my_list = my_list + ["x"]  # creates new list
```

---

### sort vs sorted

```python
my_list.sort()             # modifies original
new_list = sorted(my_list) # new list
```

---

### remove vs pop

```python
my_list.remove("x")  # removes by value (no return)
my_list.pop()        # removes by index (returns value)
```

---

## 🧠 Why this matters

Using methods like `append()` incorrectly can break scripts:

```python
servers = ["srv1", "srv2"]

# ❌ Wrong
servers = servers.append("srv3")  # becomes None

# ✅ Correct
servers.append("srv3")
```

---

## 🚀 SRE Example

```python
servers = ["web1", "web2", "web3"]

failed = servers.pop()

print(f"Removed failed server: {failed}")
print(f"Active servers: {servers}")
```
