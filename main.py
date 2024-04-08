import random

def main():
    # 半径が１の円とその円に外接する正方形(１辺の長さが２の正方形)で考える。
    # モンテカルロ法は、正方形の中に任意の数の点を打ち込み、正方形内に打ち込まれた点の総数と、正方形内の円の中に打ち込まれた点の総数から円周率を導く。
    # 円の面積 ÷ 正方形の面積 = ランダムに打ち込まれた点が円の中にある確率
    # π ÷ 4 = π / 4 = 円の中にある点の数 ÷ 点の総数
    # π(円周率) = (円の中にある点の数 ÷ 点の総数) × 4

    trial_count = 10000 # 正方形の中に打ち込む点の数を 仮に10000とする(任意の数)。
    all_point = 0 # 打ち込まれた点の数
    circle_inner_point = 0 # 打ち込まれた点の数のうち、円の中にある点の数。

    for _ in range(trial_count): # 打ち込まれた点の総数だけ繰り返す。
        x = random.uniform(0, 1) # ランダムで、0~1までの浮動小数点数を生成する。(x座標) 円を1 / 4 に分割したうちの一つをピックアップして、x の範囲を(0 ≤ x ≤ 1)とする。
        y = random.uniform(0, 1) # ランダムで、0~1までの浮動小数点数を生成する。(y座標) 円を1 / 4 に分割したうちの一つをピックアップして、y の範囲を(0 ≤ y ≤ 1)とする。
        all_point += 1 # 打ち込まれた点の総数なので、常にカウントする。
        if (x*x)+(y*y) <= 1: # 円の中の点の数については、円の方程式から円の内側を満たす(x, y)条件からフィルタリングする。
            circle_inner_point += 1 # 上記の条件を満たすことで、円の中に存在する点としてカウントする。


    circle_ratio = (circle_inner_point / all_point) * 4 # 円周率を、最初に記載した式から求める。

    print(circle_ratio) # 求められた円周率

if __name__ == '__main__':
    main()