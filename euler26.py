#! /usr/bin/python3

def cyclelength(n):
    base = 10
    rem = 1
    rems = []
    while(rem not in rems):
        rems.append(rem)
        rem = rem*base % n
    return len(rems) - rems.index(rem)

if __name__ == "__main__":
    print("d={}".format(max(range(1,1000), key=cyclelength)))
    print("length of the cycle is: {}".format(cyclelength(983)))
