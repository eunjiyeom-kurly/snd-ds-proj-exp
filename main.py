"""snd-ds-common-exp 를 submodule 로 연결해 평가지표를 호출하는 데모.

데모 순서:
  1) git submodule add <snd-ds-common-exp-url> common
  2) python main.py

submodule 을 `common/` 경로에 추가한다고 가정하고, 그 경로를 import path 에 넣어 metrics 모듈을 불러옴
(submodule 을 아직 연결하지 않으면 import 에서 실패)
"""
import os
import random
import sys

# submodule 로 추가한 common 레포 경로를 import path 에 추가
sys.path.append(os.path.join(os.path.dirname(__file__), "common"))

from metrics import accuracy, precision, recall, f1  # noqa: E402


def main():
    random.seed(42)
    n = 20
    y_true = [random.randint(0, 1) for _ in range(n)]
    y_pred = [random.randint(0, 1) for _ in range(n)]

    print("y_true :", y_true)
    print("y_pred :", y_pred)
    print(f"accuracy  : {accuracy(y_true, y_pred):.3f}")
    print(f"precision : {precision(y_true, y_pred):.3f}")
    print(f"recall    : {recall(y_true, y_pred):.3f}")
    print(f"f1        : {f1(y_true, y_pred):.3f}")


if __name__ == "__main__":
    main()
