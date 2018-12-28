from selenium.webdriver.common.by import By

# 0. 奥莱的 包名和启动名
app_package="com.android.mms"
app_activity=".ui.ConversationList"

"""
home页 首页 分类 购物车 我
"""
home_me_tab=By.ID,"com.yunmall.lc:id/tab_me"

"""
注册页 
"""
sign_in_exit_account_login=By.ID,"com.yunmall.lc:id/textView1"

"""
登录页 
"""
login_username_id = By.ID,"com.yunmall.lc:id/logon_account_textview"
login_password_id = By.ID,"com.yunmall.lc:id/logon_password_textview"
login_login_in_btn = By.ID,"com.yunmall.lc:id/logon_button"
login_login_out_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

"""
个人中心 
"""
person_center_setting_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
person_center_all_order = By.ID,"com.yunmall.lc:id/order_more_txt"

"""
设置中心 
"""
setting_center_login_out_btn =By.ID,"com.yunmall.lc:id/setting_logout"
setting_center_login_dialog_confirm_btn =By.ID,"com.yunmall.lc:id/ymdialog_right_button"

"""
toast
"""
sign_in_toast_user_no_exist =By.XPATH,"//*[contains(@text,'用户不存在')]"

