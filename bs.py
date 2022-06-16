from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def login(flag_xpath,user_xpath,lpwd_xpath,submit_xpath,login_xpath,url,account,passwd):
    driver.get(url)
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, flag_xpath)))
    user = driver.find_element(By.XPATH,user_xpath)
    user.clear()
    user.send_keys(account)
    driver.find_element(By.XPATH,lpwd_xpath).send_keys(passwd)
    driver.find_element(By.XPATH,submit_xpath).click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, login_xpath)))
    print("login successfully!")
    return True


def changeandverify(setting_xpath,center_xpath,pwd_xpath,start_xpath,oldpwd_xpath,newpwd_xpath,verify_xpath,done_xpath,newpwd,oldpwd,suc_xpath,exit_xpath):
    print("loading change passwd...")
    set = driver.find_element(By.XPATH,setting_xpath)
    set.click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,center_xpath)))
    driver.find_element(By.XPATH,center_xpath).click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,pwd_xpath)))
    driver.find_element(By.XPATH,pwd_xpath).click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH,start_xpath)))
    ow = driver.find_element(By.XPATH,oldpwd_xpath)
    ow.click()
    ow.send_keys(oldpwd)
    nw = driver.find_element(By.XPATH,newpwd_xpath)
    nw.click()
    nw.send_keys(newpwd)
    rnw = driver.find_element(By.XPATH,verify_xpath)
    rnw.click()
    rnw.send_keys(newpwd)
    driver.find_element(By.XPATH,done_xpath).click()
    WebDriverWait(driver,60).until(expected_conditions.visibility_of_element_located((By.XPATH,suc_xpath)))
    print("change finished.")
    set.click()
    driver.find_element(By.XPATH,exit_xpath).click()
    WebDriverWait(driver,60).until(expected_conditions.visibility_of_element_located((By.XPATH,flag_xpath)))
    print("starting verify...")
    vuser = driver.find_element(By.XPATH, user_xpath)
    vuser.click()
    vuser.send_keys(account)
    driver.find_element(By.XPATH, lpwd_xpath).send_keys(newpwd)
    driver.find_element(By.XPATH, submit_xpath).click()
    WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, login_xpath)))
    print("login successfully!")
    print("TOTALLY SUCCESFULLY!!!")

    return True



if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)

    flag_xpath = '//*[@id="loginDiv"]/div/section[1]/header/span'
    user_xpath = '//*[@id="inputUserName"]'
    lpwd_xpath = '//*[@id="inputPassword"]'
    submit_xpath = '//*[@id="loginBtn"]'
    login_xpath = '/html/body/qz-main/qz-nav/header/div[1]/a/img'
    url = 'https://10.2.223.6'
    account = 'bs_test'
    passwd = 'xxxx'
    #ris
    login(flag_xpath, user_xpath, lpwd_xpath, submit_xpath, login_xpath, url, account, passwd)

    #登录51cto
    #login('//*[@id="app"]/div/div/div/div[1]/div[2]/form[1]/p/span','//*[@id="app"]/div/div/div/div[1]/div[2]/form[1]/div[1]/div/div/input','//*[@id="app"]/div/div/div/div[1]/div[2]/form[1]/div[2]/div/div/input','//*[@id="app"]/div/div/div/div[1]/div[2]/form[1]/button','/html/body/div[5]/div/div[2]/div[1]','http://saas.51cto.com/','18700000001','88888888')
    setting_xpath = '/html/body/qz-main/qz-nav/header/div[2]/div[2]'
    center_xpath = '/html/body/qz-main/qz-nav/header/div[2]/div[2]/menu/ul/li[1]/a'
    pwd_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tabs/ul/ng-transclude/qz-tab[2]/li/a/ng-transclude/span'
    #change_xpath = '//*[@id="app"]/div/div[2]/div[2]/div/div/form/div[1]/div[5]/div/button'
    start_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tab-content/div/ng-transclude/qz-tab-pane/div/ng-transclude/ng-outlet/qz-update-password/form/div[4]/div/button[1]'
    oldpwd_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tab-content/div/ng-transclude/qz-tab-pane/div/ng-transclude/ng-outlet/qz-update-password/form/div[1]/div/input'
    newpwd_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tab-content/div/ng-transclude/qz-tab-pane/div/ng-transclude/ng-outlet/qz-update-password/form/div[2]/div/input'
    verify_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tab-content/div/ng-transclude/qz-tab-pane/div/ng-transclude/ng-outlet/qz-update-password/form/div[3]/div/input'
    done_xpath = '/html/body/qz-main/ng-outlet/qz-loginuser/main/ng-outlet/qz-basic-info/section/div/qz-tab-content/div/ng-transclude/qz-tab-pane/div/ng-transclude/ng-outlet/qz-update-password/form/div[4]/div/button[2]'
    oldpwd = 'xxxxx'
    newpwd = 'xxx'
    suc_xpath = '/html/body/qz-main/div[5]/div'
    exit_xpath = '/html/body/qz-main/qz-nav/header/div[2]/div[2]/menu/ul/li[4]/a'
    changeandverify(setting_xpath, center_xpath, pwd_xpath, start_xpath, oldpwd_xpath, newpwd_xpath, verify_xpath,done_xpath, newpwd, oldpwd,suc_xpath,exit_xpath)





