def split_into_lines(text):
    return text.splitlines()

def x_delete(list):
    new_list = []
    for line in list:
        x_delete = line.rstrip("×")
        new_list.append(x_delete)
    return new_list

def tab_split(list):
    new_list = []
    for line in list:
        split = line.split("\t")
        new_list.append(split)
    return new_list

def type_delete(list_of_lists):
    for list in list_of_lists:
        list.pop(1)
        list.pop(2)
    return list_of_lists

def collector_shorten(list_of_lists):
    for list in list_of_lists:
        if len(list[0]) > 3:
            list[0] = list[0][0:3]
    return list_of_lists


def rearrange(list_of_lists):
    new_list = []
    for list in list_of_lists:
        moved = list [2] + " " + list[1] + "  " + list[0]
        new_list.append(moved)
        #print(moved)

    return(new_list)

def merge(list):
    res = ''
    for string in list:
        res += string + "\n"

    res = res.strip() 
    return res