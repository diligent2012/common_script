#!/usr/bin/env python
# coding: utf-8

import get_platform_info


platform_api_dict = {
    'huobi':{
        'usdt':{
            'buy':'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=2&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
            'sell':'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=2&tradeType=0&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
        },
        'btc': {
            'buy': 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=1&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
            'sell': 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=1&tradeType=0&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
        },
        'eth': {
            'buy': 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=3&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
            'sell': 'https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=3&tradeType=0&currentPage=1&payWay=&country=&merchant=0&online=1&range=0',
        },
        'attr_list':[
            ['usdt', 'buy'],
            ['usdt', 'sell'],
            ['btc', 'buy'],
            ['btc', 'sell'],
            ['eth', 'buy'],
            ['eth', 'sell'],
        ],
        'market_coin_api': {
            'xrp/usdt': 'https://api.huobi.pro/market/history/kline?period=1min&size=10&symbol=xrpusdt',
            'eos/usdt': 'https://api.huobi.pro/market/history/kline?period=1min&size=10&symbol=eosusdt',
        },
        'market_coin_list': [
            'xrp/usdt',
            'eos/usdt',
        ],
        'huobi_cny_api':'https://api-otc.huobi.pro/v1/otc/base/market/price',
        'market_price_coin_list': [
            'BTC',
            'ETH',
            'USDT',
        ],
        'tool_obj': get_platform_info.huobi,
        'run_list': [
            get_platform_info.huobi.get_market_price,
        ]
    },
    'otcbtc':{
        'eos': {
            'buy':'https://otcbtc.com/sell_offers?currency=eos&fiat_currency=cny&payment_type=all',
            'sell':'https://otcbtc.com/buy_offers?currency=eos&fiat_currency=cny&payment_type=all',
        },
        'btc': {
            'buy':'https://otcbtc.com/sell_offers?currency=btc&fiat_currency=cny&payment_type=all',
            'sell':'https://otcbtc.com/buy_offers?currency=btc&fiat_currency=cny&payment_type=all',
        },
        'eth':{
            'buy': 'https://otcbtc.com/sell_offers?currency=eth&fiat_currency=cny&payment_type=all',
            'sell': 'https://otcbtc.com/buy_offers?currency=eth&fiat_currency=cny&payment_type=all'
        },
        'attr_list':[
            ['eos', 'buy'],
            ['eos', 'sell'],
            ['btc', 'buy'],
            ['btc', 'sell'],
            ['eth', 'buy'],
            ['eth', 'sell'],
        ],
        'tool_obj': get_platform_info.otcbtc,
    },
}

common_conf = {
    'retry_cnt': 5,
    'price_list_range': 4,
}


server_chan_api = {
    # 'pushbear': 'https://pushbear.ftqq.com/sub?sendkey={sendkey}&text={text}&desp={desp}'
    'pushbear': 'https://pushbear.ftqq.com/sub',
    'server_chan': 'https://sc.ftqq.com',
}

monitor_price = {
    'usdt_buy_price': 7.05,
    'otcbtc_eos_price': 65,
}
