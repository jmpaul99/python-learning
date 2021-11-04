import urllib.request,json

def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    data = urllib.request.urlopen(url).read()
    jsonData = json.loads(data.decode("utf-8"))
    print(jsonData["time"]["updated"])

if __name__ == '__main__':main()