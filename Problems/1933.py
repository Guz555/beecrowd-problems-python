pos = int(input())

if pos <= 100:
    res = "Top 100"
if pos <= 50:
    res = "Top 50"
if pos <= 25:
    res = "Top 25"
if pos <= 10:
    res = "Top 10"
if pos <= 5:
    res = "Top 5"
if pos <= 3:
    res = "Top 3"
if pos == 1:
    res = "Top 1"

print(res)
