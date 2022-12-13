# Markdown 語法摘要
#### https://markdown.tw/
#### Markdown是一種輕量級標記式語言，創始人為約翰·格魯伯。它允許人們使用易讀易寫的純文字格式編寫文件，然後轉換成有效的XHTML文件。
#### Markdown的目標是實現「易讀易寫」。


## 標題

### Setext形式是用底線的形式，任何數量的=和-都可以有效果。

This is an H1 標題一
=============

This is an H2 標題二
-------------

### Atx形式則是在行首插入1到6個 # ，各對應到標題1到6階，例如：
# This is an H1 #

## This is an H2 ##

### This is an H3 ######

## 區塊引言

* Markdown使用email形式的區塊引言
 
> 這是區塊引言
> 這是第二行
> 第三行
> > 區塊引言可以有階層（例如：引言內的引言），只要根據層數加上不同數量的>

## 清單

> Markdown支援有序清單和無序清單。

> 無序清單使用星號、加號或是減號作為清單標記：

*   Red
+   Green
-   Blue

>有序清單則使用數字接著一個英文句點：(在清單標記上使用的數字並不會影響輸出的HTML結果)
3. 第一
2. 第二
5. 第三

>要讓清單看起來更漂亮，你可以把內容用固定的縮排整理好：
*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.

>清單項目可以包含多個段落，每個項目下的段落都必須縮排4個空白或是一個tab：
1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.
