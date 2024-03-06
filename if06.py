def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a=n//10000
    b=(n//1000)%10
    c=(n//100)%10
    d=(n%100)//10
    x=(n%100)%10
    if a>b and a>c and a>d and a>x:
        return 5
    if b>a and b>c and b>d and b>x:
        return 4
    if c>a and c>b and c>d and c>x:
        return 3
    if d>a and d>b and d>c and d>x:
        return 2
    if x>a and x>b and x>c and x>d:
        return 1
    
    
    
print(main(23951))