
def identify():
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    import time
    import os
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # 打開評分網站
    driver.get('https://beauty.buyaocha.com/')
    # 等待網頁加載完成
    time.sleep(2)
    # 找到圖片上傳按鈕，點擊後彈出文件選擇對話框
    upload_button = driver.find_element_by_xpath('//*[@id="validatedCustomFile"]')
    upload_button.send_keys(os.getcwd() + '/2.jpg')
    js2 = "var q=document.getElementById('inputSubmit').click()"
    driver.execute_script(js2)
    time.sleep(3)
    result = driver.page_source
    soup = BeautifulSoup(result,parser='html.parser',features='lxml')
    driver.quit()
    table = soup.find('div',{"class" : "p-3 mt-2 bg-success text-white"})
    grade = table.find('h4').find('span').string
    result = table.find_all('td')
    a = [grade]
    for i in result:
        a.append(i.find("strong").string.strip())
    return {"分數":a[0],"年齡":a[1],"性別":a[2],"臉型":a[3],"emoji":a[4],"種族":a[5],"是否戴眼鏡":a[6]}

if __name__ == '__main__':
    print(identify())
    
    
