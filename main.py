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

def 加法(x, y):
    return x + y
def 減法(x, y):
    return x - y
def 乘法(x, y):
    return x * y
def 除法(x, y):
    商數 = x // y
    餘數 = x % y
    return 商數, 餘數
while True:
    計算類型 = input("請輸入計算類型 (1)加 (2)減 (3)乘 (4)除: ")
    if 計算類型 in ("1", "2", "3", "4"):
        數字1 = int(input("請輸入第一個整數: "))
        數字2 = int(input("請輸入第二個整數: "))
        if 計算類型 == "1":
            print(f"{數字1} 加 {數字2} 等於 {加法(數字1, 數字2)}")
        elif 計算類型 == "2":
            print(f"{數字1} 減 {數字2} 等於 {減法(數字1, 數字2)}")
        elif 計算類型 == "3":
            print(f"{數字1} 乘 {數字2} 等於 {乘法(數字1, 數字2)}")
        else:
            if 數字1 % 數字2 == 0:
                print(f"{數字1} 除 {數字2} 等於 {除法(數字1, 數字2)[0]}")
            else:
                print(f"{數字1} 除 {數字2} 等於 {除法(數字1, 數字2)[0]} 餘 {除法(數字1, 數字2)[1]}")
    else:
        print("拜拜~")
        break;