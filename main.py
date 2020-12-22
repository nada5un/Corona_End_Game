import random

class vaccin: #백신
    def __init__(self,name,cure_rate):
        self.name = name # 백신 이름
        self.cure_rate = cure_rate

class country: # 나라별로
    i_per_num =0# 라운드 마다 감염 수
    c_per_num =0# 라운드 마다 치료 수
    def __init__(self,name,t_num,i_num):
        self.name = name # 나라 이름
        self.t_num = t_num # 총 인구수
        self.i_num = i_num # 감염 인구수
    def cure(self,vaccin_rate):
        country.c_per_num = int(self.i_num * vaccin_rate / 100)
        self.i_num -= int(self.i_num * vaccin_rate /100)# 감염자 수 감소 -> 치료
    def printResult(self):
        print("감염 국가 :{}".format(self.name))
        print("인구수 : {}명".format(self.t_num))
        print("감염 인구수 : {}명".format(self.i_num))
        print("")
    def infectIncrease(self):# 라운드 종료시
        country.i_per_num = int(self.t_num*0.15)
        self.i_num += int(self.t_num* 0.15)
    def checkFinished(self):# 라운드 종료시
        if (self.i_num>self.t_num):
            return  True
    def printScore(self): # 최종 결과
        print("국가 :{}".format(self.name))
        print("인구수 : {}명".format(self.t_num))
        print("감염 인구수 : {}명".format(self.i_num))
        print("")
    def __lt__(self, other): # 정렬 위함
        return self.i_num > other.i_num

def info(a,b,c,d,e):
    print("선택된 백신: {}, 치료율: {}%".format(a,b))
    print("선택된 나라: {}, 인구수: {}명, 감염자수: {}명".format(c,d,e))

def vaccin_info():
    print("백신 이름: 백신1")
    print("백신 치료율: 25%\n")
    print("백신 이름: 백신2")
    print("백신 치료율: 50%\n")
    print("백신 이름: 백신3")
    print("백신 치료율: 100%\n")

def injure_list():
    print("감염 국가: 한국")
    print("인구 수: 1500명")
    print("감염 인구 수: 300명\n")
    print("감염 국가: 중국")
    print("인구 수: 3000명")
    print("감염 인구 수: 800명\n")
    print("감염 국가: 일본")
    print("인구 수: 2000명")
    print("감염 인구 수: 500명\n")
    print("감염 국가: 미국")
    print("인구 수: 2500명")
    print("감염 인구 수: 750명\n")
    print("감염 국가: 독일")
    print("인구 수: 2200명")
    print("감염 인구 수: 1000명\n")

def print_menu():
    print("-------------------")
    print("    코로나 종식 게임    ")
    print("-------------------")
    print("1. 백신 정보")
    print("2. 감염된 국가 정보")
    print("3. 게임 시작")
    print("4. 게임 종료")
    print("-------------------")

def shuffle(a,b): #백신
    random.shuffle(a)
    random.shuffle(b)
def roundCEnd():
    print("================================")
    print("모든 국가가 완치되었습니다!! ")
def roundEnd(n,flag):
    if flag == 1:
        print("\n{}차 백신 투여 후 감염된 나라에 대한 정보 ".format(n))
        print("================================")
        flag = 0
    elif flag == 0:
        print("================================")
        print("{}차 백신 투여 후 감염된 나라에 대한 정보 ".format(n))
        print("================================")
def roundEEnd():
    print("감염자 수가 인구 수보다 많은 국가가 발생하였습니다. 게임을 중단합니다!")
    print("================================")
    print("             최종 결과")
    print("================================")
def game_start():
    # 초기화
    v1 = vaccin("백신1", 25)
    v2 = vaccin("백신2", 50)
    v3 = vaccin("백신3", 100)
    v = [v1, v2, v3]

    c1 = country("한국", 1500, 300)
    c2 = country("중국", 3000, 800)
    c3 = country("일본", 2000, 500)
    c4 = country("미국", 2500, 750)
    c5 = country("독일", 2200, 1000)
    c = [c1, c2, c3, c4, c5]

    cure_list =[] # 완치된 나라
    cure_list_name = [] # 완치된 나라 이름

    #첫번째 라운드
    print("사용할 백신(1~3)과 백신을 적용할 나라(1~5) 의 번호를 차례대로 입력하세요.")
    a,b = input().split() # a: 백신, b: 나라
    a = int(a) # 백신
    b = int(b) # 나라

    count =1 # 라운드 수
    c_num =0 # 완치된 국가 수
    flag =0 # 완치된 국가 있는 경우 출력 제어 위함
    end_flag =0 # 끝났는지 확인

    sum_i = 0  # 감염된 사람 총 합
    sum_c = 0  # 치료된 사람 총 합

    shuffle(v,c) # 백신과 나라 섞기

    info(v[a-1].name,v[a-1].cure_rate,c[b-1].name,c[b-1].t_num,c[b-1].i_num) # 선택된 백신,나라 정보
    c[b-1].cure(v[a-1].cure_rate) # 백신 적용
    sum_c += c[b-1].c_per_num # 라운드 치유된 수 증가

    for i in c: #  먼저 완치 된 국가 있는 지 확인
        if i.i_num == 0:
            c_num += 1
            cure_list.append(i)  # 완치된 국가 리스트에 넣기
            print("================================")
            print("완치 된 국가: {}".format(i.name))
            flag =1
            c.remove(i)
    roundEnd(count,flag) #  ...차 백신 투여후  감염된 나라에 대한 정보
    flag =0
    for i in c:
        i.printResult() # 백신 적용 된 정보 출력 -> 감염자 수 증가 전
        i.infectIncrease() # 감염자 수 증가
        sum_i += i.i_per_num # 라운드 감염 수 증가

    # 2번째~5라운드 까지
    while count<5:
        count += 1
        print("★ {}번째 시도 ★\n".format(count))

        shuffle(v, c)  # 백신과 나라 섞기
        info(v[a - 1].name, v[a - 1].cure_rate, c[b - 1-c_num].name, c[b - 1-c_num].t_num, c[b - 1-c_num].i_num)  # 선택된 백신,나라 정보
        c[b - 1-c_num].cure(v[a - 1].cure_rate)  # 백신 적용
        sum_c += c[b - 1-c_num].c_per_num  # 라운드 치유된 수 증가

        # 먼저 완치 된 국가 있는 지 확인
        for i in c:
            if i.i_num == 0:
                c_num += 1 # 완치된 국가 수 증가
                cure_list.append(i)  # 완치된 국가 리스트에 넣기
                print("================================")
                print("완치 된 국가: {}".format(i.name))
                flag= 1
                c.remove(i)# 완치된 국가 제거
        roundEnd(count,flag)  # ...차 백신 투여후  감염된 나라에 대한 정보 출력
        flag = 0
        # 감염 국가, 인구수, 감염인구수 출력
        for i in c:
            # 백신 적용 된 정보 출력 -> 감염자 수 증가 전
            i.printResult()
            if count!= 5: # 마지막 라운드 제외하고
                # 이제 감염자 수 증가
                i.infectIncrease()
                sum_i += i.i_per_num  # 라운드 감염 수 증가
            # 감염자 수 > 인구 수 인 나라가 있거나, 라운드가 끝나면
            if i.checkFinished() == True or count == 5:
                end_flag = 1  # 게임 종료

        if end_flag ==1 :
            if count!=5: # 감염자수 > 인구 수 인 나라가 있다면
                roundEEnd()  # 감염자 수가 인구 수보다 많은 국가 발생.게임 중단합니다 출력
            else : # 라운드가 다 되서 끝난거라면
                print("================================")
                print("             최종 결과")
                print("================================")
            if c_num == 5: # 모든 국가가 완치 되었다면
                roundCEnd()
            for j in cure_list:  # 완치된 국가 리스트
                cure_list_name.append(j.name)
            print("라운드마다 추가로 감염된 감염자 수: {}명".format(sum_i))
            print("백신으로 치료된 감염자 수: {}명".format(sum_c))
            print("백신으로 완치된 국가: {} ({}개)\n".format(" ".join(cure_list_name), c_num))

            c = sorted(c) # 정렬
            i = 0 # 완치된 국가 순위 나타내기 위함

            # 완치되지 않은 국가 순위 순으로 출력
            for index, j in enumerate(c, 1):
                print("{}위".format(index))
                j.printScore()
                i =index
            # 완치된 국가 출력
            for index, j in enumerate(cure_list,i+1):
                print("{}위".format(index))
                j.printScore()
            return

# main
if __name__ == '__main__':
    while(True):
        print_menu()
        menu = int(input(">"))
        if menu ==1:
            vaccin_info()
        elif menu ==2:
            injure_list()
        elif menu==3:
            game_start()
            break
        elif menu==4:
            print("게임을 종료합니다.")
            break