import pandas as pd

# replace()
d = pd.read_csv('./samples/airtravel.csv')
print(d)

print(d.replace(to_replace=340, value='Yep'))
print(d.replace(340, 10000))
print(d.replace([340, 318, 362,363], [300, 310, 360, 200]))
print(d.replace([340, 318, 362,363], 300))
print(d.replace({"1959":360, "1958":340}, 0))
print(d.replace('[A-Za-z]', 0, regex=True))
print(d.replace({"Month":'[A-Za-z]'}, 0, regex=True))
print(d.replace(to_replace=340 , method='bfill'))
print(d.replace(to_replace=340 , method='bfill', limit=1))
d.replace(340 , 0, inplace=True)
print(d)