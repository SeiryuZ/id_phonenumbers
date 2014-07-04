
# Indonesia Phone Parser

Work in Progress

## Quickstart (Temporary)
```python
from indonesia_phone_parser import parser
p = parser.Parser('025221123456')
p.parse()

p.is_mobile
p.carrier
p.area_name
p.area_code

```


## Test
```
python -m unittest discover
```
