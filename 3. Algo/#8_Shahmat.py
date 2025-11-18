def max_chesspieces(problem_count, problems):
    f = problems[0][0]
    n = problems[0][1]
    m = problems[0][2]
    f2 = problems[1][0]
    n2 = problems[1][1]
    m2 = problems[1][2]
    if f == "r":
        print(min(m, n))
    elif f == "k":
        return ((m*n)//2)
    elif f == "Q":
        return (min(m, n))
    elif f == "K":
        return ((abs(int(n)/2)) * (abs(int(m)/2)))
        
    if f2 == "r":
        return (min(n2, m))
    elif f2 == "k":
        return ((n2*m2)//2)
    elif f2 == "Q":
        return (min(n2, m2))
    elif f2 == "K":
        return ((abs(int(n2)/2)) * (abs(int(m2)/2)))
    
    
problem_count = 2
problems = [('r', 4, 4), ('Q', 8, 8)]
result = max_chesspieces(problem_count, problems)
print(result)