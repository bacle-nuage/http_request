# coding: UTF-8

import requests
import json
from services import file

DEFAULT_OUTPUT = './default.txt'

# PC SP 出しわけの為のUA
SP_HEADER = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36'}
PC_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

# HTTPリクエスト
# return json
def request(url:str, headers):
    res = requests.get(url, headers=headers)
    return json.dumps(res.json())

# request headers user-agent
def get_headers(ua):
    if ua == 'pc':
        headers = PC_HEADER
    else:
        headers = SP_HEADER
    return headers

# チャンネルIDで情報取得
def get_status(args):
    output = args.output
    if output is None:
        output = DEFAULT_OUTPUT
    print('出力ファイル : ' + output)
    csv_file = file.read(args.path)
    for row in csv_file:
        headers = get_headers(row[1])
        res = request(row[0], headers)
        data['url'] = row[0]
        data['ua']  = row[1]
        data['status']  = str(res.status_code)
        output_data = '\n'.join(','.join(data))
        file.add(output_data, output)
    return '正常に終了しました'
