import serial
import time

# 시리얼 포트 연결 (포트와 보드레이트는 장치에 맞게 설정)
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Windows: 'COM3', Linux: '/dev/ttyUSB0'
time.sleep(2)  # 시리얼 연결 안정화

# 앞으로 움직이라는 명령어 전송
def move_forward():
    command = 'FORWARD\n'  # 장치에서 인식할 명령어 형식
    ser.write(command.encode())
    print("Lamp is moving forward")

# 실행
move_forward()

# 시리얼 연결 종료
ser.close()
