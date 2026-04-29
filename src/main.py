print("Name : Masud Ibn Musa")
print("Date : 29-04-2026")

from utils import add, subtract, divide , multiply

result_add = add(10, 5)
result_sub = subtract(10, 5)

print(f"Addition of 10 + 5 = {result_add}")
print(f"Subtraction of 10 - 5 = {result_sub}")

print("Division (10 * 2):", multiply(10, 2))

print("Division (10 / 2):", divide(10, 2))
print("Division (10 / 0):", divide(10, 0))