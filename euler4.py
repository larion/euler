#! /usr/bin/python

def palindrome(no):
    return all(str(no)[n] == str(no)[-n-1] for n in range(len(str(no))))

results = []

for i in range(999,99,-1):
    for i2 in range(999,99,-1):
        if palindrome(i*i2):
            results.append(i*i2)
            break

print results

print "-----"

print max(results)
