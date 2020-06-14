#Huy Tran
#Catalan method
def catalan(n):
    if n <= 0:
        return 1

    result = 0
    for i in range(n):
        result += catalan(i) * catalan(n-i-1)

    return result

