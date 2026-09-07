import gzip
import io 
import urllib.request


def main():
    # Bajar el archivo wet.paths.gz
    BASE = "https://data.commoncrawl.org/"
    req = urllib.request.Request("https://data.commoncrawl.org/crawl-data/CC-MAIN-2022-05/wet.paths.gz")
    with urllib.request.urlopen(req) as response:
        raw = response.read()
    # Descomprimir el archivo
    buf = io.BytesIO(raw)
    with gzip.open(buf, "rt", encoding="utf-8") as f:
        primera = f.readline().strip() #string
    # Bajar el segundo archivo
    with urllib.request.urlopen(BASE + primera) as response:
        with gzip.GzipFile(fileobj=response) as f:
            for line in f:
                print(line.decode("utf-8"), end="")


    
   


    


if __name__ == "__main__":
    main()
