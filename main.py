from parameter import *
import urllib.request
import datetime as dt




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    today=dt.datetime.today().strftime("%y%m%d")
    print(today)
    urllib.request.urlretrieve(monthlyreport_url_tech_fund, f"output/Allianz_tech_fund_monthly_report_{today}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_intelligence_fund, f"output/Allianz_intelligence_fund_monthly_report_{today}.pdf")
    urllib.request.urlretrieve(monthlyreport_url_global_investor_fund, f"output/Allianz_global_investor_fund_monthly_report_{today}.pdf")

