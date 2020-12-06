from multiprocessing import Pool
from multiprocessing import Process

list = []

def function(hoge):
    #やりたいこと
    global list
    list = list + [hoge]
    return list

def multi(n):
    p = Pool(10) #最大プロセス数:10
    result = p.map(function, range(n))

    return result

def main():
    datas = multi(20)
    for data in datas:
        print(data)

main()
