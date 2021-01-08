import datetime


def str_into_date(str_date):
    date = str_date.split("/")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])
    return datetime.date(year, month, day)

def list_to_str_space(list):
    string = ""
    for element in list:
        string += str(element)+ " "
    return string.strip()

def str_space_to_int_list(string):
    string_list = string.split(" ")
    int_list = []
    if string_list != '':
        for element in string_list:
            if element != '':
                int_list.append(int(element))
    return int_list

if __name__ == "__main__":
    test = list_to_str_space([2, 1])
    print(test)
    print(str_space_to_int_list(test))
    print(str_space_to_int_list(' '))