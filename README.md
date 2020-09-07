# PDF-Handler
PDFファイルをあれこれするプログラム群

## How to use
### PDFファイルの統合
merge.pyを実行して、統合したいファイル・フォルダを指定します。`m`と入力すると指定が終了します。  
次に出力先を入力するとそこに統合されたPDFファイルが出力されます。(拡張子は自動的に.pdfとなります)
```
> python merge.py
Merge file or Folder 1 (Type 'm' to merge.) -> sample/
 Add sample/sample1.pdf
 Add sample/sample2.pdf
 Add sample/sample3.pdf
 Add sample/sample4.pdf
Merge file or Folder 5 (Type 'm' to merge.) -> m
Generated file -> merged.pdf
File merge completed!!
> ./merged.pdf
```
