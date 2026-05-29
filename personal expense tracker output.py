Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
============================================== RESTART: C:/Users/ACER/Downloads/personal expense tracker.py =============================================
<class 'pandas.DataFrame'>
RangeIndex: 255 entries, 0 to 254
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Date          255 non-null    str    
 1   Category      209 non-null    str    
 2   Amount        241 non-null    float64
 3   Payment_Mode  255 non-null    str    
dtypes: float64(1), str(3)
memory usage: 8.1 KB
474066.0
<StringArray>
['Shopping', 'Food', 'Travel', 'Bills', 'Others']
Length: 5, dtype: str
               sum         mean     max
Category                               
Bills     110607.0  2633.500000  4960.0
Food      106229.0  2309.326087  4802.0
Others     68161.0  2350.379310  4849.0
Shopping   95359.0  2270.452381  4798.0
Travel     93710.0  2839.696970  4974.0
Month          1        2        3       4   ...       9        10       11       12
Category                                     ...                                    
Bills      8636.0  16944.0  11497.0     NaN  ...   8862.0    717.0  18059.0   7755.0
Food      18901.0   8273.0   4214.0   183.0  ...  23819.0      NaN   8120.0   4779.0
Others     4300.0   6001.0   2973.0  4849.0  ...  10093.0   4186.0   3412.0  10420.0
Shopping  10350.0  12972.0  15106.0  7065.0  ...  10765.0  10476.0   7500.0   1446.0
Travel     5649.0   8534.0   9380.0  6174.0  ...   7711.0   9334.0   3830.0   4184.0

[5 rows x 12 columns]
Category      Bills  Food  Others  Shopping  Travel
Payment_Mode                                       
Card             17    17      10        13       7
Cash             12    18       6        14      14
UPI              13    11      13        15      12
                 Date  Category  Amount Payment_Mode  Month Spending Level
0 2023-09-26 12:36:44  Shopping  1743.0          UPI      9         medium
2 2023-09-27 23:57:30      Food  4802.0         Card      9         medium
4 2023-09-02 00:03:08      Food   880.0         Cash      9            low
6 2023-01-26 20:41:29      Food  1419.0         Cash      1         medium
7 2023-11-06 10:37:10    Travel   790.0          UPI     11            low
