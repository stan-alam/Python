import nasdaqdatalink 

nasdaqdatalink.ApiConfig.api.api_key= ""
nasdaqdatalink.ApiConfig.api.base_url = "https://api.nasdaq.com/api"
data = nasdaqdatalink.get("quote/AAPL/info?assetclass=stocks")