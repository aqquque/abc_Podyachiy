def shift_bits(number, shift, left=True):
  if left:
    result = number << shift
  else:
    result = number >> shift
  print(f"Исходное число: {number}, Двоично: {bin(number)}")
  print(f"Результат сдвига: {result}, Двоично: {bin(result)}")
  return result



num = int(input("Введите целое число: "))
shift = int(input("Введите количество битов для сдвига: "))
direction = input("Сдвинуть влево (l) или вправо (r)? (l/r): ")

left_shift = direction.lower() == 'l'

result = shift_bits(num, shift, left_shift)
print(f"Результат сдвига: {result}")