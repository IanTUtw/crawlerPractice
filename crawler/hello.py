import os
import time
import requests
import json
import pandas as pd
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 台灣證券交易所，個股日成交資訊
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210801&stockNo=0050"

# 取得股票資料json字串
response = requests.get(url)
print(response.text)

# 檢查是否有返回的數據
if "查詢日期大於今日" in response.text or "很抱歉" in response.text:
    print("無法取得有效的數據，請檢查URL或日期。")
else:
    # 從json字串轉為python的字典格式
    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    # 存成Pandas的Dataframe
    df = pd.DataFrame(datas, columns=fields)
    print(df)

    # 轉成csv檔
    df.to_csv("./month_stock.csv", encoding="utf-8-sig", index=False)
    # 轉成xlsx檔
    df.to_excel("./month_stock.xlsx", index=False)
    # 轉成html檔
    df.to_html("./month_stock.html", index=False)
