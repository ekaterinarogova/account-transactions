from funcs import load_data, sort_data, pick_latest
from class_operate import Operation

def main():
    file = 'operations.json' #исходный файл json с данными
    sorted_data = sort_data(load_data(file))
    latest_operations = pick_latest(sorted_data)

    for i in latest_operations:
    #цикл перебора по списку последних выполненных операций с созданием экземпляров класса Operation
        example = Operation(i)
        print(example.display_info())


if __name__ == '__main__':
    main()
