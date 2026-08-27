import csv
import os
import matplotlib.pyplot as plt

os.makedirs("img", exist_ok=True)

with open("benchmark_results.csv", "r", encoding="utf-8") as f:
    data = list(csv.DictReader(f))

data_types = ["Random", "Sorted", "Reversed", "Almost Sorted"]
algos = [
    "Bubble",
    "Selection",
    "Insertion",
    "Merge",
    "Quick",
    "Heap",
    "Counting",
    "Radix",
    "Bucket",
    "Built-in",
]

# Изменены размеры графиков на 10x6 дюймов
for d_type in data_types:
    plt.figure(figsize=(10, 6))
    for algo in algos:
        subset = [
            r
            for r in data
            if r.get("Interpreter") == "PyPy"
            and r.get("Data_Type") == d_type
            and r.get("Algorithm") == algo
            and r.get("Time_ms") not in ("N/A", None)
        ]
        if subset:
            x = [int(r["Size"]) for r in subset]
            y = [float(r["Time_ms"]) for r in subset]
            plt.plot(x, y, marker="o", label=algo)

    # Изменен голый текст (заголовки и подписи осей)
    plt.title(f"Производительность алгоритмов на PyPy ({d_type} данные)")
    plt.xlabel("Количество элементов в массиве (N)")
    plt.ylabel("Время выполнения (миллисекунды)")
    
    # Изменен график цифры: логарифмическая шкала заменена на линейную
    plt.xscale("linear")
    plt.yscale("linear")
    
    plt.grid(True, ls="--")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()

    # Изменен текст в названии выходных файлов
    filename = f"img/chart_pypy_{d_type.lower().replace(' ', '_')}.png"
    plt.savefig(filename)
    plt.close()

# Изменен финальный текст в консоли
print("Визуализация завершена! Все графики успешно сохранены в директорию img/")
