# Decoding 2

#### Our officers have obtained some encrypted codes. See if you can decode them. We know they should start with "SKY".

Since they tell us that the start with "SKY" we can use python to determin the number of characters rotated and then use an online [tool](https://cryptii.com/pipes/caesar-cipher) to decode.

1. `FXL-TUHX-1271`
```python
>>> ord('S') - ord('F')
13
```


<details>
  <summary>Flag</summary>

    SKY-GHUK-1271
</details>

2. `HZN-ADQU-4229`
```python
>>> ord('S') - ord('H')
11
```


<details>
  <summary>Flag</summary>

    SKY-LOBF-4229
</details>
