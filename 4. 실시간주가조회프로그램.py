import pandas as pd
import requests
from bs4 import BeautifulSoup

CORP_LIST_URL="http://kind.krx.co.kr/corpgeneral/corpList.do?method=download"
STOCK_URL="https://finance.naver.com/item/main.nhn"

def fetch_corp_list_data(conditions):
    response = requests.get(CORP_LIST_URL)
    return pd.read_html(response.content, header=0)[0][conditions]

def fetch_realtime_price(code):
    url = f"{STOCK_URL}?code={code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    return price_element.text.strip() if price_element else ''


def get_company_info(company_list=[], conditions=['회사명', '종목코드']):
    if not company_list:
        return "조회할 회사 목록을 입력하세요."

    corp_list_df = fetch_corp_list_data(conditions)

    filtered_corp_list = corp_list_df[corp_list_df['회사명'].isin(company_list)].copy()
    
    # 종목코드 6자리로 맞추기
    filtered_corp_list['종목코드'] = filtered_corp_list['종목코드'].apply(lambda code: str(code).zfill(6))

    # 종목코드별 실시간주가 정보 가져오기
    filtered_corp_list['실시간주가'] = filtered_corp_list['종목코드'].apply(lambda code: fetch_realtime_price(code))

    return filtered_corp_list

# 회사 정보를 조회하고 결과를 출력
company_list = ['삼성전자', 'LG전자', 'SK하이닉스']
result_df = get_company_info(company_list)
print(result_df)

#########################################
#          회사명    종목코드    실시간주가
# 690     LG전자  066570  101,300
# 1343  SK하이닉스  000660  115,100
# 1999    삼성전자  005930   67,300 
#########################################