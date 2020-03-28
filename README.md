replace_line
========================
<B>replace_line</B> はテキストファイル内の特定行を、指定した文字列に置き換えるpythonパッケージです。

```
replace_line(input_file_name, output_file_name, replace_line, replace_str)  
input_file_name -- 入力ファイルのパス  
output_file_name -- 出力ファイルのパス  
replace_line -- 書き換えたい行  
replace_str -- 書き換える文字列
```

テキストファイル内の`orange`の行を`banana`に書き換えたい場合  
`replace_line("input.txt", "output.txt", "orange", "banana")`  

空行を削除したい場合  
`replace_line("input.txt", "output.txt", "", None)`


## 環境構築
1. `git clone https://github.com/kons16/replace_line.git`
1. `cd replace_line`
1. `python setup.py develop`
1. `input.txt`を用意した後で、以下を実行
```
>> from replace_line.replace_line import replace_line
>> replace_line("input.txt", "output.txt", "", None)
```
