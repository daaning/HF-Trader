# installation

- make an binance accout a twitter-developer account get api keys for both
- make a file called config.json in this format

{
    "trade-market" : "BNBETH",
    "data-path" : "data/data.db",

    "binance-key" : "",
    "binance-secret" : "",
    
    "twitter_key" : "",
    "twitter_secret" : "",
    "twitter_tokenkey" : "",
    "twitter_tokensecret" : ""
}



    install ta-lib on your machine https://mrjbq7.github.io/ta-lib/install.html

    pip install -r requirements.txt --no-index --find-links file:///tmp/packages


    python main.py

## to visualize outside of terminal

    bokeh serve --show src/graph.py