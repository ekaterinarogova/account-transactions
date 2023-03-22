from utils.class_operate import Operation
from utils.funcs import load_data, sort_data, pick_latest
import os.path


def main():
    file = os.path.abspath('operations.json')
    sorted_data = sort_data(load_data(file))
    latest_operations = pick_latest(sorted_data)

    for i in latest_operations:
        # цикл перебора по списку последних выполненных операций с созданием экземпляров класса Operation
        example = Operation(i)
        print(example.display_info())


if __name__ == '__main__':
    main()
