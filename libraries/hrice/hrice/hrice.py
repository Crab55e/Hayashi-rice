from contextlib import nullcontext
import random
def 皮をむく(食材):
    if 食材 == "":
        print("引数に食材が入力されていません")
    else:
        rng = random.randrange(1,100)
        if rng == 1:
            print("間違えて指を切ってしまいました")
        print(食材,"の皮をむきました")