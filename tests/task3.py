# ( годовой процент / 12 * основная сумма + основная сумма)
# На вход программа должна получать сумму депозита, желаемую конечную сумму и годовой процент.
# На выходе должно выдаваться количество месяцев нужных для накопления этой суммы при этом в годовом проценте.

sum = 1000000
wish = 10000000
proc = 12
w = (proc / 10 / 12 * sum + sum)
print(w)

while wish > 0:
    wish = 10000000
    wish = (proc / 10 / 12 * w + w)
    if wish == 10000000:
        break
    print(wish - w)