# 비접촉식 저해상도 점자 시스템을 위한 초음파 어레이 기반 햅틱 디바이스 개발 프로젝트

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13.2-3766AB?style=flat&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/build-passing-dark_green?style=flat"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/39a10892-7c28-4502-96eb-c5c6ad4d1eeb" width="40%">
  <img src="https://github.com/user-attachments/assets/e51a9abf-edb5-438b-a34b-bc5e354d25fc" width="40%">
</p>

- SonicSurface 제작 및 활용 관련 레포지토리

## 레포지토리 내 폴더 설명
- [`Algorithms`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/Algorithms) - Phase Delay 패턴 생성 알고리즘
- [`ControlSoftware`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/ControlSoftware) - 공중부양, 촉각 피드백(또는 소리 구현) 예시 구현 코드(Python)
- [`Electronics`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/Electronics) - PCB gerber 파일
- [`Firmware`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/Firmware) - FPGA 보드에 업로드할 코드
- [`Mech`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/Mech) - 스페이서(Spacer), 지지대 등 3D 프린팅하거나 레이저 커팅할 보조 파츠
- [`Simulations`](https://github.com/AlpacaParker4592/SonicSurface/tree/main/Simulations) - 단일/이중 어레이 시뮬레이션(Apache NetBeans 및 Ultraino 소프트웨어 전용)

## 어레이 제작 및 프로그램 작동 관련
### 어레이 조립 절차 및 팁
- Wiki 탭의 [한국어 번역본](https://github.com/AlpacaParker4592/SonicSurface/wiki/%EC%96%B4%EB%A0%88%EC%9D%B4-%EC%A0%9C%EC%9E%91-%EB%B0%A9%EB%B2%95-(How-to-Make-a-Transducer-Array)) 참고

### 점자 시스템 작동 방법
- 어레이 제작 및 연결 후 본 레포지토리의 `SonicSurface/ControlSoftware/Evaluation.py` 파일을 실행하세요.
  - 테스트 이전에 `SonicSurface/ControlSoftware/Python/TestOnOff.py` 파일을 실행하여 어레이가 잘 작동되는지 확힌하길 바랍니다.

### 이외 파티클 공중부양, 햅틱 센세이션 예시 코드
- 어레이 제작 및 연결 후 `https://github.com/AlpacaParker4592/SonicSurface/tree/main/ControlSoftware/Python` 폴더 내 파일을 실행하세요.

## Original Github Repogitory
[UPNA Lab/SonicSurface](https://github.com/upnalab/SonicSurface)
