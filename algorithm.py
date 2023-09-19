import math
import random
import time

from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информирующий класс."""

    sort_massive: list[int]
    size_massive: int
    sort_type: str
    time_method: time

    def get_message(self) -> str:
        """Сообщение о сортировке."""
        return (
            f'Массив отсортирован!\n'
            f'Тип сортировки: {self.sort_type}.\n'
            f'Время выполнения: {self.time_method:6f} сек.\n'
            f'Размер массива: {self.size_massive}.'
        )


class MyObject:
    """Объект, от которого будет происходить сортировка"""

    def __init__(self, size: int) -> None:
        self.size = size

    def get_unsorted_massive(self) -> list[int]:
        """Создание массива."""
        unsorted_massive: list[int] = [random.randint(-99999, 99999) for i in range(self.size)]
        return unsorted_massive

    def do_sort(self):
        """Алгоритм сортировки."""
        raise NotImplementedError(
            'Метод должен быть переопределен в дочернем классе.'
        )


class BubbleSort(MyObject):
    """Сортировка обменом."""

    def do_sort(self) -> list[int]:
        """Алгоритм сортировки."""
        massive: list[int] = self.get_unsorted_massive()

        for i in range(len(massive) - 1):
            for j in range(len(massive) - i - 1):
                if massive[j] > massive[j + 1]:
                    massive[j], massive[j + 1] = massive[j + 1], massive[j]

        return massive


class InsertSort(MyObject):
    """Сортировка вставками."""

    def do_sort(self) -> list[int]:
        """Алгоритм сортировки."""
        massive: list[int] = self.get_unsorted_massive()

        for i in range(len(massive)):
            j: int = i - 1
            key = massive[i]
            while massive[j] > key and j >= 0:
                massive[j + 1] = massive[j]
                j -= 1
            massive[j + 1] = key

        return massive


class SelectionSort(MyObject):
    """Сортировка выбором"""

    def do_sort(self) -> list[int]:
        """Алгоритм сортировки."""
        massive: list[int] = self.get_unsorted_massive()

        for i in range(0, len(massive) - 1):
            smallest: int = i
            for j in range(i + 1, len(massive)):
                if massive[j] < massive[smallest]:
                    smallest = j
            massive[i], massive[smallest] = massive[smallest], massive[i]

        return massive


class QuickSort(MyObject):
    """Быстрая сортировка"""

    @staticmethod
    def quick_sort(massive: list[int]) -> list[int]:
        """Алгоритм сортировки."""
        if len(massive) <= 1:
            return massive
        else:
            q = random.choice(massive)
        l_nums: list[int] = [n for n in massive if n < q]

        e_nums: list[int] = [q] * massive.count(q)
        b_nums: list[int] = [n for n in massive if n > q]

        return (
            (
                QuickSort.quick_sort(l_nums) + e_nums
            ) + QuickSort.quick_sort(b_nums)
        )

    def do_sort(self) -> list[int]:
        """Отправная точка"""
        massive: list[int] = self.get_unsorted_massive()
        sorted_massive: list[int] = QuickSort.quick_sort(massive)

        return sorted_massive


class HeapSort(MyObject):
    """Пирамидальная сортировка."""

    @staticmethod
    def heapify(massive: list[int], size: int, i: int):
        """Процедура для преобразования в двоичную кучу поддерева."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < size and massive[i] < massive[left]:
            largest = left

        if right < size and massive[largest] < massive[right]:
            largest = right

        if largest != i:
            massive[i], massive[largest] = massive[largest], massive[i]
            HeapSort.heapify(massive, size, largest)

    @staticmethod
    def heap_sort(massive: list[int]) -> list[int]:
        """Алгоритм сортировки."""
        for i in range(len(massive), -1, -1):
            HeapSort.heapify(massive, len(massive), i)

        for i in range(len(massive) - 1, 0, -1):
            massive[i], massive[0] = massive[0], massive[i]
            HeapSort.heapify(massive, i, 0)

        return massive

    def do_sort(self) -> list[int]:
        """Отправная точка."""
        massive: list[int] = self.get_unsorted_massive()
        sorted_massive: list[int] = HeapSort.heap_sort(massive)

        return sorted_massive


class ShellSort(MyObject):
    """Сортировка Шелла."""

    def do_sort(self) -> list[int]:
        """Алгоритм сортировки."""
        massive: list[int] = self.get_unsorted_massive()
        size: int = len(massive)
        k: int = int(math.log2(size))
        interval: int = 2 ** k - 1
        while interval > 0:
            for i in range(interval, size):
                temp: int = massive[i]
                j: int = i
                while j >= interval and massive[j - interval] > temp:
                    massive[j] = massive[j - interval]
                    j -= interval
                massive[j] = temp
            k -= 1
            interval = 2 ** k - 1

        return massive


class MergeSort(MyObject):
    """Сортировка слиянием."""

    @staticmethod
    def merge(list1: list[int], list2: list[int]) -> list[int]:
        lst: list[int] = []
        i: int = 0
        j: int = 0
        while i <= len(list1) - 1 and j <= len(list2) - 1:
            if list1[i] < list2[j]:
                lst.append(list1[i])
                i += 1

            else:
                lst.append(list2[j])
                j += 1

        if i > len(list1) - 1:
            while j <= len(list2) - 1:
                lst.append(list2[j])
                j += 1

        else:
            while i <= len(list1) - 1:
                lst.append(list1[i])
                i += 1

        return lst

    @staticmethod
    def merge_sort(massive) -> list[int]:
        """Алгоритм сортировки."""
        if len(massive) == 1:
            return massive

        mid: int = (len(massive) - 1) // 2
        list1: list[int] = MergeSort.merge_sort(massive[:mid + 1])
        list2: list[int] = MergeSort.merge_sort(massive[mid + 1:])
        result: list[int] = MergeSort.merge(list1, list2)

        return result

    def do_sort(self) -> list[int]:
        massive: list[int] = self.get_unsorted_massive()
        sorted_massive: list[int] = MergeSort.merge_sort(massive)

        return sorted_massive


# Список классов.
DATABASE_CLASSES: list[type[MyObject]] = [
        BubbleSort,
        InsertSort,
        SelectionSort,
        QuickSort,
        HeapSort,
        ShellSort,
        MergeSort,
]

# Список размеров массива.
DATABASE_SIZES: list[int] = [
    5000,
    10000,
    100000,
    150000
]


def main(my_object: MyObject, size: int) -> None:
    """Функция получения ответа"""
    sort_type: str = type(my_object).__name__

    start_time: time = time.time()
    sorted_massive: list[int] = my_object.do_sort()
    end_time: time = time.time()

    execution_time: time = end_time - start_time

    info = InfoMessage(sorted_massive, size, sort_type, execution_time)
    print(info.get_message())
