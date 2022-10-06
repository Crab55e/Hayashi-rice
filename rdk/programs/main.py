try:
    # import libraries
    from time import sleep as slp
    import hrice

    # enter Eatable items
    eatable_items = []
    for i in range(6):
        eatable_item = input("食材を渡してください: ")
        eatable_items.append(eatable_item)
        print(i+1,"個目の食材が渡されました: ",eatable_item)
    print("現在用意した食材: ",eatable_items)
    slp(1)

    # enter Cooking items
    cooking_items = []
    for i in range(6):
        cooking_item = input("調理器具を準備してください: ")
        cooking_items.append(cooking_item)
        print(i+1,"個目の調理器具が渡されました: ",cooking_item)
    print("現在用意した調理器具: ",cooking_items)

    for i in range(6):
        hrice.皮をむく(eatable_item[i])
    end = input("Enterで終了")
    exit()
except Exception as e:
    print(e)