#!/usr/bin/python
# -*- coding: utf-8 -*-
from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # 使用BCM引脚模式

channel = 17    # 使用BCM17(对应物理引脚号11)接口控制开关
start_temp = 55 # 启动风扇的温度阈值(℃)
end_temp = 48   # 关闭风扇的温度阈值(℃)

GPIO.setup(channel, GPIO.OUT, initial = GPIO.LOW) # 初始化控制引脚
is_high = GPIO.LOW # 用于标记风扇是否打开 避免频繁调用output

try:
    while True:
        # 获取当前SoC温度
        temp = open('/sys/class/thermal/thermal_zone0/temp')
        temp = int(temp.read()) / 1000

        if temp > start_temp and not is_high: # 当SoC温度超过启动阈值且风扇处于关闭状态
            GPIO.output(channel, GPIO.HIGH)   # 打开风扇
            is_high = GPIO.HIGH               # 标记风扇状态为打开

        elif temp < end_temp and is_high:     # 当SoC温度低于关闭阈值且风扇处于打开状态
            GPIO.output(channel, GPIO.LOW)    # 关闭风扇
            is_high = GPIO.LOW                # 标记风扇状态为关闭

        sleep(10) # 每隔10秒监控一次
except:
    pass
# 退出时 重置该引脚
GPIO.cleanup(channel)
