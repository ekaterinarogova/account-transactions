import datetime

class Operation():
    def __init__(self, info):
        self.info = info
        self.date = datetime.datetime.strptime(self.info['date'], '%Y-%m-%dT%H:%M:%S.%f')
        self.description = self.info['description']
        self.amount = self.info['operationAmount']['amount']
        self.currency = self.info['operationAmount']['currency']['name']
        self.from_card = []
        self.to_card = []

    def get_card_num(self, x):
        try:
            if x == 'to':
                self.to_card = (self.info['to'].split())
                if len(self.to_card) > 2:
                    self.to_card[:2] = [' '.join(self.to_card[:2])]
                return self.to_card
            elif x == 'from':
                self.from_card = (self.info['from'].split())
                if len(self.from_card) > 2:
                    self.from_card[:2] = [' '.join(self.from_card[:2])]
                return self.from_card
            else:
                return 'введено неверное значение'
        except KeyError:
            return ' данных нет'

    def hide_card_num(self, x):
        try:
            if x == 'to':
                number = self.to_card[1]
                if len(number) == 16:
                    return f'{number[:4]} {number[4:6]}** **** {number[:-5:-1]}'
                else:
                    return '*' * 2 + number[:-5:-1]
            elif x == 'from':
                number = self.from_card[1]
                if len(number) == 16:
                    return f'{number[:4]} {number[4:6]}** **** {number[:-5:-1]}'
                else:
                    return '*' * 2 + number[:-5:-1]
        except IndexError:
            return None

    def display_info(self):
        return f'''
        {datetime.datetime.strftime(self.date, "%d.%m.%Y")} {self.description}
        {self.get_card_num('from')[0]} {self.hide_card_num('from')} -> {self.get_card_num('to')[0]} {self.hide_card_num('to')}
        {self.amount} {self.currency}'''

    def __repr__(self):
        return f"""
        Operation ('all info = {self.info}', 'date = {self.date}', 'description = {self.description}', 'amount = {self.amount}',
        'currency = {self.currency}', 'write-off card = {self.from_card}', 'enrollment card{self.to_card}')
        """

