from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 로그인 정보
username = "your_username"
password = "your_password"

# 브라우저 실행 및 인증 정보 설정
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
browser.find_element_by_name("username").send_keys(username)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_xpath("//button[contains(.,'로그인')]").click()
time.sleep(2)

# 업로드할 포스트의 이미지 파일 선택
image_path = "/path/to/image.jpg"
browser.find_element_by_css_selector("[data-testid='new-post-button']").click()
time.sleep(2)
browser.find_element_by_css_selector("[aria-label='포스트 게시']").send_keys(image_path)
time.sleep(2)

# 캡션 작성 및 업로드
caption = "포스트 캡션입니다. #해시태그 #인스타그램"
browser.find_element_by_xpath("//button[contains(.,'다음')]").click()
time.sleep(2)
browser.find_element_by_css_selector("[aria-label='캡션 추가']").send_keys(caption)
browser.find_element_by_xpath("//button[contains(.,'공유')]").click()
time.sleep(2)

# 브라우저 종료
browser.quit()