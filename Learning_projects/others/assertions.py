def div(a, b):
    assert b != 0, "a is zero"
    return a / b

if __name__ == "__main__":
    print(div(1, 2))
    print(div(1, 0))