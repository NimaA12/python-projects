
from machine import Pin
from time import ticks_ms()


def click_race():
    cnt = 0
    tick = 0
    p4 = Pin(4, Pin.IN)
    old_value = p4.value()
    start = ticks_ms() 
    while ticks_ms()-start < 10_000: 
        p4_value = p4.value()
        if p4_value != old_value :
            cnt += 1
            print(cnt/2)
        old_value = p4_value
        tick += 1
    return cnt / 2

click_race()
