# Google Foo.Bar challenge level 1 - backwards and forwards

def palin(num_list):
    return num_list == num_list[::-1]

def convert(num, base):
    result = []
    temp = num
    while temp != 0:
        result = [temp % base] + result
        temp = temp / base
    return result

def answer(n):
    if n < 4:
        return 2
    # your code here
    for i in range(2, n):
        if i * 2 >= n:
            return n - 1
        result = convert(n, i)
        if palin(result):
            return i

if __name__ == "__main__":
    print answer(1000)