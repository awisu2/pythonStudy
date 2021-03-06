functoolsを利用した、decoratorのサンプル
====================================

decoratorを利用すると @ を頭につけた記述をすることで、関数の実行前にdecorator関数を実行できる

```py
@decorator
def foo():
  pass
```

引数を持たせるには
---------------

デコレータとして指定できるのは対象関数のインスタンスを引数で受け取り、*wrapsを返却する関数のポインタ*(デコレータ関数)  
そのため、デコレータに引数をもたせる場合、以下のようにする

1. 普通に引数を受け取る関数を作成
2. 1.の関数はデコレータ関数を返却する

デコレートした関数を実行せずに終了する方法
-----------------------------------

1. 引数として受け取っている関数ポインタを実行せずreturnする
  - サンプル参照: is_stop=true
  - 特定のシステム上で、何らかのルールに則ったレスポンスが必要な場合はその補完が必要

主に、チェック、認証、デコレータ内でのエラー発生時に利用

