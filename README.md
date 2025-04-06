# SonicSurface
초음파를 이용하여 공중부양(levitation), 촉각 피드백(haptic feedback), 다이렉티브 오디오(directive audio) 등에 적용할 수 있는 오픈소스 트랜스듀서 어레이(transducer array) 제작 프로젝트

Original Github Repogitory: [Link](https://github.com/upnalab/SonicSurface)

# 레포지토리 내 폴더 설명
- Algorithms - Phase Delay 패턴 생성 알고리즘
- ControlSoftware - 공중부양, 촉각 피드백(또는 소리 구현) 예시 구현 코드(Python)
- Electronics - PCB gerber 파일
- Firmware - FPGA 보드에 업로드할 코드
- Mech - 스페이서(Spacer), 지지대 등 3D 프린팅하거나 레이저 커팅할 보조 파츠


# 어레이 조립 방법(영어)
- Instructables: https://www.instructables.com/SonicSurface-Phased-array-for-Levitation-Mid-air-T/
- YouTube: https://www.youtube.com/watch?v=vAEZvYlUnEM
- 논문: https://doi.org/10.3390/app11072981


# 필요한 부품(어레이 1개 기준)
|구매 사이트|부품명|최소 개수|Link|
|:----|:----|:----|----|
|Alibaba|지름 1cm 초음파 발생기(트랜스듀서)|256|[Link](https://manorshi.en.alibaba.com/product/60248714908-801018150/10mm_40khz_piezo_ultrasonic_Transmitter_Receiver_sensor.html?spm=a2700.8304367.rect38f22d.1.2a14fee7WhfcRq)|
|Digikey|솔더 페이스트|1|[Link](https://www.digikey.kr/ko/products/detail/chip-quik-inc/NC191LT10/11480389)|
||2x3 핀 커넥터|2|[Link](https://www.digikey.kr/ko/products/detail/sullins-connector-solutions/PPPC032LFBN-RC/810243)|
||2x2 핀 커넥터|2|[Link](https://www.digikey.kr/ko/products/detail/sullins-connector-solutions/PPPC022LFBN-RC/810242)|
||시프트 레지스터|32|[Link](https://www.digikey.kr/ko/products/detail/toshiba-semiconductor-and-storage/74HC595D/5879984)|
||헤더 커넥터|2|[Link](https://www.digikey.kr/ko/products/detail/sullins-connector-solutions/PPPC222LFBN-RC/810261)|
||MIC4127 SOIC8 드라이버|128|[Link](https://www.digikey.kr/ko/products/detail/microchip-technology/MIC4127YME-TR/1029803)|
||직류(DC) 배럴 커넥터|1|[Link](https://www.digikey.kr/ko/products/detail/schurter-inc/4840-2201/2644239)|
||아두이노 Nano|1|[Link](https://www.digikey.kr/ko/products/detail/arduino/A000005/2638989)|
||0.1uf 캐퍼시터|168|[Link](https://www.digikey.kr/ko/products/detail/yageo/CC0805KRX7R9BB104/302874)|
||전선(수/수)|(필요한 만큼)|[Link](https://www.digikey.kr/ko/products/detail/sparkfun-electronics/PRT-12795/5993860)|
||전선(암/수)|(필요한 만큼)|[Link](https://www.digikey.kr/ko/products/detail/sparkfun-electronics/PRT-12794/5993859)|
|JLCPCB|PCB 기판|3|[Link](https://cart.jlcpcb.com/quote?orderType=1&homeUploadNum=97627eda783a46f08d177d4509fd49e5&businessType=example&fileNameSonicSurface1.2_2Layers_183x169.zip)|
|Amazon|FPGA 프로그래머|(만들려는 어레이 개수 상관없이 1개)|[Link](https://www.amazon.es/Waveshare-Download-Programming-Programmer-Debugger/dp/B00ID9BAUY/ref=sr_1_1?dib=eyJ2IjoiMSJ9.pJ6KQmrP2LctrOz-kMSqMXXfA4ov--utB485fOiAPyQ.MuUf_b9A_a2vgSnp4dbgAUGR5UO1FjtJPPbTX2heyuQ&dib_tag=se&keywords=Blaster+USB+ALTERA&qid=1715358515&sr=8-1)|

# 권장 부품 및 도구
|구매 사이트|부품명|최소 개수|Link|
|----|----|----|----|
|Digikey|솔더윅|0(4개 권장)|[Link](https://www.digikey.kr/short/2mwb35n2)|
||솔더 페이스트 전용 스패출러(스프레더)|||
||기판 납땜용 리플로우 오븐|||
||납땜용 실납|||
||납땜용 인두|||
||납땜용 열풍기|||
||납땜 잔여물 제거용 솔|||
|(다이소 등)|전자부품용 족집게|||
|(약국 등)|이소프로필 알코올+주사기|500mL 이상||
||목재 합판|2||
||지지대용 철제 구조물|||
||발포 스티로폼 파티클|||
