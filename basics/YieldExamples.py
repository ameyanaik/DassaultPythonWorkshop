def get_data():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

print(get_data())
print(next(get_data()))
print(next(get_data()))

for i in get_data():
    print(i)


def find_if_prime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

# Get All Prime Numbers upto a certain number
def get_all_prime_before(n):
    for i in range(1, n+1):
        result = find_if_prime(i)
        if result == True:
            yield i

result = get_all_prime_before(12)
print("Prime numbers: ", next(result), end=" ")
print(next(result), end=" ")
print(next(result), end=" ")
print(next(result), end=" ")
print(next(result), end=" ")
print(next(result), end=" ")
print()

for prime in get_all_prime_before(100):
    print(prime, end=' ')

