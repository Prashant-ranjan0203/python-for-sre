# 🧠 Python Conditions Cheatsheet

## 🔹 Basic `if`

```python
cpu = 85

if cpu > 80:
    print("High CPU")
```

---

## 🔹 `if-else`

```python
disk = 40

if disk < 50:
    print("Low Disk")
else:
    print("Disk OK")
```

---

## 🔹 `if-elif-else`

```python
status_code = 500

if status_code == 200:
    print("OK")
elif status_code == 404:
    print("Not Found")
elif status_code == 500:
    print("Server Error")
else:
    print("Unknown")
```

---

## 🔹 Comparison Operators

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | Equal            |
| `!=`     | Not Equal        |
| `>`      | Greater than     |
| `<`      | Less than        |
| `>=`     | Greater or equal |
| `<=`     | Less or equal    |

---

## 🔹 Logical Operators

```python
cpu = 85
memory = 70

# AND
if cpu > 80 and memory > 75:
    print("Critical")

# OR
if cpu > 80 or memory > 75:
    print("Warning")

# NOT
is_down = False
if not is_down:
    print("Service is running")
```

---

## 🔹 Using `in` (very useful)

```python
log = "ERROR: DB down"

if "ERROR" in log:
    print("Issue found")
```

---

## 🔹 Dictionary + Condition

```python
servers = {
    "server1": "running",
    "server2": "stopped"
}

if "server1" in servers:
    if servers["server1"] == "running":
        print("Server is up")
```

---

## 🔹 One-line Condition (Ternary)

```python
cpu = 70
result = "High" if cpu > 80 else "Normal"
print(result)
```

---

## 🔹 Input Handling

```python
value = input("Enter value: ").strip().lower()
```

---

## 🔹 Error Handling (important)

```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input")
```

---

## 🔹 Best Practices

* Always clean input (`strip()`, `lower()`)
* Avoid too many `elif` → use dictionary when possible
* Handle invalid input
* Keep conditions simple and readable

---

## 🔹 SRE Use Cases

* CPU/Disk alerts
* Log error detection
* Service health checks
* API status validation

---

## 🚀 Example (Real SRE Style)

```python
cpu = 90
disk = 85

if cpu > 85 and disk > 80:
    print("Critical")
elif cpu > 85:
    print("CPU High")
elif disk > 80:
    print("Disk High")
else:
    print("Healthy")
```

---
