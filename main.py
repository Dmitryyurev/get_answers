import requests

cookies = {
    '__utmb': '201925707',
    'cf_clearance': 'Wo3eavoYZS670sk6apuT_XDTzN13BWVQfRUF4phCggk-1755901226-1.2.1.1-J9xvHuZHzoIi57C8BZfTbqlhe8FaMN5XU39ocjIqw2NnvPbxAzmiXdiQ.oVY4s5zd0fb7BDiEK7UNP72t3eV3etDzChzV0A09nh5t1cwQqN5GGV9MgQMW1tNXWV6nJ7Eh7xD8gGyjuNMLDuIpBcUJX6TotxwWoQb9FUtMfIS8.QW1O3WEh76psrM7rVpqbPEVmOlVcPzxTTRv9B3Yz2yUSBj9TediSNSg3f.HZDlv2A',
    '__utma': '201925707.940702101.1755897454.1755897454.1755899352.2',
    'PHPSESSID': '7f54f0548a7c89a136590e2af8e5c9be',
    '__utmc': '201925707',
    '__utmz': '201925707.1755897454.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none)',
}

headers = {
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    # 'Cookie': '__utmb=201925707; cf_clearance=Wo3eavoYZS670sk6apuT_XDTzN13BWVQfRUF4phCggk-1755901226-1.2.1.1-J9xvHuZHzoIi57C8BZfTbqlhe8FaMN5XU39ocjIqw2NnvPbxAzmiXdiQ.oVY4s5zd0fb7BDiEK7UNP72t3eV3etDzChzV0A09nh5t1cwQqN5GGV9MgQMW1tNXWV6nJ7Eh7xD8gGyjuNMLDuIpBcUJX6TotxwWoQb9FUtMfIS8.QW1O3WEh76psrM7rVpqbPEVmOlVcPzxTTRv9B3Yz2yUSBj9TediSNSg3f.HZDlv2A; __utma=201925707.940702101.1755897454.1755897454.1755899352.2; PHPSESSID=7f54f0548a7c89a136590e2af8e5c9be; __utmc=201925707; __utmz=201925707.1755897454.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none)',
    'Referer': 'https://kpolyakov.spb.ru/school/ege.htm',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Accept-Language': 'ru',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15',
    'X-Requested-With': 'XMLHttpRequest',
    'Priority': 'u=3, i',
}





def check_answer(type, number, user_answer):
    user_answer, number, type = str(user_answer), str(number), str(type)
    params = {
        'egeNo': type,
        'topicNo': number,}
    response = requests.get('https://kpolyakov.spb.ru/school/ege/getanswer.php', params=params, cookies=cookies,
                            headers=headers).text
    if response:
        if str(response) == str(user_answer):
            return f'Верно({type}-{number}-{user_answer})'
        elif response[0].isdigit():
            return f'Неверно, верный ответ: {response}'
        else:
            print(response)
            return 'Ошибка'
    else:
        return 'Такого задания нет'

while True:
    data = input().split(' ')
    print(check_answer(data[0], data[1], data[2]))
