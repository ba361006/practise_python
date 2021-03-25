"""
今天來教if
首先 if 這個東西就很直白，就是如果條件為True的話，就做某一件事情，語法如下

======if 的 語法======
if 條件:
    要做的事情
=====================

為了複習一下第一次的內容(副程式)，我把每一段範例程式都寫成一個副程式，你們就照順序執行，然後看懂了就執行下一個
每個副程式裡面都有幫你們註解那個副程式在幹嘛
阿如果忘記副程式怎麼執行的話，可以把第15~17行複製下來，然後開啟一個新的.py檔案，貼上之後直接執行
你就會看到我對你的嘲諷

def subroutine():
    print("幹你娘")
subroutine()
"""

def if_practise_1():
    # 1.賦予一個變數x一個值1
    # 2.如果x這個變數大於0的話，就執行print("x比較大")
    x = 1
    if x > 0:
        print("x比較大")

def if_practise_2():
    # 當然也可以拿變數比變數
    # 1. 賦予一個變數x一個值1
    # 2. 賦予一個變數y一個值2
    # 3. 如果y比x大，就執行print("y比較大")
    x = 1
    y = 2
    if y > x:
        print("y比較大")
    # 當然，除了整數以外 小數跟負數也都可以拿來比，你們可以自己玩玩看

def if_practise_3():
    # 那如果不符合條件呢? 
    # 那就是直接跳過if，繼續往下執行剩下的程式
    x = 1
    y = 2
    if x > y:
        print("x比y大")
    print("宇智波跳過")


"""
if 進階:
到這裡應該知道if在幹嘛了，很直白，但這裡可以稍微提到一件事情就是
if的條件，其實本身是一個敘述(statement)，而這個變數它的型態比較常見的會是布林代數或是0跟1
聽不太懂的話可以看一下下面的例子
"""
def if_advance_practise():
    # if 進階練習:
    # 1. 賦予一個變數x一個值1
    # 2. 賦予一個變數y一個值2
    # 3. 賦予一個變數statement_1，x > y 的結果
    # 4. 賦予一個變數statement_2，y > x 的結果
    # 5. 把他們的型態用type()函數印出來，同時也印出他們的值
    x = 1
    y = 2
    statement_1 = x > y
    statement_2 = y > x
    print("type(statement_1):", type(statement_1), "statement_1: ", statement_1)
    print("type(statement_2):", type(statement_2), "statement_2: ", statement_2)

    # 接下來把它實際應用到if
    x = 1
    y = 2
    statement_1 = x > y
    statement_2 = y > x
    if statement_1:
        print("statement_1 is True")
    if statement_2:
        print("statement_2 is True")
    # 到這裡你會發現 print("statement_1 is True") 並沒有被印出來或者說被執行
    # 廢話，因為statement_1是False，在最一開頭有說到 if 的條件一定要是True，才會開始執行縮排的部分
    # 而這裡statement_2是False，所以其縮排的內容 print("statement_1 is True") 就不會被執行
    # 不信的話我們印出來看看 
    print(statement_1)



"""
除了if以外，還有一個很常搭配的用法就是else以及elif，我們一個一個講
而且通常if跟else是一個組合，是有連帶關係的，可以把它想像成他們是一個岔路口，如果不是if那就會跑到else，就只有兩條路走
那else是甚麼? else的意思其實就他媽的是字面上的意思，就是除了if以外，其他的東西
直接看程式就會懂了，簡單
"""

def else_practise():
    # 我懶得再一步一步寫說整個程式在幹嘛了，直接用敘述的
    # 阿就真的很直白，整個程式的過程就是，首先先看第一個if的條件 x > 1，阿你肯定知道這個敘述(statement)會是False
    # 那程式就不會進入 if x > 1:的縮排，接下來就是else發揮功能的時候了
    # 這個時候因為if x > 1的條件並沒有被滿足，也就是說你不能走if這條路，那你他媽就只能走else這條路了
    # 所以 print("x比較小") 才會被執行
    # 另外可以稍微注意一下就是else是不用有條件的，因為它其實就是在接收if以外的東西
    x = 1
    if x > 1:
        print("x比較大")
    else:
        print("x比較小")

"""
接下來講elif，他其實在其他程式語言，像是C++，被寫成else if，但python就很機掰硬要變成elif
他的想法稍微複雜一點但也還好，就很像是有二個條件一樣，首先會先判斷if的條件有沒有符合，不符合的話在判斷elif的條件
阿如果兩個都不符合的話，就會跟if_practise_3一樣，直接跳過這一對組合，繼續往下執行程式
"""
def elif_practise():
    x = 1
    y = 2
    if x > 1:
        print("x比1大")
    elif y > 2:
        print("y比2大")
    print("可憐那，兩個都不符合，就繼續執行程式")


"""
最後一部分就是if - elif - else 的組合，很好懂啦，只是再偷偷補充一件事情就是
if-elif-else其實是一個組合，如果有一個東西同時符合if的條件，也符合elif的條件的話
那他只會執行if的內容(因為順序的關係，先if再elif然後才是else)，當然通常是不會這樣設計啦
"""

def if_elif_else_practise():
    # 你可以試試看把2賦值給x，然後再把1賦值給x看看會怎樣
    x = 1
    if x > 2:
        print("x>1")
    elif x > 1:
        print("x>2")
    else:
        print("fucking else")


"""
好了我教完了 原本想讓你們寫個小題目的 但好像有點太多了 就下次吧
"""