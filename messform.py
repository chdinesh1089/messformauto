import selenium
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as FirefoxOptions
mails =['smeier@hotmail.com','cgreuter@aol.com','grolschie@sbcglobal.net','jamuir@icloud.com','jginspace@yahoo.com','kdawson@verizon.net','carcus@msn.com','wortmanj@outlook.com','dgriffith@comcast.net','frode@live.com','stern@gmail.com','hstiles@verizon.net','dartlife@comcast.net','tattooman@mac.com','ilial@outlook.com','blixem@live.com','odlyzko@verizon.net','sacraver@icloud.com','malvar@att.net','mddallara@comcast.net','jfreedma@aol.com','grolschie@me.com','crandall@icloud.com','mwitte@sbcglobal.net','grdschl@outlook.com','johndo@comcast.net','crimsane@att.net','fangorn@msn.com','tkrotchko@optonline.net','frode@comcast.net','kronvold@me.com','pavel@verizon.net','citadel@comcast.net','drolsky@gmail.com','luvirini@icloud.com','mlewan@hotmail.com','kspiteri@msn.com','jaxweb@sbcglobal.net','storerm@sbcglobal.net','dhwon@outlook.com','attwood@icloud.com','jguyer@icloud.com','marioph@sbcglobal.net','cderoove@gmail.com','bescoto@sbcglobal.net','uncle@sbcglobal.net','quantaman@gmail.com','pplinux@live.com','wayward@me.com','arnold@sbcglobal.net','sonnen@gmail.com','pkplex@gmail.com','gavinls@hotmail.com','chronos@msn.com','grinder@yahoo.com','rddesign@verizon.net','vmalik@comcast.net','drewf@live.com','euice@live.com','jfinke@mac.com','empathy@me.com','noneme@aol.com','singh@comcast.net','netsfr@yahoo.com','bartak@aol.com','mjewell@att.net','joehall@sbcglobal.net','tkrotchko@outlook.com','krueger@me.com','jfinke@att.net','okroeger@aol.com','kingjoshi@msn.com','dvdotnet@aol.com','ahuillet@outlook.com','isaacson@yahoo.ca','studyabr@comcast.net','arathi@optonline.net','codex@aol.com','mxiao@yahoo.ca','kostas@outlook.com','boein@outlook.com','mdielmann@outlook.com','morain@aol.com','jaesenj@yahoo.ca','eimear@live.com','mhouston@yahoo.ca','josem@me.com','yxing@icloud.com','cvrcek@live.com','steve@aol.com','alias@yahoo.ca','pgottsch@mac.com','pappp@comcast.net','khris@icloud.com','dogdude@icloud.com','nacho@att.net','seebs@msn.com','ryanvm@live.com','aaribaud@sbcglobal.net','jesse@sbcglobal.net']
opts = FirefoxOptions()
opts.add_argument("--headless")
for mail in mails:
    driver = webdriver.Firefox(options = opts)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSed89CF0uApemSeT51htpGiNdzX6LTsjiBXecqpDRSXeycIfw/viewform')

    email = driver.find_element_by_xpath('//*[@type="email"]')
    email.send_keys(mail)

    chbx = driver.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    xs = [2,3,4,5,7,8,11,12,16,18,26,27,30,34,36,37,38,39,40,48,51,53,55,56,58,59,61,62,64,65]
    for i in xs:
        chbx[i].click()
    driver.quit()
    print(mail)

