"""多執行緒多程式模擬執行效率"""


from multiprocessing import Pool
from threading import Thread
import time, math


def simulation_IO(a):
    """模擬IO操作"""
    time.sleep(3)


def simulation_compute(a):
    """模擬計算密集型任務"""
    for i in range(int(1e7)):
        math.sin(40) + math.cos(40)
    return


def normal_func(func):
    """普通方法執行效率"""
    for i in range(4):
        func(i)
    return


def mp(func):
    """程式池中的map方法"""
    with Pool(processes=4) as p:
        res = p.map(func, list(range(4)))
    return


def asy(func):
    """程式池中的非同步執行"""
    with Pool(processes=4) as p:
        result = []
        for j in range(4):
            a = p.apply_async(func, args=(j, ))
            result.append(a)
        res = [j.get() for j in result]


def thread(func):
    """多執行緒方法"""
    threads = []
    for j in range(4):
        t = Thread(target=func, args=(j, ))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def showtime(f, func, name):
    """
    計算並展示函式的執行時間
    :param f: 多程式和多執行緒的方法
    :param func: 多程式和多執行緒方法中需要傳入的函式
    :param name: 方法的名字
    :return:
    """
    start_time = time.time()
    f(func)
    print(f"{name} time: {time.time() - start_time:.4f}s")


def main(func):
    """
    執行程式的主函式
    :param func: 傳入需要計算時間的函式名
    """
    # showtime(normal_func, func, "normal")
    # print()
    # print("------ 多程式 ------")
    # showtime(mp, func, "map")
    # showtime(asy, func, "async")
    # print()
    print("----- 多執行緒 -----")
    showtime(thread, func, "thread")


if __name__ == "__main__":
    print("------------ 計算密集型 ------------")
    func = simulation_compute
    main(func)
    print()
    print()
    print()
    print("------------ IO 密集型 ------------")
    func = simulation_IO
    main(func)