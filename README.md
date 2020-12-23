# Corona_End_Game
코로나 종식을 바라는 게임... (~피로그래밍 지원을 위한 프로그램 이었음~)

게임 규칙
----

- 게임을 시작하면 4개의 메뉴창이 나온다. (백신 정보, 감염된 국가 정보, 게임 시작, 게임 종료)

- 1,2 번 메뉴 선택 시 미리 설정된 백신과 감염된 국가 정보가 출력, 3번 메뉴 선택시 게임 시작, 4번 선택시 게임 종료

- 3번 메뉴를 누르면 게임이 시작 되고 플레이어는 사용할 백신 (1-3) 과 백신을 적용할 국가 (1-5) 의 번호를 차례대로 입력

- 총 5 라운드로 진행, 플레이어가 처음 백신과 국가의 번호를 선택하면 나머지 라운드는 자동으로 진행. 
  이때 자동으로 진행 되는 방식은 
  라운드가 끝나고 나서 백신 리스트와 국가 리스트의 데이터들은 무작위로 셔플됨
  셔플된 리스트에서 다음 라운드에 적용할 백신과 국가를 뽑아 적용
  
- 라운드가 진행 될때마다 선택된 백신, 나라들의 정보를 출력하고 해당 라운드에서 완치된 국가 존재 시 해당 국가를 출력

- 매 라운드가 종료 시 감염된 나라들의 정보 출력, 만약 존재 하지 않으면 완치 되었다고 출력함

- 매 라운드 종료 시 (마지막 라운드 제외), 완치된 국가 이외의 감염된 국가의 감염자 수는 해당 국가의 인구수의 15% 만큼 증가. 만약 감염자 수 > 인구 수 인 나라가 생긴다면 게임 중단 후 최종 결과 창으로 이동

- 최종 결과 창에서는 아래 네 개의 정보가 출력됨 
  1. 라운드마다 추가로 감염된 감염자 수 
  2. 백신으로 치료된 감염자 수 
  3. 백신으로 완치된 국가
  4. 감염 인구 수가 많은 순서대로 1위부터 5위까지 국가들의 정보 


ScreenShots
-----

1) 초기 백신과 나라 정보 

<img src="https://user-images.githubusercontent.com/66946182/102860479-4c7a2a80-4471-11eb-96c4-3f9012bf0055.png" width = "60%">
<img src="https://user-images.githubusercontent.com/66946182/102860515-5e5bcd80-4471-11eb-951f-906e8d22fd8d.png" width = "60%">

2) 백신과 적용할 나라 번호 사용자에게 입력 받기 

<img src="https://user-images.githubusercontent.com/66946182/102860560-74698e00-4471-11eb-8db9-c1e8199e2877.png" width = "60%">

3) 2번째 시도 

<img src="https://user-images.githubusercontent.com/66946182/102860631-93682000-4471-11eb-9e00-809eceeb7c48.png" width = "60%">

4) 3번째 시도 
<img src="https://user-images.githubusercontent.com/66946182/102860664-a4b12c80-4471-11eb-8e21-f187d2ec7cd8.png" width = "60%">

5) 4번째 시도 
<img src="https://user-images.githubusercontent.com/66946182/102860716-bc88b080-4471-11eb-9bd5-60c0e79f7d9e.png" width = "60%">

6) 5번째 시도 
<img src="https://user-images.githubusercontent.com/66946182/102860768-d0341700-4471-11eb-91dd-1c6ca9f8cdfd.png" width = "60%">

7) 최종 결과 
<img src="https://user-images.githubusercontent.com/66946182/102860825-eb068b80-4471-11eb-9178-5df1cad84ff3.png" width = "60%">
