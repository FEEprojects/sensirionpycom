import sensirion_sps030
from time import sleep

RX_DELAY_S = 1
LOOP_DELAY_S = 1  # cannot poll new reading within one second

SPS030 = sensirion_sps030.Sensirion()  # automatically starts measurement
sleep(RX_DELAY_S)  # wait for sensor to initialize

while True:  # start reading measurements
    data = SPS030.read()
    print(data)
    sleep(LOOP_DELAY_S)
