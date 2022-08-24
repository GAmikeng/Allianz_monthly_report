import os.path
from parameter import *
import urllib.request
import datetime as dt




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    today=dt.datetime.today().strftime("%Y%m%d")
    month=dt.datetime.today().strftime("%Y%m")
    if not os.path.isdir(f"{output_path}{month}"):
        os.mkdir(f"{output_path}{month}")
    urllib.request.urlretrieve(monthlyreport_url_tech_fund, f"{output_path}{month}/Allianz_tech_fund_monthly_report_{today}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_intelligence_fund, f"{output_path}{month}/Allianz_intelligence_fund_monthly_report_{today}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_global_investor_fund, f"{output_path}{month}/Allianz_global_investor_fund_monthly_report_{today}.pdf")
    
