
def count_down(time):
    if time < 0:
        print('times up')
        return 0
    print('count  ', time)
    time = time - 1

    count_down(time)


count_down(6)
