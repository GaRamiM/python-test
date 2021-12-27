from random import randint
q = randint(1, 2)


def holjjak (my, wjr):

    if q == 1 :
        w = '홀'

    elif q == 2 :
        w = '짝'

    z = input ('(홀 / 짝 입력) > ')
    x = input ('구슬 몇개를 걸꺼냐? > ')

    if z == '홀' :
        c = 1

    elif z == '짝' :
        c = 2

    x=int(x)
    #my = 10

    #wjr = 10
    d=0

    if q == 2 and c == 2 :
        my += x
        wjr -= x

    elif q == 2 and c == 1 :
        my -= x
        wjr += x
    
    elif q == 1 and c == 1 :
        my += x
        wjr -= x

    elif q == 1 and c == 2 :
        my -= x
        wjr += x
        
    print('함 출력 : my', my, '적 :', wjr)
    return my, wjr;

###### 값 초기화  #########
my1 = 10
wjr1 = 10             # 함수 값 받기 위한 함수 초기화 
cnt = 0             # 맞추기 시도 횟수 초기화 

###### 함수를 이용한 값 맞추기 실행 #########
while cnt < 10:                         # 10번 실행
    print (10-cnt, "번 남았습니다")
    
    my1, wjr1 = holjjak(my1, wjr1) 
                   # 함수 반환값 저장 
    if (my1 >= 20):                      # 함수 반환값이 1이면 프로그램 종료
        print ("당신이 이겼습니다.")
        break
    elif (my1 <= 0):
        print ("당신이 졌습니다.")
        break       
    cnt += 1                            # 횟수 증가

if (my1 > wjr1):
    print ("당신이 이겼습니다.")
elif (my1 > wjr1):
    print ("당신이 졌습니다.")
elif (my1 == wjr1):
    print ("당신이 이겼습니다.")  