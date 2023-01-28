from fastapi import FastAPI

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd



app = FastAPI()

@app.get("/")
async def root():

    URL = 'https://comic.naver.com/webtoon/weekday.nhn'

    html = requests.get(URL).text # html 문서 전체를 긁어서 출력해줌, .text는 태그 제외하고 text만 출력되게 함
    soup = BeautifulSoup(html, 'html.parser')
    return {"message": "Hello World"}