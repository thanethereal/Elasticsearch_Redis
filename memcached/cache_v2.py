import functools
import sqlite3
import time
from random import *

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

@functools.lru_cache(maxsize=None)
def execute_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def execute_query_without_cache(query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# for i in range(10000, 20000):
#     print(i)
#     name = f"Employee {i+1}"  
#     age = randint(20, 40)
#     query = f"INSERT INTO employees (name, age) VALUES ('{name}', {age})"
#     result = execute_query(query)
#     conn.commit()

# Thực hiện truy vấn đếm số lượng dữ liệu
query = "SELECT COUNT(*) FROM employees"
cursor.execute(query)
count = cursor.fetchone()[0]

# In ra số lượng dữ liệu
print(f"Data number: {count}")

# Ví dụ sử dụng câu truy vấn SELECT với age = 30 
age = 30
query = f"SELECT * FROM employees WHERE age = {age}"
result = execute_query(query)

# Ví dụ sử dụng câu truy vấn SELECT với age = 20 
age = 20
query = f"SELECT * FROM employees WHERE age = {age}"
result = execute_query(query)

# Ví dụ sử dụng câu truy vấn SELECT với age = 40 
age = 40
query = f"SELECT * FROM employees WHERE age = {age}"
result = execute_query(query)

# Ví dụ sử dụng câu truy vấn SELECT với cache
start_time_with_cache = time.time()
age = 30
query = f"SELECT * FROM employees WHERE age = {age}"
result = execute_query(query)
end_time_with_cache = time.time()
execution_time_with_cache = end_time_with_cache - start_time_with_cache
print(f"Execution time with cache: {execution_time_with_cache} seconds")

# In thông tin cache ra file txt
with open('cache_info.txt', 'w') as f:
    cache_info = execute_query.cache_info()
    print(f"Cache hits: {cache_info.hits}", file=f)
    print(f"Cache misses: {cache_info.misses}", file=f)
    print(f"Cache size: {cache_info.currsize}", file=f)

# Ví dụ sử dụng câu truy vấn SELECT không có cache
start_time_without_cache = time.time()
age = 30
query = f"SELECT * FROM employees WHERE age = {age}"
result = execute_query_without_cache(query)
end_time_without_cache = time.time()
execution_time_without_cache = end_time_without_cache - start_time_without_cache
print(f"Execution time without cache: {execution_time_without_cache} seconds")