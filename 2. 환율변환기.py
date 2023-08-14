import requests

def currency_converter(amount, from_cur="KRW", to_cur="USD"):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_cur}"

    response = requests.get(url)
    data = response.json()

    exchnage_rate = data['rates'][to_cur]
    result = round(amount * exchnage_rate, 2)

    return result


# 실행결과 : 1,000,000 변환:  752.0
print("1,000,000 변환: ", currency_converter(1000000))