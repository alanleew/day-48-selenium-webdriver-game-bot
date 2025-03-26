import time

current_time = time.time()

# time.ctime() converts to human-readable format
print(time.ctime(current_time))

# Measuring execution time
start_time = time.time()
time.sleep(5)
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
