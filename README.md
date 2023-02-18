# Задание 3.
# Модуль Datastruct

<aside>
Библиотека Datastruct - разработка пакета, который позволит другим программистам “из коробки” использовать различные структуры данных для эффективной организации работы с данными: их добавления, удаления, хранения и поиска.

</aside>

## Описание задачи

### Описание задачи

- Создайте класс узла `Node`, содержащий два атрибута:
    - данные 
    (сюда будут записываться любые полезные данные: число, строка, список и т.д.)
    - ссылка на следующий узел
- Создайте класс `Stack`, одноименной структуры данных. 
Экземпляр класса `Stack` инициализируется одним атрибутом, хранящим ссылку на верхний (крайний в стэке) узел. Для пустого стэка этот атрибут будет содержать `None`.
- Создайте метод `push` для добавления данных в стэк. 
Создание экземпляра `Node`, для связывания данных в стеке, происходит прям в методе `push`.

###
Ожидаемое поведение
```commandline

n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
print(n2.next_node)
# Результаты вывода в консоли
5
a
<__main__.Node object at 0x0000022803036050>
<__main__.Node object at 0x0000022803036050>

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)
# Результаты вывода в консоли
data3
data2
data1
None
Traceback (most recent call last):
  File "-//-//-", line 29, in <module>
    print(stack.top.next_node.next_node.next_node.data)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'data'
```