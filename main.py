from bs4 import BeautifulSoup
import requests
import time
import asyncio
from telegram import Bot

# Here you need to set True on each index you want to track:
indexes = {'Dow Jones': False, 'S&P 500': False, 'Nasdaq': False, 'Small Cap 2000': False,
           'S&P 500 VIX': False, 'S&P/TSX': False, 'Bovespa': False, 'S&P/BMV IPC': False,
           'MSCI World': False, 'DAX': False, 'FTSE 100': False, 'CAC 40': False,
           'Euro Stoxx 50': False, 'AEX': False, 'IBEX 35': False, 'FTSE MIB': False,
           'SMI': False, 'PSI': False, 'BEL 20': False, 'ATX': False, 'OMXS30': False,
           'OMXC25': False, 'MOEX': False, 'RTSI': False, 'WIG20': False, 'Budapest SE': False,
           'BIST 100': False, 'TA 35': False, 'Tadawul All Share': False, 'Nikkei 225': False,
           'S&P/ASX 200': False, 'DJ New Zealand': False, 'Shanghai': False, 'SZSE Component': False,
           'China A50': False, 'DJ Shanghai': False, 'Hang Seng': False, 'Taiwan Weighted': False,
           'SET': False, 'KOSPI': False, 'IDX Composite': False, 'Nifty 50': False, 'BSE Sensex': False,
           'PSEi Composite': False, 'Karachi 100': False, 'VN 30': False, 'CSE All-Share': False
           }
token_for_chatbot = 'Enter Your Telegram Bot Token Here'
id_for_chatbot = 'Enter Chat ID for your Bot'
refresh_time = 10  # Please enter time in seconds how often you want to refresh the info


bot = Bot(token=token_for_chatbot)
index_list = []
index_last = []
headers_browser = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

link = 'https://www.investing.com/indices/major-indices'
tracking = True


async def send_telegram_message(chat_id, message):
    await bot.send_message(chat_id=chat_id, text=message)


def parse(data, true_indexes):
    for item in data:
        index_name = (item.find(class_='dynamic-table-v2_col-name__Xhsxv')
                      .find('span', class_='block')
                      .find_next_sibling()
                      .get_text(strip=True))
        if index_name in true_indexes:
            index_lasts = item.find(class_='dynamic-table-v2_col-other__zNU4A').get_text(strip=True)
            index_high = item.find_all(class_='dynamic-table-v2_col-other__zNU4A')[1].get_text(strip=True)
            index_low = item.find_all(class_='dynamic-table-v2_col-other__zNU4A')[2].get_text(strip=True)
            index_chg = item.find(class_='datatable-v2_cell--bold__cXQUV').get_text(strip=True)
            index_perc = item.find_all(class_='datatable-v2_cell--bold__cXQUV')[1].get_text(strip=True)
            index_item = {
                'Index': index_name,
                'Last': index_lasts,
                'High': index_high,
                'Low': index_low,
                'Chg.': index_chg,
                'Chg. %': index_perc
            }
            index_list.append(index_item)
            del true_indexes[index_name]


async def main():
    while tracking:
        response = requests.get(link, headers=headers_browser).text
        soup = BeautifulSoup(response, 'lxml')
        searching = soup.find_all(class_='datatable-v2_row__hkEus dynamic-table-v2_row__ILVMx')
        all_indexes = {key: value for key, value in indexes.items() if value}
        parse(searching, all_indexes)

        for i in range(min(len(index_last), len(index_list))):
            dict1 = index_last[i]
            dict2 = index_list[i]
            print(dict2)
            await send_telegram_message(id_for_chatbot, dict2)
            for key, value in dict1.items():
                if key in dict2 and dict2[key] != value:
                    mess = (f'The {dict1["Index"]} index has changed.\n'
                            f'The last index is {dict1["Last"]}\n'
                            f'The new one is {dict2["Last"]}\n')
                    await send_telegram_message(id_for_chatbot, mess)
                    break

        index_last[:] = index_list
        if refresh_time <= 5:
            time.sleep(5)
        else:
            time.sleep(refresh_time)
        index_list.clear()


if __name__ == "__main__":
    asyncio.run(main())
