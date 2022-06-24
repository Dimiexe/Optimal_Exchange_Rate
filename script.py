## Find best exchange route from EUR to CHF

import requests, pandas as pd, time
PATHS = []
RATES = []

def hit_API(from_cur, to_cur, api_key):
    url = "https://www.alphavantage.co/query"

    parameters = {
        "function":"CURRENCY_EXCHANGE_RATE",
        "from_currency":from_cur,
        "to_currency":to_cur,
        "apikey":api_key
    }

    r = requests.get(url,params=parameters).json()
    return r['Realtime Currency Exchange Rate']['5. Exchange Rate']

def get_paths(prev, next):
    for i in next:
        prev_in = []
        for j in prev:
            prev_in.append(j)
        prev_in.append(i)
        next_in=[]
        for j in next:
            next_in.append(j)
        next_in.remove(i)
        if i == "CHF":
            PATHS.append(prev_in)
        else:
            get_paths(prev_in, next_in)

def get_rates(PATHS, data):
    for path in PATHS:
        rate = 1
        for i, curency in enumerate(path):
            if i != 0:
                rate = rate * data.loc[path[i-1], curency]
        RATES.append(rate)

if __name__ == "__main__":
    api_key = "XXX-XXX-XXX"
    table = pd.DataFrame({"EUR":[1,1,1,1,1],"CHF":[1,1,1,1,1],"USD":[1,1,1,1,1],"GBP":[1,1,1,1,1],"JPY":[1,1,1,1,1]})
    table.index = ["EUR","CHF","USD","GBP","JPY"]
    counter = 0

    print("Comunicating with API...")
    for i,fc in enumerate(table.index.values):
        for j,tc in enumerate(table.index.values):
            if j>i:
                ## Sleep per 5 API calls to comply with API's fair use.
                if counter % 5 == 0:
                    time.sleep(60)
                counter +=1
                table.loc[fc,tc] = float(hit_API(fc, tc, api_key))
                table.loc[tc,fc] = 1/table.loc[fc,tc]
    print("Calculating Echange paths...")
    prev = ["EUR"]
    next = ["CHF","USD","GBP","JPY"]

    get_paths(prev, next)

    print("Finding optimal path...")
    get_rates(PATHS, table)

    max = 0
    max_index = 0
    for i, rate in enumerate(RATES):
        if max < rate:
            max = rate
            max_index = i
        elif max == rate:
            if len(PATHS[i]) < len(PATHS[max_index]):
                max = rate
                max_index = i

    ## Test amount of 200€, it is redundant but can show quickly how much you gain by following each path.
    amount = 200
    print("Base path:",PATHS[0],1/RATES[0])
    for i, p in enumerate(PATHS):
        ## Only show paths with 0.5% gain or more.
        if RATES[i] >= RATES[0]*100.5/100:
            print("Potential path",p,round((RATES[i]-RATES[0])*amount*100)/100," CHF Gain vs Direct Exchange for ", amount, ' €')
    print("Best path is", PATHS[max_index], "with total rate:", 1/max)