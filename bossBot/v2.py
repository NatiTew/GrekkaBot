import pyodbc
from discord.ext import commands

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Aepmong\PycharmProjects\disBot\DB.accdb;')
cursor = conn.cursor()
# cursor.execute("SELECT Name, HP FROM Unit WHERE Unit_ID = 'A1' ")
#
# for row in cursor.fetchall():
#     print(row.Name, row.HP)
#
#     cursor.execute("SELECT Name, HP FROM Unit WHERE Unit_ID = 'A2' ")
#
#     for row in cursor.fetchall():
#         print(row.Name, row.HP)

client = commands.Bot(command_prefix="-")

player1 = ""
player2 = ""
turn = ""
gameOver = True
arr = [[]]
arr2 = [[]]
arr3 = [[]]
arr4 = [[]]
arrB = [[]]
arr2B = [[]]
arr3B = [[]]
arr4B = [[]]
statusBot = [False, False, False]

status = ['N', 'HP', 'att', False]

@client.command()
async def start(ctx):
    await ctx.send("----- เริ่มเกมส์ โปรดเลือกตำสั่งต่อไปนี้ ----- \n"
                   "เครื่องหมายหน้าคำสั่งคือ - \n"
                   "Player Min: 2 | Max: 4 \n"
                   "start2p 3 4 \n"
                   "ผู้เล่น 2 คน | คนที่1ลง 2unit | คนที่2 ลง4unit \n"
                   "start3p 4 5 6 \n"
                   "ผู้เล่น 3 คน | คนที่1ลง 4unit | คนที่2 ลง5unit | คนที่3 ลง6unit \n"
                   "start4p 4 5 6 7 \n"
                   "ผู้เล่น 4 คน | คนที่1ลง 5unit | คนที่2 ลง6unit | คนที่3 ลง7unit | คนที่4 ลง8unit")
    await ctx.send("-------------------------------------")

@client.command()
async def start2p(ctx, player1: int, player2: int):
    global arr, arr2, arrB, arr2B, statusBot

    if statusBot[1] == True:
        await ctx.send("เกมส์อยู่ใน 3P")
    elif statusBot[2] == True:
        await ctx.send("เกมส์อยู่ใน 4P")
    elif(statusBot[0] == False):
        arr = [[None for k in range(len(status))] for l in range(player1)]
        arrB = [[None for k in range(len(status))] for l in range(player1)]
        print(arr)
        arr2 = [[None for k in range(len(status))] for l in range(player2)]
        arr2B = [[None for k in range(len(status))] for l in range(player2)]
        print(arr2)
        await ctx.send("----- โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3 ----- \n"
                       "เครื่องหมายหน้าคำสั่งคือ - \n"
                       "1 คือ ผู้เล่น \n"
                       "2 คือ ตำแหน่งตัวละคร \n"
                       "A3 คือ รหัสตัวละคร")
        statusBot[0] = True
    else:
        await ctx.send("เกมส์เริ่มไปแล้ว โปรด Reset")

@client.command()
async def start3p(ctx, player1: int, player2: int, player3: int):

    global arr, arr2, arr3, arrB, arr2B, arr3B, statusBot

    if statusBot[0] == True:
        await ctx.send("เกมส์อยู่ใน 2P")
    elif statusBot[2] == True:
        await ctx.send("เกมส์อยู่ใน 4P")
    elif (statusBot[1] == False):
        arr = [[0 for k in range(2)] for l in range(player1)]
        arrB = [[0 for k in range(2)] for l in range(player1)]
        print(arr)
        arr2 = [[0 for k in range(2)] for l in range(player2)]
        arr2B = [[0 for k in range(2)] for l in range(player2)]
        print(arr2)
        arr3 = [[0 for k in range(2)] for l in range(player3)]
        arr3B = [[0 for k in range(2)] for l in range(player3)]
        print(arr3)
        await ctx.send("----- โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3 ----- \n"
                       "เครื่องหมายหน้าคำสั่งคือ - \n"
                       "1 คือ ผู้เล่น \n"
                       "2 คือ ตำแหน่งตัวละคร \n"
                       "A3 คือ รหัสตัวละคร")
    else:
        await ctx.send("เกมส์เริ่มไปแล้ว โปรด Reset")

@client.command()
async def start4p(ctx, player1: int, player2: int, player3: int, player4: int):

    global arr, arr2, arr3, arr4, arrB, arr2B, arr3B, arr4B, statusBot

    if statusBot[0] == True:
        await ctx.send("เกมส์อยู่ใน 2P")
    elif statusBot[1] == True:
        await ctx.send("เกมส์อยู่ใน 3P")
    elif (statusBot[2] == False):
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
        await ctx.send("----- โปรดเพิ่มตัวละครด้วยคำสั่ง set 1 2 A3 ----- \n"
                       "เครื่องหมายหน้าคำสั่งคือ - \n"
                       "1 คือ ผู้เล่น \n"
                       "2 คือ ตำแหน่งตัวละคร \n"
                       "A3 คือ รหัสตัวละคร")
        statusBot[2] = True
    else:
        await ctx.send("เกมส์เริ่มไปแล้ว โปรด Reset")

@client.command()
async def setp1(ctx, unitID: str, pos):
    global arr, arr2, arr3, arr4, arrB, arr2B, arr3B, arr4B, statusBot

    if pos[0].upper() == 'A':
        i = 0
        while i<len(arr):
            if arr[i] is None:
                print(pos)
    elif pos[0].upper() == 'P':
        intPos = int(pos[1])
        for i in range(intPos):
            print(pos)


client.run("")