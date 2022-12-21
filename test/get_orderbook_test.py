import datetime
import pandas as pd

import algohouse as ah
import ah_settings as ahs

USER_EMAIL = 'tarasryb@gmail.com'
SIGNKEY = '9566c74d10037c4d7bbb0407d1e2c649'


# USER_EMAIL = 'vyklyuk@ukr.net'
# SIGNKEY = '81855ad8681d0d86d1e91e00167939cb'


def _test_get_orderbook():
    ahs.DOMAIN = 'http://127.0.0.1:5000'
    res, res_c = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='tiny',  # 'binance/f',  # 'lbank',  # 'binance',  # 'binance/f',
                                  instrument='1000LUNCBUSD',
                                  # 'APEBUSD',  # 'BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T10:00:00'
                                  )
    print(res.shape)
    assert not res is None


def _test_get_orderbook_reset():
    res, res_c = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='lbank',  # 'binance',  # 'binance/f',
                                  instrument='BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T10:00:00'
                                  )
    print(res.shape)
    assert not res is None


def _test_get_cached_orderbook():
    ahs.DOMAIN = 'http://127.0.0.1:5000'
    res, res_c = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='small',  # 'binance/f',  # 'lbank',  # 'binance',  # 'binance/f',
                                  instrument='1000LUNCBUSD',
                                  # 'APEBUSD',  # 'BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T10:00:00',
                                  levels=None
                                  )
    print(len(res['bid']))
    print(len(res['ask']))

    ahs.ORDER_LINES_TO_READ = 1000
    res, res_c = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='binance/f',
                                  # 'big,small, tiny'  # 'binance/f',  # 'lbank',  # 'binance',  # 'binance/f',
                                  instrument='1000LUNCBUSD',
                                  # 'APEBUSD',  # 'BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T10:00:00',
                                  levels=10
                                  )
    print(len(res['bid']))
    print(len(res['ask']))
    assert not res is None


def _test_get_orderbook_snapshot():
    ahs.DOMAIN = 'http://127.0.0.1:5000'
    res = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='file',
                                  instrument='set_1.txt',  # 'APEBUSD',  # 'BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T10:00:00',
                                  levels=10, snapshot=True
                                  )
    print(len(res['snapshot']))
    assert not res is None


def test_get_orderbook_1():
    # ahs.DOMAIN = 'http://127.0.0.1:5000'
    ahs.ORDER_LINES_TO_READ = 200
    # second reset 2022-11-12T10:04:21.476
    res, res_c = ah.get_orderbook(USER_EMAIL, SIGNKEY,
                                  exchange='binance/f',  #'binance/f',  #'file',
                                  instrument='LITUSDT',  #'ETHUSDT',  # 'orderbooks_ins-BTCUSDT_ex-binance-f_from-2022-11-12T10-00-00.txt',  #'BTCUSDT', # 'APEBUSD',  # 'BTS_USDT',  # 'BTCB_USD',  # '1000LUNCBUSD',
                                  from_time='2022-11-12T09:00:00',  # '2022-12-12T00:00:00',
                                  levels=0
                                  )
    print(len(res['bid']))
    print(len(res['ask']))

    print('bid\n', res_c['bid'])
    print('ask\n', res_c['ask'])

    res_c['bid'].to_csv('data/bid.csv')
    res_c['ask'].to_csv('data/ask.csv')

    assert not res is None
