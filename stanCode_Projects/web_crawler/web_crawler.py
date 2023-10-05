import requests 
from bs4 import BeautifulSoup


def main():
	url = 'https://www.imdb.com/chart/top'
	response = requests.get(url)
	print(response)
	html = response.text
	soup = BeautifulSoup(html)
	tags = soup.find_all('td', {'class', 'titleColumn'})
	d = {}
	for tag in tags:
		year = tag.span.text
		if year in d:
			d[year] += 1
		else:
			d[year] = 1
	for key, value in sorted(d.items(), key=lambda ele: ele[1]):
		print(key, '->', value)


if __name__ == '__main__':
	main()
