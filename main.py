from bs4 import BeautifulSoup
import requests
import chromedriver_binary
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

def zaiko():
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome(chrome_options=options)
  driver.get("https://online.ymobile.jp/store/CHDO0001/regi/all/entry/iphone11")
  sleep(5)
  html = driver.page_source.encode('utf-8')
  soup = BeautifulSoup(html, "html.parser")
  latest_zaiko = str(soup.select(".htmlSelect-colorVariation-element-stock.stock-label.d-inlineblock.align-middle"))
  no_zaiko = '[<span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>, <span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>, <span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>, <span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>, <span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>, <span class="htmlSelect-colorVariation-element-stock stock-label d-inlineblock align-middle" data-v-03f71054="">在庫なし</span>]'
  if no_zaiko == latest_zaiko:
    print("在庫無し！ぴえん")
  else:
    print("在庫有り！すぐに買うのだ！")
    file = open("info.json", "r")
    info = json.load(file)
    CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
    line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text="在庫あり！")
    line_bot_api.push_message(USER_ID, messages=messages)
    