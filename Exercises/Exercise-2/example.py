from urllib.parse import urljoin

base_url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
href = "filename.csv"

url_archivo = urljoin(base_url, href)
print(url_archivo)