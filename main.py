import sys
import random

mod = 0
w = 0
x = 0

def main():
    x = w**2 % mod
    u = random.randint(1, mod - 1)
    y = u**3 % mod

    print(x, u, y)

    iteration = 0

    while iteration < random.randint(64, 1024):
        b = random.randint(0, 1)
        if b == 0:
            if u**2 % mod == y:
                print("{} Passed! Trust level {}".format(iteration, 1 - 2**(-iteration)) )
            else:
                print("Failed")
                exit(1)
        else:
            if ((w*u)**2 % mod) == (( x * y )% mod):
                print("{} Passed! Trust level {}".format(iteration, 1 - 2**(-iteration)) )
            else:
                print("Failed")
                exit(1)
        

        
        iteration += 1

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Module and Input required for operation")
        exit(1)
    
    
    mod = int(sys.argv[1])
    w = int(sys.argv[2])

    main()