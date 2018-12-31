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
setting_address_manage =By.ID,"com.yunmall.lc:id/setting_address_manage"

"""
地址管理
"""
address_manage_back =By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
address_manage_editor_save =By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
address_manage_new_add_address =By.ID,"com.yunmall.lc:id/address_add_new_btn"
address_manage_modify_address =By.ID,"com.yunmall.lc:id/modify"
address_manage_delete_address =By.ID,"com.yunmall.lc:id/delete"

"""
新增地址/更新地址
"""
new_adress_back =By.ID,"com.yunmall.lc:id/back"
new_adress_save =By.ID,"com.yunmall.lc:id/button_send"
new_adress_receipt_name =By.ID,"com.yunmall.lc:id/address_receipt_name"
new_adress_phone =By.ID,"com.yunmall.lc:id/address_add_phone"
new_adress_province =By.ID,"com.yunmall.lc:id/address_province"
new_adress_detail_address =By.ID,"com.yunmall.lc:id/address_detail_addr_info"
new_adress_post_code =By.ID,"com.yunmall.lc:id/address_post_code"

"""
删除地址
"""
del_address_accept=By.ID,"com.yunmall.lc:id/ymdialog_left_button"
del_address_cancel=By.ID,"com.yunmall.lc:id/ymdialog_right_button"


"""
省/直辖市
"""
select_area=By.ID,"com.yunmall.lc:id/area_title"



