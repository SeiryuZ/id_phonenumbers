# Indonesia Phonenumber Parser


## Quickstart
```python
from id_phonenumbers import parse

number = parse('025221123456')

number.is_mobile
number.regional_number
number.carrier

```


## Test
```
python -m unittest discover
```
