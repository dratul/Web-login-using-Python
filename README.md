# Firewall login using python
In this repository, there are two programs for Automatic Firewall login using Python 
## Prerequisites
You should have installed python version 3.0 or above 
Here are the steps to prepare you to be able to open a webpage and log in using Python and some third-party applications:

1. Setting up your workspace
2. Downloading the necessary tools
3. How to hide our passwords
4. Reviewing necessary imports
Watch
[YouTube video] (https://youtu.be/NMVEU2KSY84?si=wdo0_F1TcHGYz8Hy) link showing all steps Click on the link below to watch the video: https://youtu.be/NMVEU2KSY84?si=wdo0_F1TcHGYz8Hy

## Downloads

### ChromeDriver or Edge Driver
If you are using Google Chrome, download Chromedriver, or if you are using Microsoft Edge, then use EdgeDriver. You can download the program by searching for it on Google.

Once on the page, choose the appropriate link for your Chrome version. Then you will choose the appropriate link according to your system. If you are on Windows, the 32-bit link works regardless. You will then be downloading a zip file. Once downloaded, we will move this zip file and extract it into the folder we have created. If you get stuck here, here is a video of how to download ChromeDriver for Windows and Mac.

### Selenium
Selenium is a great program for working with automation and web applications; we will be using it for these exact purposes. The installation process for Selenium is simple; you open the command prompt by searching for "cmd" on your computer. Open the command prompt and enter the following command:
> pip install selenium 
## Save ID and password in a file
If we must show our passwords while using this program, we are not really able to show them off to our friends, and where is the fun in that? In this article, I will show you a way to keep your login information hidden so you can share it with friends without worrying about security. We will be creating another file and calling it "login_details.py." We are going to keep this file as basic as possible, inserting only 2 lines of code:

```python
username = "username"
password = "password"
```
That is it. We will be importing this file into our main program code, so when we want to show anyone our file, the username and password will be hidden in our secret file.
### Main Program
Initially, we import libraries and packages
We import the modules required for the program. Beginning with Webdriver, it allows us to use our Python code to create test scripts. It is a web framework that allows for cross-browser testing. This tool will allow us to connect to a bunch of APIs and use them to test our web application.

The next line: from selenium.webdriver.common.by import By. This line allows us to locate elements by a specific name, like the variable ID or class_name. This is important as find_element() is a key part of this program, and understanding it is crucial.
The next line import login_details. Our program is able to communicate with our secret password file and get us that information. Without this, we have no username and password.
I want to repeat this code again and again therefore written a code which imports time library in the last line of importing library and packages
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import login_details
import time
```
The next thing to go for is web automation, which is also called web scraping. The program grab the content of sites using ids awailable in the content. 
We will need to locate certain IDs for this program and this is good knowledge to have about the internet and browser. 
When we will be using the function find_element(By.id, "ID") We need to locate that ID first because the function needs it,
I have shown this in my youtube video https://youtu.be/NMVEU2KSY84?si=wdo0_F1TcHGYz8Hy
Whenever you want to find out about the properties of an object right-click on the object and then click inspect. 
So, hover over the "Email" box and inspect it. We can then see all properties, we are looking for the id which looks like, id="username". 
This is how you find the properties of certain objects. 
Once you inspect the email we are looking for a piece of code that looks like this, then we are copying id which is "username"
now the program will look like

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import login_details
import time
username = login_details.username
password = login_details.password
driver = webdriver.Edge()
driver.maximize_window()
while(True):
    driver.get("http://172.16.40.5:8090/")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID,"loginbutton").click()
    time.sleep(300)
    #driver.quit()
```
