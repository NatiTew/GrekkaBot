import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="-")

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

status = ['N', 'HP','att', False]
n1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
h1 = [[1, 125, 0, False], [12, 5, 0, False], [50, 2, 0, False], [6, 4, 0, False], [32, 2, 0, False], [60, 1, 0, False], [1, 10, 0, False], [16, 1, 0, False], [16, 1, 0, False], [5, 4, 0, False]]
h2 = [8, 2]
h3 = [8, 2]
h4 = [5, 2]
h5 = [10, 1]
p1 = [[]]
p2 = [[]]
p3 = [[]]
p4 = [[]]
arr = [[]]
arr2 = [[]]
arr3 = [[]]
arr4 = [[]]
arrB = [[]]
arr2B = [[]]
arr3B = [[]]
arr4B = [[]]
statusBot = False

@client.command()
async def start(ctx, player1: int, player2: int):
    global arr
    global arr2
    global arrB
    global arr2B
    global statusBot

    if(statusBot == False):
        arr = [[0 for k in range(len(status))] for l in range(player1)]
        arrB = [[0 for k in range(len(status))] for l in range(player1)]
        print(arr)
        arr2 = [[0 for k in range(len(status))] for l in range(player2)]
        arr2B = [[0 for k in range(len(status))] for l in range(player2)]
        print(arr2)
        await ctx.send("โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3")
        await ctx.send("1 คือ ผู้เล่น")
        await ctx.send("2 คือ ตำแหน่งตัวละคร")
        await ctx.send("A3 คือ รหัสตัวละคร")
        statusBot = True
    else:
        await ctx.send("เกมส์เริ่มไปแล้ว โปรด Reset")

@client.command()
async def reset():
    global arr
    global arr2
    global arr3
    global arr4
    global arrB
    global arr2B
    global arr3B
    global arr4B
    global statusBot

    arr = [[]]
    arr2 = [[]]
    arr3 = [[]]
    arr4 = [[]]
    arrB = [[]]
    arr2B = [[]]
    arr3B = [[]]
    arr4B = [[]]
    statusBot = False
    await ctx.send("Reset เรียบร้อย")

@client.command()
async def start3(ctx, player1: int, player2: int, player3: int):

    global arr
    global arr2
    global arr3
    global arrB
    global arr2B
    global arr3B
    global statusBot

    if (statusBot == False):
        arr = [[0 for k in range(len(status))] for l in range(player1)]
        arrB = [[0 for k in range(len(status))] for l in range(player1)]
        print(arr)
        arr2 = [[0 for k in range(len(status))] for l in range(player2)]
        arr2B = [[0 for k in range(len(status))] for l in range(player2)]
        print(arr2)
        arr3 = [[0 for k in range(len(status))] for l in range(player3)]
        arr3B = [[0 for k in range(len(status))] for l in range(player3)]
        print(arr3)
        await ctx.send("โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3")
        await ctx.send("1 คือ ผู้เล่น")
        await ctx.send("2 คือ ตำแหน่งตัวละคร")
        await ctx.send("A3 คือ รหัสตัวละคร")
        statusBot = True
    else:
        await ctx.send("เกมส์เริ่มไปแล้ว โปรด Reset")

@client.command()
async def start4(ctx, player1: int, player2: int, player3: int, player4: int):

    global arr
    global arr2
    global arr3
    global arr4
    global arrB
    global arr2B
    global arr3B
    global arr4B

    arr = [[0 for k in range(2)] for l in range(player1)]
    arrB = [[0 for k in range(2)] for l in range(player1)]
    print(arr)
    arr2 = [[0 for k in range(2)] for l in range(player2)]
    arr2B = [[0 for k in range(2)] for l in range(player2)]
    print(arr2)
    arr3 = [[0 for k in range(2)] for l in range(player3)]
    arr3B = [[0 for k in range(2)] for l in range(player3)]
    print(arr3)
    arr4 = [[0 for k in range(2)] for l in range(player4)]
    arr4B = [[0 for k in range(2)] for l in range(player4)]
    print(arr4)
    await ctx.send("โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3")
    await ctx.send("1 คือ ผู้เล่น")
    await ctx.send("2 คือ ตำแหน่งตัวละคร")
    await ctx.send("A3 คือ รหัสตัวละคร")

@client.command()
async def set(ctx, player: int, pos: int, unitID: str):
    global arr
    global arr2
    global arr3
    global arr4
    global arrB
    global arr2B
    global arr3B
    global arr4B
    global n1

    cout = 0
    if player == 1:
        i = 0
        while i < len(n1):
            if n1[i] == unitID:
                arr[pos-1][0] = h1[i][0]
                arr[pos-1][1] = h1[i][1]
                arr[pos - 1][2] = h1[i][2]
                arr[pos - 1][3] = h1[i][3]
                arrB[pos - 1][0] = h1[i][0]
                arrB[pos - 1][1] = h1[i][1]
                await ctx.send("ผู้เล่น1 " + unitID + " ถูกเพิ่ม!!!")
                break
            cout += 1
            if cout == len(n1):
                await ctx.send("!!รหัสยูนิตผิด!!")
            i += 1
    elif player == 2:
        i = 0
        while i < len(n1):
            if n1[i] == unitID:
                arr2[pos-1][0] = h1[i][0]
                arr2[pos-1][1] = h1[i][1]
                arr2[pos - 1][2] = h1[i][2]
                arr2[pos - 1][3] = h1[i][3]
                arr2B[pos - 1][0] = h1[i][0]
                arr2B[pos - 1][1] = h1[i][1]
                await ctx.send("ผู้เล่น2 " + unitID + " ถูกเพิ่ม!!!")
                break
            cout += 1
            if cout == len(n1):
                await ctx.send("!!รหัสยูนิตผิด!!")
            i += 1
    elif player == 3:
        i = 0
        while i < len(n1):
            if n1[i] == unitID:
                arr3[pos-1][0] = h1[i][0]
                arr3[pos-1][1] = h1[i][1]
                arr3[pos - 1][2] = h1[i][2]
                arr3[pos - 1][3] = h1[i][3]
                arr3B[pos - 1][0] = h1[i][0]
                arr3B[pos - 1][1] = h1[i][1]
                await ctx.send("ผู้เล่น3 " + unitID + " ถูกเพิ่ม!!!")
                break
            cout += 1
            if cout == len(n1):
                await ctx.send("!!รหัสยูนิตผิด!!")
            i += 1
    elif player == 4:
        i = 0
        while i < len(n1):
            if n1[i] == unitID:
                arr4[pos-1][0] = h1[i][0]
                arr4[pos-1][1] = h1[i][1]
                arr4[pos - 1][2] = h1[i][2]
                arr4[pos - 1][3] = h1[i][3]
                arr4B[pos - 1][0] = h1[i][0]
                arr4B[pos - 1][1] = h1[i][1]
                await ctx.send("ผู้เล่น4 " + unitID + " ถูกเพิ่ม!!!")
                break
            cout += 1
            if cout == len(n1):
                await ctx.send("!!รหัสยูนิตผิด!!")
            i += 1
    else:
        await ctx.send("!!!รหัสผู้เล่นผิด!!!")

@client.command()
async def endR(ctx):
    i = 0
    while i < len(arr):
        arr[i][3] = False
        arr2[i][3] = False
        i += 1

@client.command()
async def att(ctx, player: int, unit: int):
    global arr
    global arr2
    global arr3
    global arr4
    if player == 1:
        if arr[unit-1][3] == True:
            await ctx.send("ตีไปแล้ว ตีอีกทำไม")
        else:
            sum = arr[unit-1][0] * arr[unit-1][2]
            arr[unit-1][3] = True
            await ctx.send("/roll notation: " + str(sum) + "d6s")
    elif player == 2:
        if arr2[unit-1][3] == True:
            await ctx.send("ตีไปแล้ว ตีอีกทำไม")
        else:
            sum = arr2[unit-1][0] * arr2[unit-1][2]
            arr2[unit - 1][3] = True
            await ctx.send("/roll notation: " + str(sum) + "d6s")
    elif player == 3:
        if arr3[unit-1][3] == True:
            await ctx.send("ตีไปแล้ว ตีอีกทำไม")
        else:
            sum = arr3[unit-1][0] * arr3[unit-1][2]
            arr3[unit - 1][3] = True
            await ctx.send("/roll notation: " + str(sum) + "d6s")
    elif player == 4:
        if arr4[unit-1][3] == True:
            await ctx.send("ตีไปแล้ว ตีอีกทำไม")
        else:
            sum = arr4[unit-1][0] * arr4[unit-1][2]
            arr4[unit-1][3] = True
            await ctx.send("/roll notation: " + str(sum) + "d6s")


@client.command()
async def hp(ctx, player: int, unit: int, hpE: int):
    global arr
    global arr2
    global arr3
    global arr4
    global arrB
    global arr2B
    global arr3B
    global arr4B

    if player == 1:
        rHP = ((arr[unit - 1][0]-1) * arrB[unit - 1][1])+arr[unit - 1][1]
        print(rHP)
        calHP = rHP - hpE
        print(calHP)
        if calHP <= 0 :
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + " กลับบ้านเกิดแล้ว")
            arr[unit - 1][0] = 0
            arr[unit - 1][1] = 0
        else:
            arr[unit - 1][1] = int(calHP % arrB[unit - 1][1])
            if arr[unit - 1][1] == 0:
                arr[unit - 1][0] = (int(calHP / arrB[unit - 1][1]))
                arr[unit - 1][1] = arrB[unit - 1][1]
            else:
                arr[unit - 1][0] = (int(calHP / arrB[unit - 1][1]))+1
            print(arr[unit - 1][0])
            print(arr[unit - 1][1])
            print(arr)
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + ": " + str(arr[unit-1][0]) + "N, HP:" + str(arr[unit-1][1]))
    elif player == 2:
        rHP = ((arr2[unit - 1][0]-1) * arr2B[unit - 1][1])+arr2[unit - 1][1]
        print(rHP)
        calHP = rHP - hpE
        print(calHP)
        if calHP <= 0 :
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + " กลับบ้านเกิดแล้ว")
            arr2[unit - 1][0] = 0
            arr2[unit - 1][1] = 0
        else:
            arr2[unit - 1][1] = int(calHP % arr2B[unit - 1][1])
            if arr2[unit - 1][1] == 0:
                arr2[unit - 1][0] = (int(calHP / arr2B[unit - 1][1]))
                arr2[unit - 1][1] = arr2B[unit - 1][1]
            else:
                arr2[unit - 1][0] = (int(calHP / arr2B[unit - 1][1]))+1
            print(arr2[unit - 1][0])
            print(arr2[unit - 1][1])
            print(arr2)
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + ": " + str(arr2[unit-1][0]) + "N, HP:" + str(arr2[unit-1][1]))
    elif player == 3:
        rHP = ((arr3[unit - 1][0] - 1) * arr3B[unit - 1][1]) + arr3[unit - 1][1]
        print(rHP)
        calHP = rHP - hpE
        print(calHP)
        if calHP <= 0:
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + " กลับบ้านเกิดแล้ว")
            arr3[unit - 1][0] = 0
            arr3[unit - 1][1] = 0
        else:
            arr3[unit - 1][1] = int(calHP % arr3B[unit - 1][1])
            if arr3[unit - 1][1] == 0:
                arr3[unit - 1][0] = (int(calHP / arr3B[unit - 1][1]))
                arr3[unit - 1][1] = arr3B[unit - 1][1]
            else:
                arr3[unit - 1][0] = (int(calHP / arr3B[unit - 1][1])) + 1
            print(arr3[unit - 1][0])
            print(arr3[unit - 1][1])
            print(arr3)
            await ctx.send(
                "ผู้เล่น1 ตัวละครที่" + str(unit) + ": " + str(arr3[unit - 1][0]) + "N, HP:" + str(arr3[unit - 1][1]))
    elif player == 4:
        rHP = ((arr4[unit - 1][0] - 1) * arr4B[unit - 1][1]) + arr4[unit - 1][1]
        print(rHP)
        calHP = rHP - hpE
        print(calHP)
        if calHP <= 0:
            await ctx.send("ผู้เล่น1 ตัวละครที่" + str(unit) + " กลับบ้านเกิดแล้ว")
            arr4[unit - 1][0] = 0
            arr4[unit - 1][1] = 0
        else:
            arr4[unit - 1][1] = int(calHP % arr4B[unit - 1][1])
            if arr4[unit - 1][1] == 0:
                arr4[unit - 1][0] = (int(calHP / arr4B[unit - 1][1]))
                arr4[unit - 1][1] = arr4B[unit - 1][1]
            else:
                arr4[unit - 1][0] = (int(calHP / arr4B[unit - 1][1])) + 1
            print(arr4[unit - 1][0])
            print(arr4[unit - 1][1])
            print(arr4)
            await ctx.send(
                "ผู้เล่น1 ตัวละครที่" + str(unit) + ": " + str(arr4[unit - 1][0]) + "N, HP:" + str(arr4[unit - 1][1]))

@client.command()
async def show(ctx, player: int):
    global arr
    global arr2
    global arr3
    global arr4

    if player == 1:
        await ctx.send("Player1 have " + str(len(arr)))
        for i in range(len(arr)):
            if arr[i][3] == True:
                await ctx.send("*Player1 Unit" + str(i + 1) + " : " + str(arr[i][0]) + "N, HP:" + str(arr[i][1]))
            else:
                await ctx.send("Player1 Unit" + str(i + 1) + " : " + str(arr[i][0]) + "N, HP:" + str(arr[i][1]))
        print(arr)
    elif player == 2:
        await ctx.send("Player2 have " + str(len(arr2)))
        for i in range(len(arr2)):
            if arr2[i][3] == True:
                await ctx.send("*Player2 Unit" + str(i + 1) + " : " + str(arr2[i][0]) + "N, HP:" + str(arr2[i][1]))
            else:
                await ctx.send("Player2 Unit" + str(i + 1) + " : " + str(arr2[i][0]) + "N, HP:" + str(arr2[i][1]))
        print(arr2)
    elif player == 3:
        await ctx.send("Player3 have " + str(len(arr3)))
        for i in range(len(arr3)):
            if arr3[i][3] == True:
                await ctx.send("*Player3 Unit" + str(i + 1) + " : " + str(arr3[i][0]) + "N, HP:" + str(arr3[i][1]))
            else:
                await ctx.send("Player3 Unit" + str(i + 1) + " : " + str(arr3[i][0]) + "N, HP:" + str(arr3[i][1]))
        print(arr3)
    elif player == 4:
        await ctx.send("Player4 have " + str(len(arr4)))
        for i in range(len(arr4)):
            if arr4[i][3] == True:
                await ctx.send("*Player4 Unit" + str(i + 1) + " : " + str(arr4[i][0]) + "N, HP:" + str(arr4[i][1]))
            else:
                await ctx.send("Player4 Unit" + str(i + 1) + " : " + str(arr4[i][0]) + "N, HP:" + str(arr4[i][1]))
        print(arr4)


@client.command()
async def add(ctx, player: int, Unit: int, n: int, hp: int):
    global arr
    global arr2
    global arr3
    global arr4

    if player == 1:
        arr[Unit - 1][0] = n
        arr[Unit - 1][1] = hp
        await ctx.send("Player1 Unit" + str(Unit) + " : " + str(arr[Unit - 1][0]) + "N, HP:" + str(arr[Unit - 1][1]))
    elif player == 2:
        arr2[Unit][0] = n
        arr2[Unit][1] = hp
        await ctx.send("Player2 Unit" + str(Unit) + " : " + str(arr2[Unit - 1][0]) + "N, HP:" + str(arr2[Unit - 1][1]))
    elif player == 3:
        arr3[Unit][0] = n
        arr3[Unit][1] = hp
        await ctx.send("Player3 Unit" + str(Unit) + " : " + str(arr3[Unit - 1][0]) + "N, HP:" + str(arr3[Unit - 1][1]))
    elif player == 4:
        arr4[Unit][0] = n
        arr4[Unit][1] = hp
        await ctx.send("Player4 Unit" + str(Unit) + " : " + str(arr4[Unit - 1][0]) + "N, HP:" + str(arr4[Unit - 1][1]))


client.run('')
