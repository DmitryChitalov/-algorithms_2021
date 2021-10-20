import re

def log_parse(src):
    re_list = [r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s',
               r'\[(.*?)\]',
               r'\"([A-Z]{3})',
               r'\s(\/[\w\/]+)',
               r'\s(\d{3})\s',
               r'\s\d{3}\s(\d+)']
    try:
        result = list(re.findall(x, src)[0] for x in re_list)
    except IndexError:  # шаблон для особых строк
        # re_list[0] = '([0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4})\s'
        # result = list(re.findall(x, src)[0] for x in re_list)
        result = ['','','','', '', '']
    # print(result)
    return result


if __name__ == '__main__':
    exit(0)
