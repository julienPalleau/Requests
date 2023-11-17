# https://www.youtube.com/watch?v=yqom9E32KIc
# https://www.youtube.com/watch?v=pGxe6OJlRx8
import requests
import pandas as pd

# our API address
url = 'https://random-data-api.com/api/v2/users?size=1'

# runs a get request and assigns it to a variable named response
response = requests.get(url)

# request then handles our json data
api_result = response.json()

# api_result
df1 = pd.json_normalize(api_result)
print(df1)

df2 = df1.melt()
df2.to_csv('json result.csv', index=False)
print("done")