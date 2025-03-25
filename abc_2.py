import struct

def find_max(data):
    """
    Находит максимальное число в байтовой строке (IEEE 754 float).
    """
    numbers = []
    for i in range(0, len(data), 4):  # Читаем по 4 байта (float32)
        chunk = data[i:i+4]
        if len(chunk) == 4: # Убедимся, что у нас есть полные 4 байта
            num = struct.unpack('f', chunk)[0]
            numbers.append(num)

    if not numbers:
        return None

    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Пример использования:
numbers = [1.5, 2.7, -3.0, 4.2, 5.9]  # Список чисел
data = b""
for num in numbers:
    data += struct.pack('f', num) # Упаковываем в байты

max_num = find_max(data)

if max_num is not None:
    print("Максимальное число:", max_num)
else:
    print("Список пуст.")
