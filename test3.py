


def remove_space(str):
    """
        remove space
    """
    str_no_space = str.replace(' ', '')
    return str_no_space

def remove_dollar(str):
    """
        remove $
    """
    if '$' in str:
        return str.replace('$', '')
    else:
        return str

def clean_str_lst(str_lst, operations):
    """
        clean string list
    """
    #函数式编程
    result = []
    for item in str_lst:
        for op in operations: #遍历函数
            item = op(item)
        result.append(item)
    return result

if __name__ == '__main__':
    # 处理字符串
    str_lst = ['$1.123', ' $1123.454', '$899.12312']
    clean_operations = [remove_space, remove_dollar]
    result = clean_str_lst(str_lst, clean_operations)
    print (result)