# Patient 1
# FIXED: range(1, 10) stops before 10, so it was changed to range(1, 11).
for i in range(1, 11):
    print(i)


# Patient 2
n = 3

# FIXED: The loop was infinite because n was never decreased. Subtracting 1 makes the loop eventually stop.
while n > 0:
    print(n)
    n = n - 1


# Patient 3
total = 0

# FIXED: total was reset to 0 inside the loop. It must be initialized before the loop so the running total is preserved.
for i in range(1, 6):
    total = total + i

print(total)
