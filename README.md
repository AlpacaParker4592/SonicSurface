# 비접촉식 저해상도 점자 시스템을 위한 초음파 어레이 기반 햅틱 장치 개발 프로젝트

<p align="center">
  <img src="https://github.com/user-attachments/assets/39a10892-7c28-4502-96eb-c5c6ad4d1eeb" width="40%">
  <img src="https://github.com/user-attachments/assets/e51a9abf-edb5-438b-a34b-bc5e354d25fc" width="40%">
</p>

- SonicSurface 제작 및 활용 관련 레포지토리

## 레포지토리 내 폴더 설명
- Algorithms - Phase Delay 패턴 생성 알고리즘
- ControlSoftware - 공중부양, 촉각 피드백(또는 소리 구현) 예시 구현 코드(Python)
- Electronics - PCB gerber 파일
- Firmware - FPGA 보드에 업로드할 코드
- Mech - 스페이서(Spacer), 지지대 등 3D 프린팅하거나 레이저 커팅할 보조 파츠

## 프로젝트 진행 목적
- 기존 점자 시스템은 시각장애인의 정보 접근을 위한 핵심 수단이다. 하지만 물리적 접촉에 기반한 구조로 인해 위생 문제, 마모 및 유지보수의 어려움, 설치 공간의 제약 등 여러 한계를 지닌다. 특히 공공장소에서는 접촉을 통한 감염병 전파의 우려가 있으며, 고정형 장치는 유동적인 정보 제공에 적합하지 않아 디지털 환경에서의 활용성이 떨어진다. 이러한 배경에서 비접촉식 촉각 기술은 물리적 장벽 없이 정보를 전달할 수 있고, 다양한 환경에 유연하게 통합될 수 있다는 점에서 새로운 대안으로 주목받고 있다. 비접촉식 초음파 기술은 다양한 위치, 강도, 패턴의 촉각 자극을 공중에서 생성할 수 있어, 점자 정보뿐 아니라 방향 안내, 경고 신호 등 다양한 촉각 콘텐츠를 동시에 제공하는 것이 가능하다. 이를 통해 단순한 문자 전달을 넘어 복합적인 정보 전달 수단으로 기능할 수 있으며, 장애 유무에 관계없이 접근 가능한 유니버설 디자인 구현이 가능하여 포용적 공공 인터페이스로 확장될 수 있다.
- 본 연구는 비접촉 햅틱 기술을 기반으로, 저해상도 점자 시스템을 구현하고 그 효과를 실증적으로 평가함으로써 기존 점자 시스템의 대안적 방향을 제시하고자 하였다. 본 연구는 하드웨어 설계, 초음파 패턴 및 제어 알고리즘 개발, 사용자 중심의 시스템 평가로 구성하여 진행하였다. 초음파 트랜스듀서 어레이의 배열 및 제어 시스템을 설계하여 다양한 점자 패턴을 실시간으로 구현하였으며, 인간의 촉각 인지 특성을 반영한 저해상도 점자 표현 방식을 개발하였다. 또한, 점자의 위치, 진동 특성, 패턴 변형 등을 조합하여 사용자에게 다양한 촉각 정보를 제공하고, 사용자 실험을 통해 점자 인식률, 학습 용이성, 사용자 경험 등 시스템의 효과성을 다각도로 검증하였다.

## 어레이 제작 및 프로그램 작동 관련
### 어레이 조립 절차 및 팁
- Wiki 탭의 [한국어 번역본](https://github.com/AlpacaParker4592/SonicSurface/wiki/%EC%96%B4%EB%A0%88%EC%9D%B4-%EC%A0%9C%EC%9E%91-%EB%B0%A9%EB%B2%95-(How-to-Make-a-Transducer-Array)) 참고

### 작동 방법
- 어레이 제작 및 연결 후 본 레포지토리의 `SonicSurface/ControlSoftware/Evaluation.py` 파일을 실행하세요.
  - 테스트 이전에 `SonicSurface/ControlSoftware/Python/TestOnOff.py` 파일을 실행하여 어레이가 잘 작동되는지 확힌하길 바랍니다.

## Original Github Repogitory
[UPNA Lab/SonicSurface](https://github.com/upnalab/SonicSurface)
