# nestedTelnetClientlib/NestedTelnetClient

- auther: @tj8000rpm
- repository: https://github.com/tj8000rpm/nestedTelnetClientlib

## Install手順

```terminal
git clone https://github.com/tj8000rpm/nestedTelnetClientlib
cd nestedTelnetClientlib
pip install -e .
```

## 目的（独断と偏見による）
- 超レガシーな運用をしている人たちには*未だに*(そしてオリンピック以後の当分の間) ``telnet`` は重要なアイテムだ。
- しかも超レガシーな設備は往々にして保守用PCからの``ip reachability``がないノードが存在しうる
- しかしながら、超レガシーな環境にもかかわらず``自動化``と``AI化``が求められる！（なんてこった）
- そんな超レガシーな運用の現場における``scripting``による踏み台との戦い、``expect``や``teraterm macro``に疲れた人のために踏み台がいくつあっても怖くないPython telnetlibのラッパーライブラリが必要だ。

## 対象
- あまり難しいことはしない。
- とにかくtelnetの踏み台地獄と戦う人向け。
- 踏み台の先にあるサーバでコマンドを実行し、その結果をパースしながら順次コマンドを打つみたいな用途で使う想定
- なんか色々やりたい、冪等性ががが！となった人は``ansible``やその他WFを組めるような自動化ツールをお使いください。

## 使い方
- ``sample.py``を主に参照。
- ``NestedTelnetClient``インスタンスを生成する
- ``NestedTelnetClient``インスタンスのmethodである``connectWithTelnet``, ``writeACommandAndGetResultSTDOUT``だけを使えばOK。
- 最初の踏み台サーバのみ,python独自のtelnetlibを用いる
- それ以降の踏み台or最終目的サーバには``telnet``コマンドを順次打っていくだけです。

1. 踏み台サーバ/２つめ以降の踏み台/目的サーバにアクセスするときも、同じ``connectWithTelnet``を使用します。
2. 途中の踏み台を含め、コマンドを実行したい場合は``writeACommandAndGetResultSTDOUT``コマンドを用い、引数``telnetInstance``に上述の``telnetlib``インスタンスを指定してください。

- 当然ですが、踏み台の途中のサーバに、その踏み台以降のサーバにいる場合に途中でコマンドを投入することはできません。
- Nestedした場合、自分がいまどこのサーバにいるのかは常に気をつけてください・・・（対象確認！ヨシ！）
- その他の使い方は、``sample.py``を参照するか、チープな英語で書かれているソースコードの``docstirng``をご参照ください

## 制限事項
- rhel系/debian系/busyboxのtelnetサーバにしか今の所対応してないです。
 - 正確には確認してないです
- Unix系/switch系/交換機系等々の場合はカスタマイズが入りそうです
