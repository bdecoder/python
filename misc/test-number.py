def test_number(a):
    try:
        float(a)
        return True
    except ValueError:
        print'f"{a} isn't a number")
        exit()
