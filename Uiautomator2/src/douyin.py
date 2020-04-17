import random
import uiautomator2 as u2
import subprocess
import threading
import time

class AutoRushD:
    def __init__(self):
        self.threads = []
        threads = []
        for i in range(len(getphonelist())):
            threads.append(threading.Thread(target=self.action(getphonelist()[i]),args=()))
        for t in threads:
            time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()

    def action(self, device):
        self.d = u2.connect(device)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
        self.d.app_start('com.ss.android.ugc.aweme.lite')
        while True:
            self.d(className="android.view.View", instance=4).swipe("up")
            time.sleep(random.randint(5,15))

class AutoRushK:
    def __init__(self):
        self.threads = []
        threads = []
        for i in range(len(getphonelist())):
            threads.append(threading.Thread(target=self.action(getphonelist()[i]),args=()))
        for t in threads:
            time.sleep(0.3)
            t.start()
        for t in threads:
            t.join()

    def action(self, device):
        self.d = u2.connect(device)  # d = u2.connect('192.168.1.117')#  uiautomator2 连接手机
        self.d.app_start('com.kuaishou.nebula')
        while True:
            self.d(resourceId="com.kuaishou.nebula:id/player").swipe("up")
            time.sleep(random.randint(5,15))


def getphonelist():  # 获取手机设备
    cmd = r'adb devices'  # % apk_file
    pr = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    pr.wait()  # 不会马上返回输出的命令，需要等待
    out = pr.stdout.readlines()  # out = pr.stdout.read().decode("UTF-8")
    devices = []
    for i in (out)[1:-1]:
        device = str(i).split("\\")[0].split("'")[-1]
        devices.append(device)

    return devices  # 手机设备列表



if __name__ == '__main__':
    str1 = input("1：抖音 2：快手：/n");
    if str1 == '1':
        aaa = AutoRushD()
    else:
        aaa = AutoRushK()

