import time
import os.path
from parameter import *
import urllib.request
import datetime as dt
import ssl
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import shutil
ssl._create_default_https_context = ssl._create_unverified_context

def Allianz_monthly_reports(month):

    if not os.path.isdir(f"{allianz_output_path}{month}"):
        os.mkdir(f"{allianz_output_path}{month}")
    urllib.request.urlretrieve(monthlyreport_url_tech_fund, f"{allianz_output_path}{month}/Allianz_tech_fund_monthly_report_{month}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_intelligence_fund, f"{allianz_output_path}{month}/Allianz_intelligence_fund_monthly_report_{month}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_global_investor_fund, f"{allianz_output_path}{month}/Allianz_global_investor_fund_monthly_report_{month}.pdf")

def yuanta_etf_monthly_csv(month):
    csv_mv_path = f"{yuanta_output_path}{month}/"
    if not os.path.isdir(csv_mv_path):
        os.mkdir(f"{csv_mv_path}")
    fl_dict={'0050.csv':yuanta_50_url,'0051.csv':yuanta_100_url}
    dl_path = str(Path.home() / "Downloads/")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    for file,url in fl_dict.items():
        # chromeOptions = webdriver.ChromeOptions()
        # prefs = {"download.default_directory": f"{csv_dl_path}"}
        # chromeOptions.add_experimental_option("prefs", prefs)

        driver.get(url)
        driver.implicitly_wait(5)
        while not os.path.isfile(dl_path+'\\'+file):
            driver.find_element(By.XPATH, "//*[@id='productinfoR']/div/div[2]/div[3]/div/div/div[1]/div").click()
            print('sleeping')
            print(dl_path+file)
            print(f'os.isfile: {os.path.isfile(dl_path+"/"+file)}')
            print(f'list dir: {os.listdir(dl_path)}')
            time.sleep(5)
        shutil.move(os.path.join(dl_path,file),os.path.join(csv_mv_path+file))
    return driver.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    today=dt.datetime.today().strftime("%Y%m%d")
    month=(dt.datetime.today() - dt.timedelta(weeks=4)).strftime("%Y%m")
    Allianz_monthly_reports(month)
    yuanta_etf_monthly_csv(today,month)

#productinfoR > div > div:nth-child(2) > div.productinfoContent > div > div > div.sortBox > div
    
