# snd-ds-proj-exp

Git Submodule 세미나 데모용 **작업(프로젝트)** 레포지토리.

랜덤하게 생성한 `y_true` / `y_pred` 에 대해, 공통 모듈
`snd-ds-common-exp` 의 평가지표 함수를 호출합니다.

## 데모 순서

```bash
# 1) 공통 모듈을 submodule 로 연결 (common/ 경로에)
git submodule add <snd-ds-common-exp-url> common

# 2) 실행
python main.py
```

> `common/` 은 submodule 로 연결되기 전까지 비어 있습니다.
> 연결 전에 `python main.py` 를 돌리면 import 에러가 나는데, 그게 데모 포인트입니다.

## 다른 사람이 이 레포를 클론할 때

```bash
git clone --recursive <snd-ds-proj-exp-url>
# 이미 클론했다면
git submodule update --init --recursive
```
