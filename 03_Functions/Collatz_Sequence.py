try:
    def collatz(n):
        if n%2==0:
            return n//2
        elif n%2!=0:
            return 3*n+1
    
    num = int(input("input an integer: "))
    x = collatz(num)
    print(x)
    while True:
        x = collatz(x)
        if x == 1:
            break
        print(x)
        
except ValueError:
    print("Enter a valid INTEGER")

