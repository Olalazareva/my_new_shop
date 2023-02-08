# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account =  driver.find_element_by_link_text('My Account')
# my_account.click()
# login_username =  driver.find_element_by_id('username')
# login_username.send_keys('olalazareva@gmail.com')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Natalishechka!1971')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# book = driver.find_element_by_class_name('post-181')
# book.click()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# book_name = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "entry-title"), "HTML5 Forms"))
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account =  driver.find_element_by_link_text('My Account')
# my_account.click()
# login_username =  driver.find_element_by_id('username')
# login_username.send_keys('olalazareva@gmail.com')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Natalishechka!1971')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# html = driver.find_element_by_link_text('HTML')
# html.click()
# html_shop = driver.find_elements_by_class_name('product_tag-html')
# if len(html_shop) == 3:
#     print('True')
# else:
#     print('False'+ str(len(html_shop)))
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account =  driver.find_element_by_link_text('My Account')
# my_account.click()
# login_username =  driver.find_element_by_id('username')
# login_username.send_keys('olalazareva@gmail.com')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Natalishechka!1971')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# order = driver.find_element_by_class_name("orderby")
# element_check = order.get_attribute("value")
# assert element_check == "menu_order"
# from selenium.webdriver.support.select import Select
# price_desc = driver.find_element_by_class_name("orderby")
# select = Select(price_desc)
# select.select_by_value("price-desc")
# time.sleep(3)
# price_desc = driver.find_element_by_class_name("orderby")
# element_check = price_desc.get_attribute("value")
# assert element_check == "price-desc"
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account =  driver.find_element_by_link_text('My Account')
# my_account.click()
# login_username =  driver.find_element_by_id('username')
# login_username.send_keys('olalazareva@gmail.com')
# login_password = driver.find_element_by_id('password')
# login_password.send_keys('Natalishechka!1971')
# login = driver.find_element_by_name('login')
# login.click()
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# start_guide = driver.find_element_by_class_name('post-169')
# start_guide.click()
# old_price = driver.find_element_by_css_selector('p > del > span')
# old_price_text = old_price.text
# assert old_price.text == '₹600.00'
# new_price = driver.find_element_by_css_selector('p > ins > span')
# new_price_text = new_price.text
# assert new_price.text == '₹450.00'
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# pre_open = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "wp-post-image")) )
# pre_open.click()
# close_window = WebDriverWait(driver, 10).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) )
# close_window.click()
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# webb_app_book = driver.find_element_by_class_name('post-165')
# webb_app_book.click()
# quantity = driver.find_element_by_class_name('qty')
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == '1'
# price = driver.find_element_by_css_selector('div:nth-child(2) > p > span')
# price_text = price.text
# assert price.text == '₹350.00'
# add_to_cart = driver.find_element_by_css_selector('form > button')
# add_to_cart.click()
# view_basket = driver.find_element_by_css_selector('div.woocommerce-message > a')
# view_basket.click()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# subtotal = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td"), "₹350.00"))
# total = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total > td"), "₹357.00"))
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 1200);")
# time.sleep(5)
# java_book = driver.find_element_by_css_selector('.add_to_cart_button.ajax_add_to_cart')
# java_book.click()
# time.sleep(3)
# basket = driver.find_element_by_class_name('wpmenucart-contents')
# basket.click()
# time.sleep(3)
# remove = driver.find_element_by_css_selector('td.product-remove > a')
# remove.click()
# time.sleep(3)
# undo = driver.find_element_by_link_text('Undo?')
# undo.click()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector("td.product-quantity > div >input")
# quantity.clear()
# time.sleep(3)
# quantity.send_keys("3")
# update = driver.find_element_by_name('update_cart')
# update.click()
# time.sleep(3)
# new_quantity = driver.find_element_by_css_selector("td.product-quantity > div >input")
# element_check = new_quantity.get_attribute("value")
# assert element_check == "3"
# time.sleep(3)
# coupon = driver.find_element_by_name('apply_coupon')
# coupon.click()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# code = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# driver.quit()


# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# shop = driver.find_element_by_link_text('Shop')
# shop.click()
# time.sleep(3)
# driver.execute_script("window.scrollBy(0, 1200);")
# time.sleep(5)
# java_book = driver.find_element_by_css_selector('.add_to_cart_button.ajax_add_to_cart')
# java_book.click()
# time.sleep(3)
# basket = driver.find_element_by_class_name('wpmenucart-contents')
# basket.click()
# time.sleep(3)
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# proceed = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
# proceed.click()
# time.sleep(3)
# first_name = driver.find_element_by_id('billing_first_name')
# first_name.send_keys('Olga')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Lazareva')
# e_mail = driver.find_element_by_id('billing_email')
# e_mail.send_keys('olalazareva@gmail.com')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('78123040448')
# time.sleep(3)
# country =driver.find_element_by_id('s2id_billing_country')
# country.click()
# ru = driver.find_element_by_id('s2id_autogen1_search')
# ru.send_keys("russ")
# russia = driver.find_element_by_class_name('select2-match')
# russia.click()
# street = driver.find_element_by_id('billing_address_1')
# street.send_keys('Zemski')
# city = driver.find_element_by_id('billing_city')
# city.send_keys('St. Petersburg')
# state = driver.find_element_by_id('billing_state')
# state.send_keys('nord-west')
# time.sleep(1)
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys("191014")
# time.sleep(1)
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check_payment = driver.find_element_by_id('payment_method_cheque')
# check_payment.click()
# place_order = driver.find_element_by_id('place_order')
# place_order.click()
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# thanks = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received"))
# method = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "method"), "Check Payments"))
# driver.quit()

