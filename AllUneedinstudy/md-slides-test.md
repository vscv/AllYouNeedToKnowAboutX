範本來自 https://hackmd.io/@tedchen107/H1bm7Hbpd#/ https://hackmd.io/@tedchen107/ByFgWPWVY#/

簡報語法只能在hackmd.io上使用＠＠

# 8_Object-Oriented Programming

---

### 物件導向 Object-oriented

##### 物件導向程式設計(Object-oriented programming, OOP)

* 類別 ( Class )
* 物件 ( Object )
* 屬性 ( Attribute )
* 方法 ( Method )
* 建構子 ( Constructor )

---

## 類別 Class

#### &lt;font color=&#39;red&#39;&gt;Classes&lt;/font&gt; provide a means of bundling data and functionality together. Creating a new class creates a new type of &lt;font color=&#39;red&#39;&gt;object&lt;/font&gt;, allowing new &lt;font color=&#39;red&#39;&gt;instances&lt;/font&gt; of that type to be made

#### Class 提供了一種結合資料與功能的手段。建立一個 class 將會新增一個&lt;font color=&#39;red&#39;&gt;物件&lt;/font&gt;的型別，並且允許建立該型別的新&lt;font color=&#39;red&#39;&gt;實例&lt;/font&gt;。


---

### 類別說明
:::info
一個抽象的概念 -- 車子，人類，大象，蛋糕 ...

* 車子 是 ... 有 ... 可以(會） ...
* 人類 是 ... 有 ... 可以(會） ...
* 大象 是 ... 有 ... 可以(會） ...
* 蛋糕 是 ... 有 ... 可以(會） ...

:::

---

### 類別 Class 
:::info
車子 
* 是本身具有動力得以驅動前進，具有兩輪或以上以原動機驅動
* 有廠牌，價格，動力來源，車牌號碼 ...
* 可以定速巡航，車道維持輔助 ...
::: 

:::success
**類別**
**有**靜態資料 --  &lt;font color=&#39;blue&#39;&gt;**屬性 (Attribute) 也就是變數**&lt;/font&gt;
**可以**操作動作 -- &lt;font color=&#39;blue&#39;&gt;**方法(Method) 也就是函式**&lt;/font&gt;
:::

---

#### 定義類別 Class definition
```python=
class ClassName:
    ...
    ...
```

#### 建立物件 Object instantiation


```python=
object = ClassName()
```

---

#### 車子類別

```python=
# Define a car Class
class Car:
    pass # nothing to do

car1 = Car() # Car instance / car object
car2 = Car() # Car instance / car object
```
![](https://i.imgur.com/qIRTvHe.png)

---

#### 實例變數 (instance variable)
###### 每一個實例有自已的屬性資料
```python=
# Define a car Class
class Car:
    pass # nothing to do
car1 = Car() # Car instance / car object
car1.brand = &#34;Toyota&#34;
car2 = Car() # Car instance / car object
car2.weight = 450
```
![](https://i.imgur.com/0IXAQyD.png)


---

### \_\_init\_\_() 特別方法 
###### 建立&lt;font color=#FF6600&gt;預設&lt;/font&gt;實例變數

:::info
__init__(self [,... ]): constructor
self is the instance itself
:::
```python=
#initial the instace variable withr default value
def __init__(self):
    self.attribute = &#34;default value&#34;

#initial the instace variable with user defined value
def __init__(self, attr1):
    self.attribute = attr
```

---

#### 定義車子類別 + 預設實例變數

```python=
# Define a car Class
class Car:
    # Constructor
    def __init__(self):
        # initial instance variable
        self.brand = &#34;Toyota&#34;
```
![](https://i.imgur.com/6Lk7aDe.png)

---

#### 建立物件 車子類別 + 預設實例變數
```python=預設實例變數
class Car:
    # Constructor
    def __init__(self):
        # initial instance variable
        self.brand = &#34;Toyota&#34;

car1 = Car()
```
![](https://i.imgur.com/IGVNMeO.png)

---

#### 建立物件 車子類別 + &lt;font color=#FF6600&gt;自訂&lt;/font&gt;預設實例變數

```python=
class Car:
    
    def __init__(self, brand):
        self.brand = brand

car1 = Car(&#34;Toyota&#34;)
car2 = Car(&#34;Tesla&#34;)
```
![](https://i.imgur.com/PkU8JcJ.png)

---

#### 物件使用屬性 ( Access attribute)
:::info
object.attribute_name 
:::

```python=
class Car:
    def __init__(self, brand):
        self.brand = brand
        
car1 = Car(&#34;Tesla&#34;)
# print car brand
print(f&#34;car1.brand is {car1.brand}&#34;)
```
```shell
car1.brand is Tesla
```
![](https://i.imgur.com/kXHnBzj.png)


---

#### 自訂預設實例變數的&lt;font color=#FF6600&gt;預設值&lt;/font&gt;

```python=
class Car:
    # sepacial method with default Toyota brand   
    def __init__(self, brand = &#34;Toyota&#34;):
        # initial instance variable brand
        self.brand = brand
```

![](https://i.imgur.com/pFtMAnu.png)


---

#### 自訂預設實例變數&lt;font color=#FF6600&gt;使用&lt;/font&gt;預設值產生物件

```python=
class Car:  
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand

car1 = Car() # No brand --&gt; brand is Toyota
print(f&#34;car1.brandis {car1.brand}&#34;)
```
```shell
car1.brand is Toyota
```
![](https://i.imgur.com/jjM81qB.png)

---


#### 自訂預設實例變數&lt;font color=#FF6600&gt;不使用&lt;/font&gt;預設值產生物件

```python=
class Car:  
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand

car1 = Car(&#34;Tesla&#34;) # brand is Tesla
print(f&#34;car1.brand is {car1.brand}&#34;)
```
```shell
car1.brand is Tesla
```
![](https://i.imgur.com/HKxTYZl.png)

---

#### 實例方法 (instance method)

:::info
類別中沒有加任何裝飾詞(Decorator)的方法(Method)-也就是類別中的函式
:::

```python=
Class ClassName:
    def method(self[,...]):
        ...
        ...
```

---

#### 車子類別 + 實例方法
```python=
class Car:  
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand

    # 實例方法 instance method    
    def info(self):
        return f&#34;This car is {self.brand} brand)&#34;
```
![](https://i.imgur.com/hgbQ1nP.png)

---

#### 物件使用實例方法 ( Access instance method)
:::info
object.method_name
:::
```python=
class Car:  
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand 
    def info(self):
        return f&#34;This car is {self.brand} brand&#34;
car1 = Car(&#34;Tesla&#34;)
print(car1.info())
```
```shell
This car is Tesla brand)
```

---

##### class diagram
![](https://i.imgur.com/PKGa7dt.png)

---

### 類別變數 Class Variable

###### 類別中直接定義的變數，所有實例共享的變數

```python=
Class ClassName:
    attribute = xxx
    ...
    ...
```

---

#### 車子類別 + 類別變數

```python=
class Car:
    chinese_name = &#34;汽車&#34; # 類別變數 class variable
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand 
    def info(self):
        return f&#34;This {self.brand} is {self.chinese_name}&#34;
car1 = Car(&#34;Tesla&#34;)
print(car1.info())
car2 = Car(&#34;Toyota&#34;)
print(car2.info())
```
```shell
This Tesla is 汽車
This Toyota is 汽車
```
:::danger
兩台車 chinese_name 都一樣 ！！！
:::

---

##### class diagram
![](https://hackmd.io/_uploads/rkCCac253.png)

---

#### __str__(self) special method

###### 類別的預設方法之一，物件的字串表達形式
```
print(object) --&gt; python call object.__str__(self)
````

```python=
class Car:
    status = &#34;Good&#34; # class attribute
    def __init__(self, brand = &#34;Toyota&#34;):
        self.brand = brand
    def __str__(self):
        return f&#34;Car class status {self.status} from __str__&#34;
    def info(self):
        return f&#34;This {self.brand} is {self.status}&#34;
car1 = Car(&#34;Tesla&#34;)
print(car1)
```
```shell
Car class status Good from __str__
```

---

##### class diagram
![](https://i.imgur.com/DEOuszy.png)


---

### 類別方法 (class method)
:::info
類別中有 @classmethod 裝飾詞 (Decorator) 的方法，類別呼叫類別方法時，類別方法會傳入 cls 參數，指向類別
:::

```python=
class ClassName:
    # 類別方法(Class Method)
    @classmethod
    def class_metho(cls):
        ...
        ...
```

---

#### 車子類別 + 類別方法

```python=
class Car:
    status = &#34;Good&#34; # class attribute
    # 類別方法(Class Method)
    @classmethod
    def chk_status(cls):
        print(&#34;Car chk_staus is {cls.status}.&#34;)
Car.chk_status()
```
```shell
Car chk_staus is Good.
```

![](https://i.imgur.com/hxdUvDd.png)

---

### 實例變數的存取方式
#### 車子的引擎號碼變數
```python=
class Car:
    def __init__(self, engin_no = &#34;0000-0000&#34;):
        self.engin_no = engin_no
    def __str__(self):
        return f&#34;Car&#39;s engin_no is  {self.engin_no}&#34;
car1 = Car(&#34;1234-5678&#34;)
print(car1)
car1.engin_no = &#34;2468-1357&#34;
print(car1)
```
```shell
Car&#39;s engin_no is  1234-5678
Car&#39;s engin_no is  2468-1357
```
:::danger
引擎號碼可以改 ！！！
:::

---

##### class diagram
![](https://i.imgur.com/zbPesVK.png)

---

#### @property 實例變數的讀取控制

:::info
@property 裝飾詞將方法轉換為只能讀取的變數
:::

```python=
class Car:
    def __init__(self, engin_no = &#34;0000-0000&#34;):
        self._engin_no = engin_no
    @property # engin_no just can be read
    def engin_no(self):
        return self._engin_no
car1 = Car(&#34;1234-5678&#34;)
print(f&#34;car1.engin_no {car1.engin_no}&#34;)
car1.engin_no = &#34;2468-1357&#34;
```
```shell
car1.engin_no 1234-5678
---------------------------------
AttributeError    Traceback (most recent call last)
&lt;ipython-input-3-dd4183959b5d&gt; in &lt;module&gt;
      7 car1 = Car(&#34;1234-5678&#34;)
      8 print(f&#34;car1.engin_no {car1.engin_no}&#34;)
----&gt; 9 car1.engin_no = &#34;2468-1357&#34;

AttributeError: can&#39;t set attribute
```

---

#### @property 實例變數的修改

:::info
@property 實例變數.setter
:::

```python=
class Car:
    def __init__(self, engin_no = &#34;0000-0000&#34;):
        self._engin_no = engin_no
    @property # engin_no just can be read
    def engin_no(self):
        return self._engin_no
    @engin_no.setter
    def engin_no(self, engin_no):
        self._engin_no = engin_no
    
car1 = Car(&#34;1234-5678&#34;)
print(f&#34;car1.engin_no {car1.engin_no}&#34;)
car1.engin_no = &#34;2468-1357&#34;
print(f&#34;car1.engin_no {car1.engin_no}&#34;)
```
```shell
car1.engin_no 1234-5678
car1.engin_no 2468-1357
```

---

##### class diagram
![](https://i.imgur.com/LjuHkSm.png)

---

### 繼承 ( Inheritance )
:::info
If you inherit money or property, you receive it from someone who has died. &lt;font color=#FF0FF&gt;繼承&lt;/font&gt;
If you inherit a characteristic or quality, you are born with it, because your parents or ancestors also had it. &lt;font color=#FF6600&gt;遺傳&lt;/font&gt;
:::

---

#### Pyhton 類別繼承

:::info
繼承可使類別擁有共同的屬性或方法，將共同的屬性或方法定義在父類別(Parent Class)中，而子類別(Child Class)則透過繼承得到共同的屬性或方法
:::

---

#### 兩種車子類別
```python=
class gasoline_Car:
    def __init__(self, brand, engin):
       self.brand = brand
       self.engin = engin

class electric_Car:
    def __init__(self, brand, battery):
       self.brand = brand
       self.battery = battery

gcar = gasoline_Car(&#34;Totyo&#34;, &#34;Turbo&#34;)
ecar = electric_Car(&#34;Tesla&#34;, &#34;750kw&#34;)
```
:::danger
brand 是一樣的屬性 ...
:::

---

###### class diagram
![](https://i.imgur.com/DsiI8XK.png)

---

#### 車子類別 父類別 -- car
:::info
車子共同的屬性 -- brand
:::
```python=
class car:
    def __init__(self, brand):
       self.brand = brand
    
car = car(&#34;Toyota&#34;)
```
![](https://i.imgur.com/4Bo2pmZ.png)

---

#### 類別繼承

```python=
class child_class(parent_class):
    #super() is parent class
    ...
```


---

###### gasoline_Car 繼承 car 類別

```python=
class car:
    def __init__(self, brand):
       self.brand = brand
    
class gasoline_Car(car):
    def __init__(self, brand, engin):
       super().__init__(brand)
       self.engin = engin
        
gcar = gasoline_Car(&#34;Totyo&#34;, &#34;Turbo&#34;) 
```

---

![](https://i.imgur.com/kRJg2nZ.png)

---

#### 兩種車子繼承 car 類別
```python=
class car:
    def __init__(self, brand):
       self.brand = brand     
class gasoline_Car(car):
    def __init__(self, brand, engin):
       super().__init__(brand)
       self.engin = engin
class electric_Car(car):
    def __init__(self, brand, battery):
       super().__init__(brand)
       self.battery = battery     
gcar = gasoline_Car(&#34;Totyo&#34;, &#34;Turbo&#34;)
ecar = electric_Car(&#34;Tesla&#34;, &#34;750kw&#34;)
```

---

![](https://i.imgur.com/om3x36b.png =700x600)

---

#### 有兩個共同屬性
```python=
class car:
    def __init__(self, brand, engin_no):
       self.brand = brand
       self.engin_no = engin_no
    
class gasoline_Car(car):
    def __init__(self, brand, engin_no, engin):
       super().__init__(brand, engin_no)
       self.engin = engin
        
gcar = gasoline_Car(&#34;Totyo&#34;, &#34;12345678&#34;, &#34;Turbo&#34;) 
```

---

![](https://i.imgur.com/x70qG9O.png)

---

### Operator overloading
| Operator | Method | 
| :--------: | :--------: |
| +	| &#39;object.\_\_add\_\_(self, other) |
|-	|object.\_\_sub\_\_(self, other)|
|*	|object.\_\_mul\_\_(self, other)|
|//	|object.\_\_floordiv\_\_(self, other)|
|/	|object.\_\_div\_\_(self, other)|
|%	|object.\_\_mod\_\_(self, other)|

---

###### \_\_add\_\_() example
```python=
class MyTime:
    def __init__(self, h=0, m=0):
        self.hour = h
        self.min = m
    def __add__(self, other):
        nhour = self.hour+other.hour
        nmin  = self.min+other.min
        if nmin &gt;= 60:
            nhour = nhour + 1
            nmin  -= 60
        if nhour &gt;= 24:
            nhour -= 24
        return MyTime(nhour, nmin) 
    def __str__(self):
        return f&#34;{self.hour:02} : {self.min:02}&#34;
        
time1 = MyTime(22, 40)
time2 = MyTime(2, 30)
time3 = time1 + time2
print(f&#34;{time1} + {time2} = {time3}&#34;)
```
```shell
22 : 40 + 02 : 30 = 01 : 10
```

---
