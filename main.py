#!venv/bin/python3.11
from abc import ABC, abstractmethod


class Customer:
    def __init__(self, full_name):
        self.ru_last_name = full_name[0].lower().title()
        self.ru_first_name = full_name[1].lower().title()

        if len(full_name) >= 3:
            self.ru_patronimyc = full_name[2].lower().title()
        else:
            self.ru_patronimyc = ""

        self.eng_last_name = ""
        self.eng_first_name = ""

        if len(full_name) >= 3:
            self.eng_patronimyc = ""
        else:
            self.eng_patronimyc = "n"

        for ch in full_name[0].lower():
            self.eng_last_name += Transliter.translit(ch, self.eng_last_name)
        self.eng_last_name = self.eng_last_name.replace("ь", "")
        self.eng_last_name = self.eng_last_name.replace("ъ", "").title()

        for ch in full_name[1].lower():
            self.eng_first_name += Transliter.translit(ch, self.eng_first_name)
        self.eng_first_name = self.eng_first_name.replace("ь", "")
        self.eng_first_name = self.eng_first_name.replace("ъ", "").title()

        if len(full_name) >= 3:
            for ch in full_name[2].lower():
                self.eng_patronimyc += Transliter.translit(ch, self.eng_patronimyc)
            self.eng_patronimyc = self.eng_patronimyc.replace("ь", "")
            self.eng_patronimyc = self.eng_patronimyc.replace("ъ", "").title()

        self.mail_prefix = self.eng_first_name.lower() + "." + self.eng_last_name.lower()
        self.email = self.mail_prefix

        if len(full_name) >= 3:
            self.login = self.eng_last_name.lower() + "." + Transliter.translit(full_name[1].lower()[0], full_name[
                1].lower()) + Transliter.translit(full_name[2].lower()[0], full_name[2].lower())
        else:
            self.login = self.eng_last_name.lower() + "." + Transliter.translit(full_name[1].lower()[0],
                                                                                full_name[1].lower()) + \
                         self.eng_patronimyc.lower()[0]


class Transliter(ABC):
    char_dict = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",  # e, ye
        "ё": "e",  # e, ye
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ъ": "ъ",
        "ы": "y",
        "ь": "ь",
        "э": "e",
        "ю": "yu",
        "я": "ya",
        "-": "-"
    }

    @abstractmethod
    def translit(self, word):
        word.lower()
        if self == "е" and len(word) != 0:
            if word[-1] == "ъ" or word[-1] == "ь":
                return "ye"

        if self == "ё":
            if len(word) == 0 or word[-1] == "ъ" or word[-1] == "ь":
                return "ye"

        if self == " ":
            return "-"

        return Transliter.char_dict[self]


def namer(name):
    name = name.replace(',', '')
    name = name.lower()
    name = name.strip()
    customer = Customer(name.split())
    mail = customer.email
    login = customer.login
    long = f'[  {name}  |  {login}  |  {mail}  ]'
    print(long)
    print('-'*len(long))


def read_input():
    input_list = []
    while True:
        input_data = input()
        if input_data:
            input_list.append(input_data)
        else:
            break
    return input_list


def cuc(input_list):
    for one in input_list:
        namer(one)


if __name__ == '__main__':
    cuc(read_input())
