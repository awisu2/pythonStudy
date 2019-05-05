[16\.4\. argparse — コマンドラインオプション、引数、サブコマンドのパーサー — Python 3\.6\.5 ドキュメント](https://docs.python.jp/3/library/argparse.html#action)

```bash
python3 . 1 2 3
python3 . 1 2 3 --sum
python3 . 1 2 3 --ping
python3 . 1 2 3 --ping --pinger foobar
python3 . 1 2 3 --ping --pinger foobar --sum
```

基本
---

argparse.ArgumentParser インスタンス に add_argument をすることにより引数を解析及び取得できる
設定によっては、requireとなりparse時にエラーを返却するようになる

また *-h* を指定することによってヘルプが表示される

仕様
---

### ArgumentParser

[argparse \-\-\- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3\.7\.3 ドキュメント](https://docs.python.org/ja/3/library/argparse.html#argumentparser-objects)

`class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True)`

- prog - プログラム名 (デフォルト: sys.argv[0])
- usage - プログラムの利用方法を記述する文字列 (デフォルト: パーサーに追加された引数から生成されます)
- description - 引数のヘルプの前に表示されるテキスト (デフォルト: none)
- epilog - 引数のヘルプの後で表示されるテキスト (デフォルト: none)
- parents - ArgumentParser オブジェクトのリストで、このオブジェクトの引数が追加されます
- formatter_class - ヘルプ出力をカスタマイズするためのクラス
- prefix_chars - オプションの引数の prefix になる文字集合 (デフォルト: '-')
- fromfile_prefix_chars - 追加の引数を読み込むファイルの prefix になる文字集合 (デフォルト: None)
- argument_default - 引数のグローバルなデフォルト値 (デフォルト: None)
- conflict_handler - 衝突するオプションを解決する方法 (通常は不要)
- add_help - -h/--help オプションをパーサーに追加する (デフォルト: True)
- allow_abbrev - 長いオプションが先頭の 1 文字に短縮可能 (先頭の文字が一意) である場合に短縮指定を許可する。(デフォルト: True)

### ArgumentParser.add_argument

[argparse \-\-\- コマンドラインオプション、引数、サブコマンドのパーサー — Python 3\.7\.3 ドキュメント](https://docs.python.org/ja/3/library/argparse.html#the-add-argument-method)

`ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])`

- name または flags - 名前か、あるいはオプション文字列のリスト (例: foo や -f, --foo)。
    - '-'付きのものを*flags*といい `python . --foo="bar"` のように引数を取る。基本 option
    - '-'がつかないものを*name*といい `python . 123` のように場所で引数を取る。基本 required
    - 複数割り当てることも可能 (ex: `parser.add_argument('--foo', '-f')`)
    - destを指定しない場合、この値から引数キーが生成される, --の数が多い順、先頭に近い順で決定されるっぽい。不安ならdestを指定のこと
- action - コマンドラインにこの引数があったときのアクション。拡張することも可能
    - store (default): 単に与えられた値を取得する
    - store_const: 引数がない場合にconstの値を取得する
    - store_true, store_false: 引数がある場合に指定した boolean値 が取得される、ない場合は反転する
    - append: 与えられた値を配列に追加する形で取得 (ex: `python . --foo 1 --foo 2` => "['1','2']")
    - append_const: 引数が与えられた回数分のconstの値を配列に追加して取得 (ex: `python . --foo --foo` => "['bar','bar']")
    - count: キーワドの回数を取得 (ex: `python -vvv` => 3)
    - help: help表示時の文言
- nargs - 受け取るべきコマンドライン引数の数。(指定しない場合は1)
    - N: 一定数の引数を受け取る、指定するのはNではなく数値(ex: `python --foo 1 2 3`)
    - ?: 0 or 1 引数がないときは defaultが割り当てられる。それもない場合はconstの値
    - *: 何個でもOK
    - +: 1個以上
- const - 一部の action と nargs の組み合わせで利用される定数。
- default - コマンドラインに引数がなかった場合に生成される値。
- type - コマンドライン引数が変換されるべき型。
    - int, float: intまはたfloat型をチェック
    - open: 文字列を受け取りファイルオープンが可能
- choices - 引数として許される値のコンテナー。 (ex: `choices=range([5, 10])`)
- required - コマンドラインオプションが省略可能かどうか (オプション引数のみ)。
- help - 引数が何なのかを示す簡潔な説明。
- metavar - 使用法メッセージの中で使われる引数の名前。
- dest - parse時のキー名をname, flagsとは別にする

samples
-------

### minimam

何も引数を取らない。(引数があるとエラーになる)

```py
parser = argparse.ArgumentParser()
parser.parse_args()
```

### simple use

```py
def argpase():
    parser = argparse.ArgumentParser(prog='argparse sample', description='this is argparse sample')




    return parser.parse_args()
```
