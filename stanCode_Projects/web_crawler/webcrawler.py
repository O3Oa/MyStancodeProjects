"""
File: webcrawler.py
Name: Jessica
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)


        # ----- Write your code below this line ----- #

        tags = soup.find_all('tr')
        # num = tags[2].find_all('td')
        # num1 = num[2].text.split(',')
        # num2 = num1[0]+num1[1]
        # num3 = ''.join(num1)
        # num4 = num[2].text.strip(',')
        # # print(num2)
        # # print(num3)
        # # print(num[4].text)
        # print(num4)

        m_sum = 0
        f_sum = 0
        for i in range(2, 202):
            num = tags[i].find_all('td')
            m_num = num[2].text.split(',')
            m_num2 = int(''.join(m_num))
            f_num = num[4].text.split(',')
            f_num2 = int(''.join(f_num))
            m_sum += m_num2
            f_sum += f_num2
        print('Male Number: ' + str(m_sum))
        print('Female Number: ' + str(f_sum))


if __name__ == '__main__':
    main()
