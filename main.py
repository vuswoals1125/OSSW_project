#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import UARTDevice
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time

#==========[Initialize]==========
#==========[sensors]==========
ev3 = EV3Brick()
gyro = GyroSensor(Port.S1)
ser = UARTDevice(Port.S3, baudrate=115200)
<<<<<<< HEAD
cs = ColorSensor(Port.S2)

=======
>>>>>>> mhj4_branch
#==========[motors]==========
grab_motor = Motor(Port.A)
shooting_motor = Motor(Port.B)

left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=115)

#==========[target_angle turn(gyro)]==========
def turn(target_angle, power):
    
    # left_motor.run(power)
    # right_motor.run(-power)
    # while True:
    #     angle=gyro.angle()
        
    #     if abs(angle)>target_angle-2:
    #         left_motor.stop()
    #         right_motor.stop()
    #         break
    # robot.turn()
    print('robot turn')
    robot.drive(power, power)
    while True:
        angle = gyro.angle()
        print(angle)
        if abs(angle)>target_angle-2:
            robot.stop()
            break

#==========[camera_chase]==========
def process_uart_data(data):
    try:
        # 데이터를 문자열로 디코드 (키워드 인자 제거)
        data_str = data.decode().strip()
        if not data_str:
            pass

        # 문자열에서 리스트 파싱
        data_str = data_str.strip("[]")
        parsed_list = [int(value.strip()) for value in data_str.split(",")]

        # 파싱된 결과 반환
        return parsed_list
    except:
        # 에러 처리
        return [-1,-1] # -1이 나오면 무시하는 코드 사용

def pd_control(cam_data, kp, kd, power):
    global previous_error
    error = cam_data - threshold
    derivative = error - previous_error
    output = (kp * error) + (kd * derivative)
    robot.drive(power, output)
    previous_error = error
 
#==========[shooting positions]==========
def grab(command):
    if command == 'motion3':
        #close
<<<<<<< HEAD
        grab_motor.run_until_stalled(800,Stop.COAST,duty_limit=80)
=======
        grab_motor.run_until_stalled(100,Stop.COAST,duty_limit=50)
>>>>>>> mhj4_branch
        #set_zero point
        grab_motor.reset_angle(0)
    elif command == 'motion1':
        #open1
<<<<<<< HEAD
        grab_motor.run_until_stalled(-1800,Stop.COAST,duty_limit=80)
    elif command == 'motion2':
        #open2
        grab_motor.run_target(80,-1800)
=======
        grab_motor.run_until_stalled(-100,Stop.COAST,duty_limit=50)
    elif command == 'motion2':
        #open2
        grab_motor.run_target(100,-100)

>>>>>>> mhj4_branch

def shoot(command):
    if command == 'zero':
        #zero_position
        shooting_motor.run_until_stalled(-5000,Stop.COAST,duty_limit=80)
    elif command == 'shoot':
        #shooting
<<<<<<< HEAD
        shooting_motor.run(1000000)
        time.sleep(0.1)
=======
        shooting_motor.run(2300)
        time.sleep(0.25)
>>>>>>> mhj4_branch
        shooting_motor.stop()

#==========[process_uart_data]========== 
def process_uart_data(data):
    try:
        # 데이터를 문자열로 디코드 (키워드 인자 제거)
        data_str = data.decode().strip()
        if not data_str:
            return []

        # 문자열에서 리스트 파싱
        data_str = data_str.strip("[]")
        parsed_list = [list(map(int, item.split(','))) for item in data_str.split(";")]

        # 파싱된 결과 반환
        return parsed_list
    except:
        # 에러 처리
        return []  # 빈 리스트 반환


#==========[setup]==========
<<<<<<< HEAD
=======
ev3.speaker.beep()
>>>>>>> mhj4_branch
threshold = 80
previous_error = 0
gyro.reset_angle(0)
#==========[zero set position setting]==========
shoot('zero') #shoot 모터가 안쪽이고,
grab('motion3') #grab 모터가 바깥쪽이므로 shoot먼저 세팅 후 grab을 세팅해야한다
time.sleep(0.5)
grab('motion1') #공을 잡기 위한 높이로 열기

print("Zero set postion completed")

#==========[main loop]========== 
while True:
    print("Entering main loop")
    data = ser.read_all()
<<<<<<< HEAD
    
    # 컬러 센서 값 확인
    detected_color = cs.color()
    
    if detected_color == Color.GREEN:
        robot.straight(-300)
        continue  # 초록색을 인식했으면 나머지 로직 건너뛰기
    
    try:
        # UART 데이터 처리
        filter_result = process_uart_data(data)
        #filter_result[0] : x, filter_result[1] : y
        if filter_result[0]!= -1 and filter_result[1]!= -1:
        # if filter_result[0]!= -1 and filter_result[1]!= -1:
            if filter_result[1] > 100: #공이 카메라 화면 기준으로 아래에 위치 = 로봇에 가까워졌다
                robot.straight(225) #강제로 앞으로 이동
                grab('motion3') #공을 잡기
                time.sleep(0.2) #동작간 딜레이f
                grab('motion1') #슛을 위한 열기
                time.sleep(0.5)
                shoot('shoot') #공 날리기
                time.sleep(0.5) #동작간 딜레이
                robot.straight(-280)
                shoot('zero')
                grab('motion2') 
            else: #공이 카메라 화면 기준 멀리 위치해 있으면 chase한다
                pd_control(filter_result[0], kp=0.7, kd=0.1, power=100)
        # else: # 센서가 공을 보지 못했을 경우의 움직임.
        #     robot.straight(50)
        #     robot.turn(10)

        time.sleep_ms(50)
=======
    try:
        # 데이터 처리 및 결과 필터링
        filter_results = process_uart_data(data) 

        if filter_results:
            # 가장 가까운 공 선택 (Y 값 기준으로 정렬)
            filter_results.sort(key=lambda ball: ball[1], reverse=True)  # Y 값이 큰 공이 더 가까움
            closest_ball = filter_results[0]  # 가장 가까운 공 선택

            # 공이 가까운 경우
            if closest_ball[1] > 90:  # 공이 로봇에 가까워졌을 때
                robot.straight(150)  # 강제로 앞으로 이동
                grab('motion3')  # 공을 잡기
                time.sleep(2)  # 동작 간 딜레이
                grab('motion1')  # 슛을 위한 열기
                shoot('shoot')  # 공 날리기
                time.sleep(0.5)  # 동작 간 딜레이
                shoot('zero')
                grab('motion2')  # 초기화
            else:
                # 공을 따라가는 동작
                pd_control(closest_ball[0], kp=0.5, kd=0.1, power=100)
        else:
            # 센서가 공을 보지 못했을 경우 탐색 동작 수행
            robot.straight(50)
            robot.turn(30)
            robot.turn(-60)
            robot.turn(60)

        time.sleep(0.05)
>>>>>>> mhj4_branch
    except:
        pass

while True:
    try:
        data = ser.read_all()
        filter_result = process_uart_data(data)
        if filter_result[0]!= -1 and filter_result[1]!= -1:
            print(filter_result)
<<<<<<< HEAD
            pd_control(filter_result[0], kp=0.7, kd=0.1, power=100)
=======
            pd_control(filter_result[0], kp=0.5, kd=0.1, power=100)
>>>>>>> mhj4_branch
        wait(10)
    except:
        pass
        
