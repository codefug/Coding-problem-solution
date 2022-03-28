def lcm(m, n):
    M=m
    N=n
    while M!=N:
        if M<N:
            M*=m
        elif M>N:
            N*=n
    return M


a = int(input('a = '))
b = int(input('b = '))
print('최소공배수 : ', lcm(a, b))
