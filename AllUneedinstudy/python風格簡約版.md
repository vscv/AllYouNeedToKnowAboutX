## 簡單版風格
#### one example is all we need

```python
# Aligned with opening delimiter
def run_this_code_free(inps):
    """Python style note.
    
    即使是一個打算被用作腳本的文件, 也應該是可導入的. 並且簡單的導入不應該導致這個腳本的主功能(main functionality)被執行, 這是一種副作用. 主功能應該放在一個main()函數中.
    def main():
      ...

    if __name__ == '__main__':
        main()
    """
    
    print(f'QQcheck:')
    long_str_auto_link = ('This will build a very long long '
                         'long long long long long long string')
    hit_1 = '用4個空格來縮進代碼,絕對不要用tab, 也不要tab和空格混用.'
    hit_2 = '頂級定義之間空兩行, 比如函數或者類定義. 方法定義之間空一行.'
    hit_3 = '括號內不要有空格. Yes: spam(ham[1], {eggs: 2}, [])
    hit_4 = ('即使是一個打算被用作腳本的文件, 也應該是可導入的.'
             '並且簡單的導入不應該導致這個腳本的主功能(main functionality)被執行,'
             '這是一種副作用. 主功能應該放在一個main()函數中.')
    return inps
    
```
