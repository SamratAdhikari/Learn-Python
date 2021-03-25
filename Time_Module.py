import time

k = 0
initial = time.time()
print(initial)

while k<10:
    print("This is Samrat.")
    # time.sleep(2)
    k += 1
print(f"While Loop ran in {time.time() - initial} seconds.")

initial2 = time.time()
for i in range(10):
    print("This is Samrat.")
print(f"For Loop ran in {time.time() - initial2} seconds.")
print()
print()
print()
print()
time.sleep(3)

localtime = time.asctime()
print(localtime)
