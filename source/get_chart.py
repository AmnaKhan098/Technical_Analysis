# Generating charts
def chart_generation(ticker):
    url = "https://api.chart-img.com/v2/tradingview/advanced-chart"
    headers = {
        "x-api-key": "UTn03xsWQt1lPfymgJe1P3UAJFF7NgMO6ORUEyVZ",
        "content-type": "application/json"
    }

    data = {
        "theme": "dark",
        "interval": "1W",
        "symbol": f"NASDAQ:{ticker}",
        "override": {
            "showStudyLastValue": False
        },
        "studies": [
            {
                "name": "Volume",
                "forceOverlay": True
            },
            {
                "name": "MACD",
                "override": {
                    "Signal.linewidth": 2,
                    "Signal.color": "rgb(255,65,129)"
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Open an image file
    image = Image.open(BytesIO(response.content))

    # Display the image
    return image

