Type "help", "copyright", "credits" or "license" for more information.
>>> import yfinance as yf
>>> ticker = 'AAPL'
>>> data = yf.download(ticker, period='1y')
YF.download() has changed argument auto_adjust default to True
[*********************100%***********************]  1 of 1 completed
>>> print(data.head())
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date
2024-05-29  189.404221  191.355104  188.627853  188.727393  53068000
2024-05-30  190.399567  191.285423  189.742650  189.872035  49947900
2024-05-31  191.355103  191.673620  189.025999  190.548875  75158300
2024-06-03  193.126785  194.082323  191.623820  192.002041  50080500
2024-06-04  193.445312  194.410798  192.131450  193.733956  47471400
>>> import yahoo finance as yf
  File "<stdin>", line 1
    import yahoo finance as yf
                 ^^^^^^^
SyntaxError: invalid syntax
>>> import yfinance as yf
>>> from datetime import datetime
>>> ticker = 'AAPL'
>>> end date = datetime.now().strftime('%Y=%m-%d')
  File "<stdin>", line 1
    end date = datetime.now().strftime('%Y=%m-%d')
        ^^^^
SyntaxError: invalid syntax
>>> end date = datetime.now().strftime('%Y-%m-%d')
  File "<stdin>", line 1
    end date = datetime.now().strftime('%Y-%m-%d')
        ^^^^
SyntaxError: invalid syntax
>>> end_date = datetime.now().strftime('%Y-%m-%d')
>>> start_date = (datetime.now().replace(year=datetime.now().year - 1)).strftime('%Y-%m-%d')
>>> data = yf.download(ticker , start = start_date , end = end_date)
[*********************100%***********************]  1 of 1 completed
>>> print(data.head())
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date
2024-05-29  189.404205  191.355088  188.627837  188.727378  53068000
2024-05-30  190.399567  191.285423  189.742650  189.872035  49947900
2024-05-31  191.355103  191.673620  189.025999  190.548875  75158300
2024-06-03  193.126801  194.082338  191.623835  192.002056  50080500
2024-06-04  193.445312  194.410798  192.131450  193.733956  47471400
>>> from datetime import datetime
>>> print(datetime.now())
2025-05-29 20:43:08.405628
>>> data_recent = yf.download(ticker, period="5d")
[*********************100%***********************]  1 of 1 completed
>>> print(data_recent)
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date
2025-05-21  202.089996  207.039993  200.710007  205.169998  59211800
2025-05-22  201.360001  202.750000  199.699997  200.710007  46742400
2025-05-23  195.270004  197.699997  193.460007  193.669998  78432900
2025-05-27  200.210007  200.740005  197.429993  198.300003  56288500
2025-05-28  200.419998  202.729996  199.899994  200.589996  44158300
>>> form datetime import datetime
  File "<stdin>", line 1
    form datetime import datetime
         ^^^^^^^^
SyntaxError: invalid syntax
>>> from datetime import datetime
>>> ticker = 'AAPL'
>>> end_date = datetime.now().strftime(%Y-%m-%d)
  File "<stdin>", line 1
    end_date = datetime.now().strftime(%Y-%m-%d)
                                       ^
SyntaxError: invalid syntax
>>> end_date = datetime.now().strftime('%Y-%m-%d')
>>> satrt_date = (datetime.now().replace(year=datetime.now().year - 1)).strftime('%Y-%m-%d')
>>> data = yf.download(ticker, start = satrt_date, end = end_date)
[*********************100%***********************]  1 of 1 completed
>>> print(data.tail())
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date
2025-05-21  202.089996  207.039993  200.710007  205.169998  59211800
2025-05-22  201.360001  202.750000  199.699997  200.710007  46742400
2025-05-23  195.270004  197.699997  193.460007  193.669998  78432900
2025-05-27  200.210007  200.740005  197.429993  198.300003  56288500
2025-05-28  200.419998  202.729996  199.899994  200.589996  44158300
>>> data.shape[0]
250
>>> print(data)
Price            Close        High         Low        Open    Volume
Ticker            AAPL        AAPL        AAPL        AAPL      AAPL
Date
2024-05-29  189.404205  191.355088  188.627837  188.727378  53068000
2024-05-30  190.399567  191.285423  189.742650  189.872035  49947900
2024-05-31  191.355103  191.673620  189.025999  190.548875  75158300
2024-06-03  193.126801  194.082338  191.623835  192.002056  50080500
2024-06-04  193.445312  194.410798  192.131450  193.733956  47471400
...                ...         ...         ...         ...       ...
2025-05-21  202.089996  207.039993  200.710007  205.169998  59211800
2025-05-22  201.360001  202.750000  199.699997  200.710007  46742400
2025-05-23  195.270004  197.699997  193.460007  193.669998  78432900
2025-05-27  200.210007  200.740005  197.429993  198.300003  56288500
2025-05-28  200.419998  202.729996  199.899994  200.589996  44158300

[250 rows x 5 columns]
>>> from datetime import datetime
>>> import yfinance as yf
>>> import pandas as pd
>>> ticker = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
>>> end_date = datetime.now().strftime('%Y-%m-%d')
>>> start_date = (datetime.now().replace(year = datetime.now().year - 1)).strftime('%Y-%m-%d')
>>> data = yf.download(ticker, start = start_date, end = end_date)
[*********************100%***********************]  4 of 4 completed
>>> data = yf.download(ticker, start = start_date, end = end_date)['close']
[*********************100%***********************]  4 of 4 completed
Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'close'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\frame.py", line 4101, in __getitem__
    return self._getitem_multilevel(key)
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\frame.py", line 4159, in _getitem_multilevel
    loc = self.columns.get_loc(key)
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\indexes\multi.py", line 3040, in get_loc
    loc = self._get_level_indexer(key, level=0)
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\indexes\multi.py", line 3391, in _get_level_indexer
    idx = self._get_loc_single_level_index(level_index, key)
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\indexes\multi.py", line 2980, in _get_loc_single_level_index
    return level_index.get_loc(key)
  File "C:\Users\user\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'close'
>>> data = yf.download(ticker, start = start_date, end = end_date)
[*********************100%***********************]  4 of 4 completed
>>> print(data.head())
Price            Close              ...    Volume
Ticker            AAPL        AMZN  ...     GOOGL      MSFT
Date                                ...
2024-05-29  189.404205  182.020004  ...  23388700  15517100
2024-05-30  190.399567  179.320007  ...  22958700  28424800
2024-05-31  191.355103  176.440002  ...  37638900  47995300
2024-06-03  193.126801  178.339996  ...  27459100  17484700
2024-06-04  193.445312  179.339996  ...  26879600  14348900

[5 rows x 20 columns]
>>> print(data.tail())
Price            Close              ...    Volume
Ticker            AAPL        AMZN  ...     GOOGL      MSFT
Date                                ...
2025-05-21  202.089996  201.119995  ...  73416000  19216900
2025-05-22  201.360001  203.100006  ...  74864400  18025600
2025-05-23  195.270004  200.990005  ...  35211400  16883500
2025-05-27  200.210007  206.020004  ...  37995700  20974300
2025-05-28  200.419998  204.720001  ...  34492000  16992000

[5 rows x 20 columns]
>>> data = yf.download(ticker , start = start_date, end = end_date)['Close']
[*********************100%***********************]  4 of 4 completed
>>> print(data)
Ticker            AAPL        AMZN       GOOGL        MSFT
Date
2024-05-29  189.404205  182.020004  175.063034  425.904633
2024-05-30  190.399567  179.320007  171.291077  411.514923
2024-05-31  191.355103  176.440002  171.679199  411.971436
2024-06-03  193.126801  178.339996  172.346024  410.373657
2024-06-04  193.445312  179.339996  172.963058  412.904297
...                ...         ...         ...         ...
2025-05-21  202.089996  201.119995  168.559998  452.570007
2025-05-22  201.360001  203.100006  170.869995  454.859985
2025-05-23  195.270004  200.990005  168.470001  450.179993
2025-05-27  200.210007  206.020004  172.899994  460.690002
2025-05-28  200.419998  204.720001  172.360001  457.359985

[250 rows x 4 columns]
>>> data = yf.download(ticker , start = start_date, end = end_date, auto_adjust=True)
[*********************100%***********************]  4 of 4 completed
>>> print(data.head())
Price            Close              ...    Volume
Ticker            AAPL        AMZN  ...     GOOGL      MSFT
Date                                ...
2024-05-29  189.404205  182.020004  ...  23388700  15517100
2024-05-30  190.399567  179.320007  ...  22958700  28424800
2024-05-31  191.355103  176.440002  ...  37638900  47995300
2024-06-03  193.126801  178.339996  ...  27459100  17484700
2024-06-04  193.445312  179.339996  ...  26879600  14348900

[5 rows x 20 columns]
>>> price = data['Close']
>>> print(price.head())
Ticker            AAPL        AMZN       GOOGL        MSFT
Date
2024-05-29  189.404205  182.020004  175.063034  425.904633
2024-05-30  190.399567  179.320007  171.291077  411.514923
2024-05-31  191.355103  176.440002  171.679199  411.971436
2024-06-03  193.126801  178.339996  172.346024  410.373657
2024-06-04  193.445312  179.339996  172.963058  412.904297
>>> returns = price.pct_change().dropna()
>>> print(returns.head())
Ticker          AAPL      AMZN     GOOGL      MSFT
Date
2024-05-30  0.005255 -0.014834 -0.021546 -0.033786
2024-05-31  0.005019 -0.016061  0.002266  0.001109
2024-06-03  0.009259  0.010768  0.003884 -0.003878
2024-06-04  0.001649  0.005607  0.003580  0.006167
2024-06-05  0.007821  0.010817  0.009322  0.019083
>>> import numpy as np
>>> trading_days = 250
>>> mu = returns.mean()
>>> cov = returns.cov()
>>> print("Expected annual returns (mu):")
Expected annual returns (mu):
>>> print(mu.round(3))
Ticker
AAPL     0.000
AMZN     0.001
GOOGL    0.000
MSFT     0.000
dtype: float64
>>> print("\nAnnualised covarience matrix:")

Annualised covarience matrix:
>>> print(cov.round(4))
Ticker    AAPL    AMZN   GOOGL    MSFT
Ticker
AAPL    0.0004  0.0003  0.0002  0.0002
AMZN    0.0003  0.0005  0.0003  0.0003
GOOGL   0.0002  0.0003  0.0004  0.0002
MSFT    0.0002  0.0003  0.0002  0.0003
>>> import matplotlib.pyplot as plt
>>> price.plot(figsize =(10,6))
<Axes: xlabel='Date'>
>>> plt.title("stock prices over time")
Text(0.5, 1.0, 'stock prices over time')
>>> plt.xlabel("Date")
Text(0.5, 0, 'Date')
>>> plt.ylabel("price($)")
Text(0, 0.5, 'price($)')
>>> plt.legend (title = "ticker")
<matplotlib.legend.Legend object at 0x000001FAA667BC40>
>>> plt.grid(True)
>>> plt.show()
>>> plt.show()
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>> price.plot(figsize=(10,6))
<Axes: xlabel='Date'>
>>> plt.title("stock prices over time")
Text(0.5, 1.0, 'stock prices over time')
>>> plt.xlabel("date")
Text(0.5, 0, 'date')
>>> plt.ylabel("price in dollars")
Text(0, 0.5, 'price in dollars')
>>> plt.legend(title = "ticker")
<matplotlib.legend.Legend object at 0x000001FAAB95F550>
>>> plt.grid(True)
>>> plt.show()
>>>
>>>
>>> returns.hist(bins = 50, figsize = (10 , 6))
array([[<Axes: title={'center': 'AAPL'}>,
        <Axes: title={'center': 'AMZN'}>],
       [<Axes: title={'center': 'GOOGL'}>,
        <Axes: title={'center': 'MSFT'}>]], dtype=object)
>>> plt.suptitle("Histogram of daily returns")
Text(0.5, 0.98, 'Histogram of daily returns')
>>> plt.show()