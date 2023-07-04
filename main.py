### https://www.youtube.com/watch?v=8UHmhfnUIRo&list=PL7enJ2-v6SPk5vrrzV_f0QJy7bDa06vI5&index=4

### 第二集
# 午餐 = 100
# 晚餐 = 150
# 一周餐費 = (午餐 + 晚餐) * 7
# print(一周餐費)
# print(type(一周餐費))
#
# 月生活費 = 16000
# 日平均 = 月生活費 // 30
# print(日平均)
# print(type(月生活費 / 30))
#
# print(type("YOYO"))
#
# print("""
# 第一行
# 第二行
# 第三行
# """)

# _name = input("請輸入你的姓名: ")
# _year = input("請輸入你的出生年: ")
# _age = 2023 - int(_year)
# print("你好，" + str(_age) + " 歲的 " + _name)
# print(f"你好，{_age} 歲的 {_name}")

### 第3集

# 牛排 = 500
# 豬排 = 450
# 魚排 = 400
# 套餐 = 80
#
# print(not 牛排 == 豬排 and 豬排 < 魚排)
# print(not 牛排 == 豬排 or 豬排 < 魚排)
# 餐點 = input("請問你要點什麼餐點? (A)牛排 (B)豬排 (C)魚排 :").upper()
# 升級 = input("你是否要升級套餐? (Y)是 (N)否 :").upper()
#
# if 餐點 == "A":
#     if 升級 == "Y":
#         print(f"牛排套餐的費用是{牛排 + 套餐}")
#     else:
#         print(f"牛排的費用是{牛排}")
# elif 餐點 == "B":
#     if 升級 == "Y":
#         print(f"豬排的費用是{豬排 + 套餐}")
#     else:
#         print(f"豬排的費用是{豬排}")
# else:
#     if 升級 == "Y":
#         print(f"魚排的費用是{魚排 + 套餐}")
#     else:
#         print(f"魚排的費用是{魚排}")


### 第4集

# 學生List = ["阿明", "阿華", "阿強", "阿珍"] # 跟前端的陣列一樣
# 學生Tuple = ("阿明", "阿華", "阿強", "阿珍") # 資料不可變更及增減的陣列
# 唐詩 = "床前明月光"
# 日期 = "2022/12/1"
#
# print(len(學生List))
# print(len(唐詩))
# print(list(唐詩))
# print(日期.split("/"))
# print("/".join(學生List))
#
# 學生List.append("阿美")
# print(學生List)
#
# 學生Test = ["阿怡", "阿靜"]
# 學生List.extend(學生Test)
# print(學生List)
#
# 學生List.remove("阿華")
# print(學生List)
#
# 學生List.pop(0)
# print(學生List)

# 學生姓名 = input("請問想找哪位學生?")
# if 學生姓名 in 學生List:
#     print(f"{學生姓名}同學座號為{學生List.index(學生姓名)}")
# else:
#     print("班級裡沒有這號學生")

# 成績系統 = ["阿明", 82, "阿強", 94, "阿花", 85]
# print(成績系統)
# 操作 = input("請輸入操作指令 (A)查詢 (B)新增 (C)刪除 (D)修改 :").upper()
#
# if 操作 == "A":
#     姓名 = input("請輸入要查詢的姓名: ")
#     if 姓名 not in 成績系統:
#         print("班級裡沒有這號同學")
#     else:
#         print(f"{姓名}同學的成績為{成績系統[成績系統.index(姓名) + 1]}")
#
# elif 操作 == "B":
#     學生資料 = input("請輸入要新增的姓名/成績: ")
#     成績系統.extend(學生資料.split("/"))
#     print(f"成績新增完畢，目前已登錄的學生人數為{len(成績系統)//2}人")
#
# elif 操作 == "C":
#     姓名 = input("請輸入要刪除的姓名: ")
#     if 姓名 not in 成績系統:
#         print("班級裡沒有這號同學")
#     else:
#         姓名位置 = 成績系統.index(姓名)
#         成績系統.pop(姓名位置)
#         成績系統.pop(姓名位置)
#         print(成績系統)
#
# else:
#     姓名成績 = input("請輸入要修改的姓名/成績: ")
#     姓名 = 姓名成績.split("/")[0]
#     成績 = 姓名成績.split("/")[1]
#     if 姓名 not in 成績系統:
#         print("班級裡沒有這號同學")
#     else:
#         成績系統[成績系統.index(姓名) + 1] = int(成績)
#         print(成績系統)


### 第5集

# 早餐 = ["蛋餅", "三明治", "漢堡", "飯糰"]
# 飲料 = ["豆漿", "紅茶", "奶茶"]
# 數量 = 0
#
# for 餐點 in 早餐:
#     if 餐點 == "漢堡":
#         continue;
#     print(餐點)
#
# for 文字 in "早餐店":
#     print(文字)
#
# for 餐點 in 早餐:
#     for 飲品 in 飲料:
#         print(f"{餐點}配{飲品}")
#         數量 += 1
#         print(f"總共有{數量}種套餐組合")

# 數列 = [1, 2, 3, 4, 5, 6]
# 正負數列 = [1, -2, 3, -4, 5, -6]
# 乘積 = 1
# 清單 = []
# 正數 = []
# 負數 = []
#
# for 數字 in 數列:
#     乘積 *= 數字
# print(乘積)
#
# for 數字 in 數列:
#     if 數字 > 3:
#         清單.append(數字)
# print(清單)
#
# for 數字 in 正負數列:
#     if 數字 > 0:
#         正數.append(數字)
#     else:
#         負數.append(數字)
# print(f"正數為{正數}, 負數為{負數}")

# for x in range(5, 10, 2): # 開始值 結束值 間距值
#     print(x)

# 正確密碼 = "1234"
# for 次數 in range(5):
#     密碼 = input("請輸入密碼: ")
#     if 密碼 == 正確密碼:
#         print("密碼正確")
#         break;
#     elif 密碼 != 正確密碼 and 次數 <4:
#         print("密碼不正確，請重新輸入")
#         print(f"您還剩下{4-次數}次機會")
#     else:
#         print("密碼錯誤過多，帳號已被鎖定")


### 第6集 while先不學

# while True:
#     x = input("請輸入一個數字: ")
#     if x == "不玩了":
#         print("再見")
#         break
#     else:
#         print(x)

# 數字 = 1
# while 數字 <= 5:
#     print(數字)
#     數字 += 1

# 早餐 = ["蛋餅", "三明治", "漢堡", "飯糰"]
# 編號 = 0
# while 編號 < len(早餐):
#     print(早餐[編號])
#     編號 += 1

# 商品價格 = 1000
# A = input("請輸入第一位玩家的暱稱: ")
# B = input("請輸入第二位玩家的暱稱: ")
# 回答次數 = 1
# 總次數 = 5
# # while True:
# while 回答次數 <= 總次數:
#     A答 = int(input(f"請{A}輸入商品金額: "))
#     B答 = int(input(f"請{B}輸入商品金額: "))
#     if A答 == 商品價格 or B答 == 商品價格:
#         break;
#     elif abs(商品價格 - A答) < abs(商品價格 - B答):
#         print(f"{A}更接近")
#     else:
#         print(f"{B}更接近")
#
#     回答次數 += 1
# if A答 == 商品價格:
#     print(f"{A}猜對了!{A}獲勝")
# elif B答 == 商品價格:
#     print(f"{B}猜對了!{B}獲勝")
# elif abs(商品價格 - A答) < abs(商品價格 - B答):
#     print(f"遊戲結束! 正確價格為{商品價格}，{A}更接近，{A}獲勝")
# else:
#     print(f"遊戲結束! 正確價格為{商品價格}，{B}更接近，{B}獲勝")

### 第7集

# def 打印(_name, _age):
#     print(f"{_name}今年是{_age}歲")
#
# 打印(_age = 18, _name = "Nains")
#
# def Total(售價, 運費 = 50):
#     global 折扣 # global可將區域變數升級為全域變數
#     折扣 = 0.9
#     return int(售價 * 折扣 + 運費)
# print(f"總金額為 {Total(1000, 80)}元")

# def 加法(x, y):
#     return x + y
# def 減法(x, y):
#     return x - y
# def 乘法(x, y):
#     return x * y
# def 除法(x, y):
#     商數 = x // y
#     餘數 = x % y
#     return 商數, 餘數
#
# while True:
#     計算類型 = input("請輸入計算類型 (1)加 (2)減 (3)乘 (4)除: ")
#     if 計算類型 in ("1", "2", "3", "4"):
#         數字1 = int(input("請輸入第一個整數: "))
#         數字2 = int(input("請輸入第二個整數: "))
#         if 計算類型 == "1":
#             print(f"{數字1} 加 {數字2} 等於 {加法(數字1, 數字2)}")
#         elif 計算類型 == "2":
#             print(f"{數字1} 減 {數字2} 等於 {減法(數字1, 數字2)}")
#         elif 計算類型 == "3":
#             print(f"{數字1} 乘 {數字2} 等於 {乘法(數字1, 數字2)}")
#         else:
#             if 數字1 % 數字2 == 0:
#                 print(f"{數字1} 除 {數字2} 等於 {除法(數字1, 數字2)[0]}")
#             else:
#                 print(f"{數字1} 除 {數字2} 等於 {除法(數字1, 數字2)[0]} 餘 {除法(數字1, 數字2)[1]}")
#     else:
#         print("拜拜~")
#         break;

### 第8集

# 手機 = {
#     "廠牌" : "蘋果",
#     "型號" : "iPhone 14 Pro",
#     "容量" : "512 GB",
#     "顏色" : "深藍色"
# }
# print(手機.get("顏色", "查無此選項"))
# 手機["顏色"] = ["深藍色", "銀色", "黑色"]
# print(手機["顏色"][0])
# 手機.pop("廠牌") # 指定key刪除
# 手機.popitem() # 刪除最後一項
# 手機.clear() # 全部清空

# for 規格 in 手機.keys():
#     print(規格)
# for 規格 in 手機.values():
#     print(規格)
# for 標題, 規格 in 手機.items():
#     print(f"{標題} 為 {規格}")

# 手機1 = {
#     "廠牌" : "蘋果",
#     "型號" : "iPhone 14 Pro",
#     "容量" : "512 GB",
#     "顏色" : "深藍色"
# }
# 手機2 = {
#     "廠牌" : "小米",
#     "型號" : "12 Pro 5G",
#     "容量" : "256 GB",
#     "顏色" : "銀色"
# }
# 手機3 = {
#     "廠牌" : "三星",
#     "型號" : "Galaxy S22 Ultra",
#     "容量" : "256 GB",
#     "顏色" : "夜幕紅"
# }
# 庫存 = [手機1, 手機2, 手機3]
# 查詢 = input("請輸入要查詢的廠牌名稱: ")
# if 查詢 in str(庫存):
#     for 手機 in 庫存:
#         if 手機["廠牌"] == 查詢:
#             print(f"目前庫存中有{手機['顏色']}的{手機['型號']}，容量是{手機['容量']}")
# else:
#     print(f"目前沒有{查詢}手機的庫存")


### 第九集

# import my_module as hello
# hello.打招呼("Nains")
# from my_module import 打招呼
# 打招呼("Nains")

# import random
# 數字 = [1,2,3,4,5,6]
# random.shuffle(數字) # 將陣列隨機排列
# print(數字)
# a = random.choice(數字) # 隨機抽一個數字
# print(a)
# b = random.randint(10, 50) # 在自定義範圍內隨機抽選一個數字
# print(b)

# import random
# import string
#
# 數字 = string.digits  # digits可產生0到9的數字
# 英文 = string.ascii_letters  # ascii_letters可產生英文大小寫的字母
# 字母表 = list(數字 + 英文)
# random.shuffle(字母表)
# 長度 = int(input("你的密碼要幾位數? "))
# 密碼 = "".join(字母表[: 長度])
# print(f"您的密碼為: {密碼}")

# import requests
# 城市 = input("請輸入要查詢城市名稱: ")
# API = "313f95ca0c819881fd7ed8b662a38abd"
# 網站 = f"https://api.openweathermap.org/data/2.5/weather?q={城市}&appid={API}"
# 天氣資料 = requests.get(網站)
# 氣溫 = int(天氣資料.json()["main"]["temp"] - 273.15)
# 天氣 = 天氣資料.json()["weather"][0]["main"]
# 濕度 = 天氣資料.json()["main"]["humidity"]
# 風速 = 天氣資料.json()["wind"]["speed"]
# print(f"{城市}目前的氣溫為{氣溫}")
# print(f"天氣: {天氣}")
# print(f"濕度: {濕度}%")
# print(f"風速: {風速} (單位：米/秒)")

### 第十集
# class 遊戲角色:
#     等級 = 1
#     經驗值 = 0
#     def __init__(self, 姓名, 年齡):
#         self.姓名 = 姓名
#         self.年齡 = 年齡
#     def 衝鋒(self):
#         print(f"{self.姓名}一個箭步衝向了敵人!")
#     def 洞察(self):
#         print(f"{self.姓名}用敏銳眼光環顧著四周")
#
# class 戰士(遊戲角色):
#     def 攻擊(self):
#         print(f"{self.姓名}使出突刺攻擊!")
#
# 玩家1 = 戰士("小明", 24)
# 玩家2 = 遊戲角色("小華", 22)
# 玩家1.攻擊()
# 玩家1.洞察()
# 玩家2.衝鋒()

import random
class 遊戲角色:
    生命 = 500
    def __init__(self, 姓名):
        self.姓名 = 姓名

    def 防禦(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}成功格擋 ~")
            return 0.5
        elif 指令 == 2:
            閃避機率 = random.choice([0, 1])
            if 閃避機率 == 0:
                print(f"{self.姓名}成功閃避 ~")
                return 0
            else:
                print(f"{self.姓名}閃避失敗 ~")
            return 1

class 戰士(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出突刺攻擊!")
            return 200
        elif 指令 == 2:
            print(f"{self.姓名}奮力使出迴旋揮砍")
            return  random.choice([300, 100])


class 魔物(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f"{self.姓名}使出利爪攻擊!")
            return 180
        elif 指令 == 2:
            print(f"{self.姓名}張口使用毒液")
            return  random.choice([320, 100])


玩家姓名 = input("請輸入角色名稱: ")
玩家 = 戰士(玩家姓名)
敵方 = 魔物("哥布林")

while True:

    隨機 = random.choice([1, 2])

    玩家指令 = int(input("請輸入您的攻擊指令 (1)普通攻擊 (2)特殊攻擊 :"))
    玩家攻擊力 = 玩家.攻擊(玩家指令)
    扣血 = int(敵方.防禦(隨機) * 玩家攻擊力)
    敵方.生命 -= 扣血

    if 敵方.生命 <= 0:
        print(f"{敵方.姓名}倒下了，{玩家.姓名}勝利!!")
        break
    else:
        print(f"{敵方.姓名}受到了{扣血}傷害! 生命值剩下{敵方.生命}")
        print("")

    防禦指令 = int(input("請輸入您的防禦指令 (1)格擋 (2)閃避 :"))
    敵方攻擊力 = 敵方.攻擊(防禦指令)
    損血 = int(玩家.防禦(隨機) * 敵方攻擊力)
    玩家.生命 -= 扣血

    if 敵方.生命 <= 0:
        print(f"{玩家.姓名}受傷過重，遊戲結束!!")
        break
    else:
        print(f"{玩家.姓名}受到了{損血}傷害! 生命值剩下{玩家.生命}")
        print("")