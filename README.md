# Indonesia Phonenumber Parser

## Installation
```sh
pip install id_phonenumbers
```


## Quickstart
```python
from id_phonenumbers import parse

number = parse('025221123456')

number.is_mobile
number.regional_number
number.carrier

```


## Test
```sh
python -m unittest discover
```
