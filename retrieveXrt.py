import pandas as pd
import requests
from datetime import datetime
import os
import re
url = "https://rate.bot.com.tw/xrt/flcsv/0/day"

xrt_response = requests.get("https://rate.bot.com.tw/xrt/flcsv/0/day",stream = True)
# # xrt = pd.read_html("https://rate.bot.com.tw/xrt/flcsv/0/day") #wrong usage based on source
xrt = xrt_response.content
# if len(csv_files) != 1:
#     raise ValueError('should be only one csv file in the current directory')
# final_url = requests.head(url, allow_redirects=True).url
# filename = final_url.split('/')[-1]
# print(filename)
d = xrt_response.headers['content-disposition']
fname = re.findall("filename=(.+)", d)
print(fname[0])
xrtfile = open(fname[0],'wb')
# csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
xrtfile.write(xrt)
xrtfile.close()


# # with open(df) as dfs:
# #     df = dfs.write(rrr.content)
#     # df = pd.read_csv(dfs)
#     # df = df.readlines()
# timestring = datetime.now()
# # print(timestring)

# xrt.to_csv(timestring.csv)
# print(df)

# def download_file(url):
#     local_filename = url.split('/')[-1]
#     # NOTE the stream=True parameter below
#     with requests.get(url, stream=True) as r:
#         r.raise_for_status()
#         print(r.raise_for_status())
#         with open(local_filename, 'wb') as f:
#             print(f)
#             for chunk in r.iter_content(chunk_size=8192): 
#                 # If you have chunk encoded response uncomment if
#                 # and set chunk_size parameter to None.
#                 #if chunk: 
#                 f.write(chunk)
#     # print(local_filename)
#     return local_filename

# print(download_file(url))
# print(is_downloadable(url))