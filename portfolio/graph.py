import matplotlib.pyplot as plt
import numpy as np
import unicodedata
import math


# ----------半角にする----------
def normalize_string(input_str):
    return unicodedata.normalize("NFKC", input_str)


# ----------数字か判定----------
def is_float(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False


def is_integer(value):
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False


# ----------演算----------
def sqrt(number):
    return math.sqrt(number)


def sin(number):
    return math.sin(number)


def cos(number):
    return math.cos(number)


def tan(number):
    return math.tan(number)


def ln(number):
    return math.log(number)


def log(number):
    return math.log10(number)


pie = math.pi
eNumber = math.e

#FIXME:マイナス範囲で小数幅を取るとエラーになる(例:-1 < x < 1で幅0.1)
#FIXME:tanがうまく動かない
while True:
    quantity = input("２つ以上の関数を1つのグラフする場合は文字を入力、そうでない場合はenterを入力:")
    if quantity:
        # ----------------------------------------グラフが2つ以上の時----------------------------------------
        while True:
            howMany = input("関数の個数を入力:")
            if is_integer(howMany) == True and int(howMany) >= 2:
                break
            else:
                print("2以上の整数を入力してください:")

        while True:
            x_range = input("すべての関数の範囲が違う場合は文字を入力、同じ場合はenterを入力:")
            judgement = 1
            if x_range:
                judgement = howMany
            x_starts = [0] * int(judgement)
            x_ends = [0] * int(judgement)
            x_betweens = [0] * int(judgement)

            for i in range(int(judgement)):
                while True:
                    while True:
                        x_start = input("x の始まりの数を入力してください:")
                        x_start = normalize_string(x_start)
                        x_end = input("x の終わりの数を入力してください:")
                        x_end = normalize_string(x_end)
                        x_between = input("x の間隔を入力してください:")
                        x_between = normalize_string(x_between)
                        if (
                            is_float(x_start) == True
                            and is_float(x_end) == True
                            and is_float(x_between) == True
                        ):
                            break
                        else:
                            print("数字を入力してください")

                    count = 0
                    while 0 < float(x_start) < 1:
                        x_between = float(x_between) * 10
                        x_start = float(x_start) * 10
                        x_end = float(x_end) * 10
                        count += 1

                    while 0 < float(x_end) < 1:
                        x_between = float(x_between) * 10
                        x_start = float(x_start) * 10
                        x_end = float(x_end) * 10
                        count += 1

                    while 0 < float(x_between) < 1:
                        x_between = float(x_between) * 10
                        x_start = float(x_start) * 10
                        x_end = float(x_end) * 10
                        count += 1

                    if float(x_end) - float(x_start) > 0:
                        if float(x_between) > 0:
                            if (float(x_end) - float(x_start)) % float(x_between) == 0:
                                break
                            else:
                                print("間隔は範囲を等分にできる値を入力してください")
                        else:
                            print("間隔には0より大きい値を入力してください")
                    else:
                        print("始まりの数は終わりの数より小さくしてください")

                # ----------πを付けるか----------
                answer = input("xの範囲にπがつくなら文字を入力、つかないならenterを入力:")
                if answer:
                    x_start = float(x_start) * np.pi
                    x_end = float(x_end) * np.pi
                    x_between = float(x_between) * np.pi

                x_end = float(x_end) + float(x_between)
                # ----------xのデータ----------
                while count != 0:
                    x_start = float(x_start) / 10
                    x_end = float(x_end) / 10
                    x_between = float(x_between) / 10
                    count -= 1

                x_starts[i] = float(x_start)
                x_ends[i] = float(x_end)
                x_betweens[i] = float(x_between)
            # ----------------------------------------yのデータ----------------------------------------
            x_values = [0] * int(howMany)
            if int(judgement) == int(howMany):
                for j in range(int(howMany)):
                    x_values[j] = np.arange(
                        float(x_starts[j]), float(x_ends[j]), float(x_betweens[j])
                    )
            else:
                for j in range(int(howMany)):
                    x_values[j] = np.arange(
                        float(x_starts[0]), float(x_ends[0]), float(x_betweens[0])
                    )

            y_values = [0] * int(howMany)
            for k in range(int(howMany)):
                while True:
                    print(
                        "和、差、積、商、乗、根、sin、cos、tan、ln、log、π、e\n + , - , * , / , ** ,sqrt(値),sin(値),cos(値),tan(値),ln(値),log(値),p,e"
                    )
                    expression = input("数式を入力してください:y=")
                    try:
                        y_values[k] = [
                            eval(
                                expression.replace("x", str(x))
                                .replace("p", str(pie))
                                .replace("e", str(eNumber))
                            )
                            for x in x_values[k]
                        ]
                        print("x:", x_values[k])
                        print("y:", y_values[k])
                        result = True
                        break
                    except Exception as e:
                        print("エラー:", e)
                        reset = input("\n範囲からやり直す場合は文字を入力、式をやり直す場合はenterを入力:")
                        if reset:
                            result = False
                            break

            if result == True: #falseなら範囲のとこまで戻る(line.68)
                break

        for j in range(int(howMany)):
            plt.plot(x_values[j], y_values[j], label=f"Function {j+1}")

        title = input("タイトルを入力(enterでラベルなし):")
        if title:
            plt.title(title)

        xlabel = input("xのラベルを入力(enterでラベルなし):")
        if xlabel:
            plt.xlabel(xlabel)

        ylabel = input("yのラベルを入力(enterでラベルなし):")
        if ylabel:
            plt.ylabel(ylabel)

        plt.grid(True)
        plt.show()
        retry = input("もう一度グラフを作る場合は文字を入力、終わる場合はenterを入力")
        if not retry:  #trueならグラフの個数選択に戻る(line.57)
            break
    # ----------------------------------------グラフが1つの時----------------------------------------
    else:
        while True:
            while True:
                while True:
                    x_start = input("x の始まりの数を入力してください:")
                    x_start = normalize_string(x_start)
                    x_end = input("x の終わりの数を入力してください:")
                    x_end = normalize_string(x_end)
                    x_between = input("x の間隔を入力してください:")
                    x_between = normalize_string(x_between)
                    if is_float(x_start) and is_float(x_end) and is_float(x_between):
                        break
                    else:
                        print("数字を入力してください")

                count = 0
                while 0 < float(x_start) < 1:
                    x_between = float(x_between) * 10
                    x_start = float(x_start) * 10
                    x_end = float(x_end) * 10
                    count += 1

                while 0 < float(x_end) < 1:
                    x_between = float(x_between) * 10
                    x_start = float(x_start) * 10
                    x_end = float(x_end) * 10
                    count += 1

                while 0 < float(x_between) < 1:
                    x_between = float(x_between) * 10
                    x_start = float(x_start) * 10
                    x_end = float(x_end) * 10
                    count += 1

                if float(x_end) - float(x_start) > 0:
                    if float(x_between) > 0:
                        if (float(x_end) - float(x_start)) % float(x_between) == 0:
                            break
                        else:
                            print("間隔は範囲を等分にできる値を入力してください")
                    else:
                        print("間隔には0より大きい値を入力してください")
                else:
                    print("始まりの数は終わりの数より小さくしてください")

            x_end = float(x_end) + float(x_between)
            # ----------πを付けるか----------
            answer = input("xの範囲にπがつくなら文字を入力、つかないならenterを入力:")
            if answer:
                x_start = float(x_start) * np.pi
                x_end = float(x_end) * np.pi
                x_between = float(x_between) * np.pi
            # ----------xのデータ----------
            while count != 0:
                x_start = float(x_start) / 10
                x_end = float(x_end) / 10
                x_between = float(x_between) / 10
                count -= 1
            x_values = np.arange(float(x_start), float(x_end), float(x_between))
            while True:
                print(
                    "和、差、積、商、乗、根、sin、cos、tan、ln、log、π、e\n + , - , * , / , ** ,sqrt(値),sin(値),cos(値),tan(値),ln(値),log(値),p,e"
                )
                expression = input("数式を入力してください:y=")
                try:
                    y_values = [
                        eval(
                            expression.replace("x", str(x))
                            .replace("p", str(pie))
                            .replace("e", str(eNumber))
                        )
                        for x in x_values
                    ]
                    print("x:", x_values)
                    print("y:", y_values)
                    result = True
                    break
                except Exception as e:
                    print("エラー:", e)
                    reset = input("\n範囲からやり直す場合は文字を入力、式をやり直す場合はenterを入力:")
                    if reset:
                        result = False
                        break

            if result == True:  #falseなら範囲のとこまで戻る(line.209)
                break

        plt.plot(x_values, y_values)
        title = input("タイトルを入力(enterでラベルなし):")
        if title:
            plt.title(title)

        xlabel = input("xのラベルを入力(enterでラベルなし):")
        if xlabel:
            plt.xlabel(xlabel)

        ylabel = input("yのラベルを入力(enterでラベルなし):")
        if ylabel:
            plt.ylabel(ylabel)

        plt.grid(True)
        plt.show()
        retry = input("もう一度グラフを作る場合は文字を入力、終わる場合はenterを入力:")
        if not retry:  #trueならグラフの個数選択に戻る(line.57)
            break
