#coding:utf-8


# 获取任意位数的斐波那契额数列
def get_fibonacci_list(num):
    front = 0
    back = 1

    i = 1
    while i <= num:
        yield back
        front, back = back, front + back
        i += 1


def main():
    num = 10
    faibonacci_list = [element for element in get_fibonacci_list(num)]
    print faibonacci_list

if __name__ == '__main__':
    main()