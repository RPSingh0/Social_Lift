import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
gecko = os.getcwd()
options = Options()
options.add_argument("--headless")


def create_post(email_number, password, caption, file_path=None):
    """Arguements:\n
            1. email_number [str] -> takes an email/number registered with your facebook account.\n
            2. password [str] -> password for yor account.\n
            3. caption [str] -> caption for post.\n
            4. file_path [raw-str] -> photo/video path to be uploaded\.n\n

        Returns: [str] object\n
            1. Failed to login, check your credentials, if the user credentials as incorrect.\n
            2. Success, if post was created successfully.\n
            3. Something went wrong!, if any internel error happened\n"""
    driver = webdriver.Firefox(
        executable_path=gecko+"\social_lift\geckodriver.exe", options=options)
    driver.get("https://www.facebook.com/")
    try:
        print("Started")
        email = driver.find_element_by_name("email")
        email.send_keys(email_number)
        sleep(1)
        pswrd = driver.find_element_by_name("pass")
        pswrd.send_keys(password)
        sleep(1)
        login = driver.find_element_by_name("login")
        login.click()
        sleep(3)
        home = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]")
        home.click()
        sleep(5)
        try:
            home = driver.find_element_by_xpath(
                "//span[contains(text(),'on your mind')]")
            home.click()
            print("Login Sucessfull...")
        except:
            return("Failed to login, check your credentials")
        sleep(3)
        print("Adding caption...")
        active = driver.switch_to_active_element()
        active.send_keys(caption)
        print("Uploading media...")
        sleep(1)
        photo = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div/div/div[1]/div/div/div[1]/i")
        photo.click()
        photo = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[1]/div/span/span")
        photo.click()
        sleep(15)
        print("Posting...")
        post = driver.find_element_by_xpath(
            "//span[contains(text(), 'Post')]")
        post.click()
        sleep(10)
        driver.close()
        return("Success")
    except:
        return("Something went wrong!")


# create_post("anonymous.it.iter@gmail.com", "elgooghtiwpungiS",
#             "kaise ho bhaiyon hello there?", r"C:\Users\john1\Pictures\Capturex.PNG")
