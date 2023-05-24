# How to use pytest

## Start
-v : 詳細資訊  
-s : 顯示所有訊息(包含print)  
- 執行指令  

```
pytest unit_test_session.py -v
```
- 匯出報表
```
pytest unit_test_session.py -v --junitxml=report.xml
```
## 匯出含覆蓋率報表
- 下載需求套件
```
python -m pip install pytest-cov
```
- 執行指令
```
py.test {test.py} --cov={project-dir} --cov-report={output type}
ex: py.test testMain.py --cov=../ --cov-report=xml
```
## 特殊用法
依據function命名，有特殊功能
- setup_method  
可在每個測試funtion執行前自動執行此function  
ex:
```
class TestCase():
    def setup_method(self):
        print('testStart')
    
    def test_this(self):
        print('hi')

    def test_this2(self):
        print('hi2')
```
>> testStart  
>> hi  
>> testStart  
>> hi2

- teardown_method  
可在每個測試funtion結束後自動執行此function
ex:
```
class TestCase():
    def teardown_method(self):
        print('testEnd')
    
    def test_this(self):
        print('hi')

    def test_this2(self):
        print('hi2')
```
>> hi  
>> testEnd  
>> hi2  
>> testEnd  
- setup_class
在該測試類別執行前執行此function，每個類別只會有觸發一次  
ex:
```
class TestCase():
    def setup_class(self):
        print('testStart')
    
    def test_this(self):
        print('hi')

    def test_this2(self):
        print('hi2')
```
>> testStart  
>> hi
>> hi2

- teardown_class  
在該測試類別結束後執行此function，每個類別只會有觸發一次 
ex:
```
class TestCase():
    def teardown_class
        print('testEnd')
    
    def test_this(self):
        print('hi')

    def test_this2(self):
        print('hi2')
```
>> hi  
>> hi2  
>> testEnd
