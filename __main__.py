#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import argparse
import sys

from services import request

def get_args():
    # コマンド１
    parser = argparse.ArgumentParser(description='YouTube Api')
    parser.add_argument('-o', '--output', dest='output', type=str, help='保存ファイル', required=True)

    # コマンド２
    subparsers = parser.add_subparsers()
    get_channel_parser = subparsers.add_parser('get_status', help='Response HttpStatus')
    get_channel_parser.add_argument('path', help='csv file path') # チャンネルID
    get_channel_parser.set_defaults(func=request.get_status) # 実行する関数設定

    return  parser.parse_args()


def main():
    # コマンドライン引数の取得
    args = get_args()

    #アプリケーション内部の実装
    try:
        res = args.func(args)

        #終了ステータスの定義
        print(res)

        #エラーの出力
    except :
        print('#' * 5 + 'エラーが発生して処理を中断しました' + '#' * 5)

if __name__ == '__main__':
    main()