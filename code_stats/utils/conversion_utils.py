from code_stats.bin.logger import Logger

def convert_dict_to_list(dictionary):
    """
    Accepts a dictionary and return a list of lists.
    @example:   input : { "python" : 50, "json": 100, "text" : 20}
                output : [['python', 50], ['json', 100], ['text', 20]]
    """
    output_list = []
    for k in dictionary.keys():
        output_list.append([k, dictionary[k]])

    return output_list

def convert_dicts_to_list(*dicts):
    """
    Accepts mutiple dictions with the same keys and return a list of lists.
    @example : Input = {"python" : 50, "json": 100, "text" : 20}
                       {"python" : .5, "json": .3, "text" : .2}
               Output = [['python', 50, .5], ['json', 100, .3], ['text', 20, .2]]
    """
    output_list = []
    # Check if all the dicts have the same keys.
    dict_keys = dicts[0].keys()
    for i in range(1, len(dicts)):
        cur_dict = dicts[i]
        if not are_keys_equal(cur_dict.keys(), dict_keys):
            Logger().verbose_print("Mismatching keys in Dictionary while conver\
            ting dictionaries in to list of lists", v_lvl=0, msg_tpe="error")
            return None

    for k in dict_keys:
        stat_per_key = [k]
        for dictionary in dicts:
            stat_per_key.append(dictionary[k])

        output_list.append(stat_per_key)

    return output_list

def are_keys_equal(keys_1, keys_2):
    for i in keys_1:
        if i not in keys_2:
            return False

    return True

def convert_csv_to_list(string):
    """
    Convert Cauma separated single string to list.
    """
    return string.split(",")
