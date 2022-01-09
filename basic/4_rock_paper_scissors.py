"""
這次的目標是要結合以前所有學過的東西，再加上這次教的東西，寫出剪刀石頭布的遊戲
這次要學的東西有3個，分別是import, while 跟 input
其中import是一個比較特別的東西，先把他拉出來講

import:
首先，import的功能其實是說，因為python這個程式語言他有一些內建(built-in)的函數可以用(這些函數其實可以想成已經被寫好的副程式
然後你把他import進來用而已)，像是之前學的range, print都是內建的函數，但還是會有些不方便，因為當初設計python的人不可能
把各種領域會用到的工具都寫好給你用，例如你如果要用很多數學的函數，像是cos或是sin，你要嘛自己寫出來sin跟cos，不然就可以
import一些大神寫好的程式進來用，這就是import的功能。

那這次我們就先import一個剪刀石頭布會用到的函數來示範，這裡的話其實還有一個議題是全域變數跟區域變數，但這裡就先不講
下次見面有機會再一起說，或是如果想知道，可以上網查查看
"""

def import_random():
    # 這裡我們import了一個叫做random的函數進來(這個也是python內建的函式)
    # 它的功能就跟他的名字一樣，可以隨機產生一些數字來，使用上就是用一個句點"."
    # 來提取它裡面的功能，這個示範就先用它裡面的功能randrange來介紹
    # 至於想要知道randrange的功能是甚麼就交給你上網查查看了，上網查某個想要的功能
    # 其實是我最常用的方式，也有另外一個方法就是把滑鼠移動到randrange上面，但不要按下去
    # 他自己會跳出來對於這個函數的註解，但這個就要看你使用的是甚麼軟體了，像是visual studio code
    # 是支援這個功能的，spider我就不確定了
    import random
    print(random.randrange(2))


"""
再來就是while loop了，while loop跟for loop其實很像，都是迴圈的一種
只是while loop變成是持續執行迴圈的內容，直到條件變成False為止，他的語法(syntax)如下
======while 的 語法======
while(條件):
    迴圈的內容
=====================
直接開看
"""
def while_loop():
    # 1. 將0賦值給一個變數counter
    # 2. while loop，跳出迴圈的條件為 (counter < 10)這件事情為False
    #    也就是說當counter == 0 or counter > 10的時候就會跳出迴圈
    # 3. print(f"")這個語法的意思其實也沒甚麼，就是原本如果你想要print
    #    一段字串 + 一個變數(以counter這個變數為例) + 另一段字串那這樣一般使用方法要用逗號隔開，像這樣
    #    print("一段字串", counter, "另一段字串")，可是這樣使用上要一直用逗號很麻煩也不直觀
    #    於是就有了print(f"")這個東西，它可以讓你在字串裡面print出變數，只是要放在大括號{}內
    #    所以就可以打成這樣print(f"一段字串 {counter} 另一段字串")，這樣就簡潔多了
    # 4. counter = counter + 1這裡稍微比較複雜一點點，但也還好，之前在說賦值都講得比較簡單，這裡在認真講一次
    #    其實像是counter = 0這件事情，步驟應該是先從等號右邊開始，創造一個數字0，而創造0這件事，
    #    其實你就是在記憶體的某一個地方寫進去0這個值，然後在記憶體的另外一個地方創造出一個變數counter，
    #    然後去找放0的記憶體位址在哪裡，最後把0賦值給counter。
    #    你可以想像成首先你先創造一號盒子，然後裡面放0這個值，之後你再創造二號盒子，裡面放counter這個變數
    #    最後再把一號盒子裡面的東西，丟給二號盒子裡面的東西，也就是把0這個數字丟給counter這個變數。
    #    那這樣如果有看懂的話整個式子 就應該好懂了，一樣先從counter=0開始，
    #    i. 創造一號盒子，裡面放0，再創造二號盒子裡面放counter，然後把一號盒子裡面的東西丟給二號盒子，結束
    #    ii. 看到counter = counter + 1，首先因為我們知道counter放在二號盒子裡面，那你現在創造一個三號盒子
    #       裡面放1，接著你把二號盒子的內容與三號盒子的內容相加(第一次執行迴圈應該會是 0 + 1)，然後再把他們
    #       的結果(1)放回去二號盒子，結束。
    #    如果真的看不懂的話，總之就是右邊先做，把counter + 1得到的結果塞回去counter裡面，這樣counter就會有+1的效果
    # 5. 執行完counter = counter + 1，基本上就完成了第一次迴圈的內容，接下來會重新判斷while的條件為何，這個時候
    #    counter的值應該是1(因為0+1)，那麼條件counter < 10 會是True，那就重新執行步驟3、步驟4，然後再判斷一次while的條件
    # 6. 當執行完第十次迴圈的時候，這時候counter的值會變成10，但注意print出來的東西只會是9，因為print在上面，counter = counter + 1
    #    在下面，接下來就會回去判斷while的條件，此時counter < 10會變成False，接下來就會跳出迴圈，我特別印出來counter的值給你看
    #    這裡要完全看懂哦! 這個小地方雖然很短，但是觀念很重要，
    #    小小練習一下，心裡想一下下面這個迴圈會執行幾次、會print甚麼出來，跳出迴圈之後counter的值會是多少，想好之後再去執行程式對答案看看
    #    x = 1
    #    y = 2
    #    while(x+y<10):
    #        y = y + 1
    #        print(f"x+y={x+y}")
    #    print("Get out of the while loop")
    #    print(f"x+y={x+y}")
    
    counter = 0
    while(counter < 10):
        print(f"counter: {counter}")
        counter = counter + 1
    print("Get out of the while loop")
    print(f"counter: {counter}")

"""
最後一個，開始進入與使用者互動的地方了!，就會開始好玩一點，不會那麼枯燥
這裡要介紹一個函數: input
基本上它的功能就是在Terminal(cmd，終端機，命令提示自元...隨便你叫)裡面，讓使用者輸入一個值
然後你可以在程式裡面以str(字串)的型態接收到使用者的輸入值，當然你也可以留言妳想要跟使用者說的東西
中英文都可以，但一般都會使用英文會比較不容易出錯，因為有些裝置是不支援中文的
在這裡你可以隨意輸入一些數字，英文、數字，甚至符號都可以
但一般是會希望能限制使用者輸入的東西的，不然不給使用者指示，讓他們亂輸入東西
大部分來講都會是一場災難，因為你不知道那群婊子到底會不會把你的程式玩炸
這時候就可以用一些手段來避免使用者亂輸入東西
開看程式
"""
def input_function():
    # 1. 開啟while迴圈，這裡條件直接放True，意思就是使用一個無限迴圈，她媽不管怎樣就是會一直跑裡面的內容，直到break
    #    break的功能就是只要執行到break就會強制跳出迴圈，對，是迴圈，意思就是不管是for迴圈或是while迴圈，遇到break都會
    #    直接跳出去
    # 2. 創造一個變數user_input用來接收使用者給的值
    # 3. 如果使用者給的值超過0到9的區間，那就嗆他然後進入下一次迴圈，重新叫使用者給我們一個值
    # 4. 如果使用者給的值在0到9的區間內，那就break，強制跳出迴圈
    # 5. 印出使用者給的值，以及他的type
    # 注意: 這裡要注意的是因為使用input函數取得的值都會被轉換成字串(str)，那如果要限制使用者給的值是數字的話，要自己轉換
    #       所以我才在if的條件裡面把str轉成int，這樣才可以用來比大小
    while(True):
        user_input = input("Please input a number between 0~9: ")
        if int(user_input) < 0 or int(user_input) > 9:
            print("Give me a number between 0~9 bitch")
        else:
            break

    print("Nice!")
    print(f"user_input: {user_input}, type of the user_input: {type(user_input)}")
input_function()
    

# 目前為止應該已經學了不少東西了，基本上你要製作剪刀石頭布的工具我全部都教了，接下來要出題目了
# 就是結合以前全部的東西，自己創造出來剪刀石頭布，下面會列出遊戲的條件，做出來之後傳給我 我會跟你說有沒有做錯
# 1. 總共比3次
# 2. 電腦會隨機出剪刀石頭布 hint: import random
# 3. 使用者要輸入能輸入剪刀石頭或布
# 4. 印出電腦出的東西以及使用者出的東西
# 5. 印出這次比賽的結果(平手，電腦贏，或是使用者贏，隨便你怎麼印，反正意思要到)
# 5. 比完三次之後，要印出結論是誰贏，使用者贏幾場，電腦贏幾場，平手幾場
# 6. 整個程式寫在一個.py檔內，並且使用副程式的方式寫，例如
"""
def 剪刀石頭布():
    內容
    內容
    內容
"""
# Good luck!，寫完傳給我