##Problema A

def thousands_with_commas(i):
  print '{:,}'.format(i)
  formatedValue = '{:,}'.format(i)

  return formatedValue


if __name__ == '__main__':
assert thousands_with_commas(1234) == '1,234'
assert thousands_with_commas(123456789) == '123,456,789'
assert thousands_with_commas(12) == '12'  


