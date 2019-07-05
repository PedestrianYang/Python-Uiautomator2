from time import sleep

import uiautomator2 as u2

class AutoTest:
    def __init__(self):
        self.d = u2.connect('192.168.2.7')
        self.d.app_start('com.iyunshu.android.apps.client')
        self.d.wait_activity('com.iyunshu.android.apps.client.ui.MainActivity', timeout=10)

    def complete(self):
        self.d.app_stop_all()

    def homeModule(self):
        sleep(5)
        for i in range(10):
            self.d(resourceId="com.iyunshu.android.apps.client:id/home_banner").swipe("left")
        sleep(2)
        for i in range(10):
            self.d(resourceId="com.iyunshu.android.apps.client:id/home_banner").swipe("right")
        sleep(2)
        self.d(resourceId="android:id/list").scroll.toEnd()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/iv_back_top", className="android.widget.ImageView").click()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorOneItemImg").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorOneItemImg", className="android.widget.ImageView", instance=1).click()
        self.goBack()
        sleep(2)
        self.d(className="android.widget.LinearLayout", instance=10).click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.3)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorTwoImgOne", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.3)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorTwoImgFive", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.3)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorFiveImg1", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.3)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorFiveImg6", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.3)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorSixImg1", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorSixImg6", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorSevenImg1", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mFloorSevenImg6", className="android.widget.ImageView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mRlCon1").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mRlCon1", className="android.widget.RelativeLayout", instance=1).click()
        self.goBack()
        sleep(2)
        self.d(resourceId="android:id/list").session.swipe(0.5, 0.5, 0.5, 0.2)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/iv_back_top", className="android.widget.ImageView").click()
        self.searchModule()


    def searchModule(self):
        self.d(resourceId="com.iyunshu.android.apps.client:id/tv_search").click()
        sleep(1)
        if self.d(resourceId="com.iyunshu.android.apps.client:id/iv_clear_search", className="android.widget.ImageView").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/iv_clear_search", className="android.widget.ImageView").click()
            self.d(resourceId="com.iyunshu.android.apps.client:id/left_button", text=u"否", className="android.widget.TextView").click()
            self.d(resourceId="com.iyunshu.android.apps.client:id/iv_clear_search", className="android.widget.ImageView").click()
            self.d(resourceId="com.iyunshu.android.apps.client:id/right_button", text=u"是", className="android.widget.TextView").click()


        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/edit_search").set_text("111")
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/tv_auto_name").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mLvAutoCom").session.swipe(0.5, 0.5, 0.5, 0.2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/mLvAutoCom").session.swipe(0.5, 0.5, 0.5, 0.7)
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/edit_search").set_text("iphone")
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/tv_auto_name", text=u"Apple/苹果 iPhone 8 Plus  iphone8   5.5英寸手机", className="android.widget.TextView").click()
        self.goBack()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/image_clear", className="android.widget.ImageView").click()

        if self.d(resourceId="com.iyunshu.android.apps.client:id/taglistview_hotword").sibling(className="android.widget.ToggleButton").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/taglistview_hotword").sibling(className="android.widget.ToggleButton")[0].click()
            self.goBack()
            self.d(resourceId="com.iyunshu.android.apps.client:id/taglistview_hotword").sibling(className="android.widget.ToggleButton")[1].click()
            self.goBack()
        sleep(2)
        self.d(resourceId="com.iyunshu.android.apps.client:id/edit_search").set_text("苹果")
        self.d(resourceId="com.iyunshu.android.apps.client:id/btn_begin_search").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/mRlCon1").click()
        self.goBack()
        self.goBack()
        self.goBack()

    def subOrder(self):
        self.d(resourceId="com.iyunshu.android.apps.client:id/tv_search").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/edit_search", text=u"搜索商品", className="android.widget.EditText").set_text("测试")
        self.d(resourceId="com.iyunshu.android.apps.client:id/btn_begin_search", text=u"搜索", className="android.widget.TextView").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/mRlCon1", className="android.widget.RelativeLayout", instance=1).click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/goods_buy", text=u"立即购买", className="android.widget.TextView").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/settle_submit", text=u"提交订单", className="android.widget.Button").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/mTVPosPay", text=u"立即支付", className="android.widget.TextView").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/order_pay_result_usercenter", text=u"我知道了", className="android.widget.Button").click()
        self.goBack()
        self.goBack()
        self.goBack()

    def cancelOrder(self):
        self.d(resourceId="com.iyunshu.android.apps.client:id/tab_icon_4", className="android.widget.ImageView").click()
        self.d(resourceId="com.iyunshu.android.apps.client:id/user_center_myorder_waitdeliver", className="android.widget.LinearLayout").click()
        sleep(2)
        childCount = self.d(resourceId="android:id/list", className="android.widget.ListView").child(resourceId="com.iyunshu.android.apps.client:id/container").count
        if childCount > 0:
            while childCount > 0:
                if not self.d(resourceId="com.iyunshu.android.apps.client:id/wait_deliver_order_cancel", text=u"取消订单", className="android.widget.TextView").exists():
                    print("没有取消订单按钮")
                    break
                self.d(resourceId="com.iyunshu.android.apps.client:id/wait_deliver_order_cancel", text=u"取消订单", className="android.widget.TextView").click()
                self.d(resourceId="com.iyunshu.android.apps.client:id/right_button", text=u"确认", className="android.widget.TextView").click()
                self.d(resourceId="com.iyunshu.android.apps.client:id/left_button", text=u"确定", className="android.widget.TextView").click()
                childCount = self.d(resourceId="android:id/list", className="android.widget.ListView").child(resourceId="com.iyunshu.android.apps.client:id/container").count
        self.goBack()
        self.d(resourceId="com.iyunshu.android.apps.client:id/user_center_myorder_waitpay", className="android.widget.LinearLayout").click()
        sleep(2)
        childCount = self.d(resourceId="android:id/list", className="android.widget.ListView").child(resourceId="com.iyunshu.android.apps.client:id/container").count
        if childCount > 0:
            while childCount > 0:
                if not self.d(resourceId="com.iyunshu.android.apps.client:id/wait_pay_order_cancel", text=u"取消订单", className="android.widget.TextView").exists():
                    print("没有取消订单按钮")
                    break
                self.d(resourceId="com.iyunshu.android.apps.client:id/wait_pay_order_cancel", text=u"取消订单", className="android.widget.TextView", ).click()
                self.d(resourceId="com.iyunshu.android.apps.client:id/right_button", text=u"确认", className="android.widget.TextView").click()
                self.d(resourceId="com.iyunshu.android.apps.client:id/left_button", text=u"确定", className="android.widget.TextView").click()
                childCount = self.d(resourceId="android:id/list", className="android.widget.ListView").child(resourceId="com.iyunshu.android.apps.client:id/container").count
        self.goBack()

    def goBack(self):
        if self.d(resourceId="com.iyunshu.android.apps.client:id/title_back").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/title_back").click()
        elif self.d(resourceId="com.iyunshu.android.apps.client:id/mGoodsListBackImg").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/mGoodsListBackImg").click()
        elif self.d(resourceId="com.iyunshu.android.apps.client:id/title_back").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/title_back").click()
        elif self.d(resourceId="com.iyunshu.android.apps.client:id/titlebar_left_imageview").exists():
            self.d(resourceId="com.iyunshu.android.apps.client:id/titlebar_left_imageview").click()
        else:
            self.d.press("back")

if __name__ == '__main__':
    aaa = AutoTest()
    aaa.cancelOrder()
    # aaa.complete()
