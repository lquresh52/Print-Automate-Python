from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Desktop\Codes\Python\Print_Automate_Chrome_Page\chromedriver.exe")
driver.get("https://kjeigatepass.herokuapp.com/")
# driver.save_screenshot("D:\Desktop\Codes\Python\Print_Automate_Chrome_Page\test1.png")
driver.get_screenshot_as_file("test.png")
driver.quit()
print("Done")