import hashlib
def solution(key, zero):

    n = 1
    prefix = zero * '0'

    while True:
        s = key + str(n)
        print(s)
        p = hashlib.md5(s.encode()).hexdigest()[:zero]
        if p == prefix:
            return n
        n += 1

answer = solution('iwrupvqb', 5)
print(answer)
