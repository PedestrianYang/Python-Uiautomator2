import random
from time import sleep
import uiautomator2 as u2

class AutoRush:
    def __init__(self):
        self.d = u2.connect('192.168.2.7')
        self.d.app_start('com.ss.android.ugc.aweme.lite')
        while True:
            self.d(resourceId="com.ss.android.ugc.aweme.lite:id/awd").swipe("up")
            sleep(random.randint(5,15))




if __name__ == '__main__':
    aaa = AutoRush()
