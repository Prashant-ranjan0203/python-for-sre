1. What are Data Types?
Data types define what kind of value a variable can store
x = 10        # int
name = "app"  # string


2. Categories of Data Types


Primitive (Single Value)
int
float
str
bool


Collection (Multiple Values)
list
tuple
set
dict

| Type  | Syntax | Ordered  | Mutable | Duplicates       | Indexing      | Use Case      |
| ----- | ------ | -------- | ------- | ---------------- | ------------- | ------------- |
| int   | 10     | ❌        | ❌       | ❌                | ❌             | counts        |
| float | 10.5   | ❌        | ❌       | ❌                | ❌             | metrics       |
| str   | "abc"  | ✅        | ❌       | ✅                | ✅             | logs          |
| bool  | True   | ❌        | ❌       | ❌                | ❌             | flags         |
| list  | []     | ✅        | ✅       | ✅                | ✅             | sequences     |
| tuple | ()     | ✅        | ❌       | ✅                | ✅             | fixed data    |
| set   | {1,2}  | ❌        | ✅       | ❌                | ❌             | unique values |
| dict  | {k:v}  | ✅ (3.7+) | ✅       | Keys ❌, Values ✅ | ❌ (uses keys) | mapping       |



4. Key Concepts (Must Know)

📌 Ordered vs Unordered

👉 Ordered = maintains position

lst = ["a", "b", "c"]
print(lst[0])  # a

👉 Unordered = no fixed position

s = {"a", "b", "c"}
# s[0] ❌ error

📌 Mutable vs Immutable

👉 Mutable = can change

lst = [1, 2]
lst.append(3)

👉 Immutable = cannot change

t = (1, 2)
# t[0] = 5 ❌
📌 Indexing

👉 Access element by position

lst = ["a", "b"]
print(lst[0])

✔ Available in: list, tuple, string
❌ Not in: set, dict

📌 Key-Based Access (Dict)
server = {"name": "app1"}
print(server["name"])


📌 Duplicates
lst = [1,1,2]     # allowed
s = {1,1,2}       # becomes {1,2}


5. Each Data Type Explained
📌 Integer (int)
x = 10

👉 Whole numbers
👉 Used in retries, counters

📌 Float
cpu = 75.5

👉 Decimal values
👉 Used in metrics

📌 String (str)
name = "server1"

👉 Text data
👉 Immutable

📌 Boolean (bool)
is_active = True

👉 True / False
👉 Used in conditions

📌 List
servers = ["app1", "app2"]

✔ Ordered
✔ Mutable
✔ Allows duplicates

👉 Best for:

Logs
Ordered steps
📌 Tuple
config = ("localhost", 8080)

✔ Ordered
❌ Immutable

👉 Best for:

Fixed configs
📌 Set
ips = {"10.1.1.1", "10.1.1.2"}

❌ Unordered
✔ Unique values only

👉 Best for:

Removing duplicates
Comparing data
⚠️ Empty Set Trap
a = {}       # dict ❌
b = set()    # set ✅
📌 Dictionary
server = {
    "name": "app1",
    "ip": "10.1.1.1"
}

✔ Key-value
✔ Fast lookup

👉 Best for:

Configs
API responses
🔥 6. Set Operations (Very Important)
a = {"a", "b"}
b = {"b", "c"}
a | b   # union → {'a','b','c'}
a & b   # intersection → {'b'}
a - b   # difference → {'a'}
🔥 7. Real SRE Use Cases
✅ Remove duplicate servers
servers = ["app1", "app2", "app1"]
unique = set(servers)
✅ Compare servers
s1 = {"app1", "app2"}
s2 = {"app2", "app3"}

print(s1 - s2)   # only in s1
✅ Store server info
server = {"name": "app1", "cpu": "80%"}
✅ Execution steps
steps = ["build", "test", "deploy"]
🔥 8. Important Terms (Interview Keywords)

👉 Memorize these:

Ordered
Unordered
Mutable
Immutable
Indexing
Key-value pair
Unique elements
Hashable
Iterable
Nested data structure
📌 Hashable (Advanced but Important)

👉 Required for:

set elements
dict keys

✔ Allowed:

{1, "a", (1,2)}

❌ Not allowed:

{[1,2]}   # list not hashable
📌 Iterable

👉 Can loop over

for x in [1,2,3]:
    print(x)

✔ list, tuple, set, dict, string

📌 Nested Data Structure
data = {
    "servers": ["app1", "app2"],
    "config": {"cpu": 2}
}


a = 5  
b = 5  
print(id(a) == id(b))