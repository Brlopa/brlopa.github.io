url = "https://planning.simfest.co.uk/flightboard?email=simfest"

html = urlopen(url).read()

soup = BeautifulSoup(html)


for script in soup(["script", "style"]):

    script.decompose()

strips = list(soup.stripped_strings)

print(strips[:5])