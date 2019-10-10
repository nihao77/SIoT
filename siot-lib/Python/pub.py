'''# file pub.py# brief         Set 'SERVER','CLIENT_ID'(this can be null),'IOT_pubTopic','IOT_UserName','IOT_PassWord'#               download into pc or raspberryPi and run the file#               You will send the message by seconds# Copyright     Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)# licence       The MIT License (MIT)# author        [LuoYufeng](yufeng.luo@dfrobot.com)# version       V1.0# date          2019-10-8'''from siot import iotimport timeSERVER = "127.0.0.1"            #MQTT服务器IPCLIENT_ID = ""                  #在SIoT上，CLIENT_ID可以留空IOT_pubTopic  = 'xzr/001'       #“topic”为“项目名称/设备名称”IOT_UserName ='siot'            #用户名IOT_PassWord ='dfrobot'         #密码siot = iot(CLIENT_ID, SERVER, user=IOT_UserName, password=IOT_PassWord)siot.connect()siot.loop()tick = 0try:    while True:        siot.publish(IOT_pubTopic, "value %d"%tick)        time.sleep(1)           #隔1秒发送一次        tick = tick+1except:    siot.stop()    print("disconnect seccused")