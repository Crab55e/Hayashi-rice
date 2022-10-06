from time import sleep
try:
    import hrice
    eatable_item = input("材料を入力してください: ")

    hrice.皮をむく(eatable_item)
    sleep(3)
except Exception as e:
    print("ERROR: ", e)
    sleep(3)