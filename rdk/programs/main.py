from time import sleep as slp

eatable_items = []
for i in range(6):
    item_eatable = input("食材を渡してください: ")
    eatable_items.append(item_eatable)
    print(i+1,"個目の食材が渡されました: ",item_eatable)
print("現在用意した食材: ",eatable_items)
slp(3)
cooking_items = []
for i in range(6):
    item_eatable = input("調理器具を準備してください: ")
    eatable_items.append(item_eatable)
    print(i+1,"個目の調理器具が渡されました: ",item_eatable)
print("現在用意した調理器具: ",eatable_items)

end = input("enterで終了")
exit()