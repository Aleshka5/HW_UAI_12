import requests
import pprint
import json
import time

DOMAIN = 'https://api.hh.ru/'

url_vacancies = f'{DOMAIN}vacancies'
url_areas = 'https://api.hh.ru/areas/'
dict_requirement = {}
for page_num in range(10):
    time.sleep(1)
    params = {
        'text': 'python developer',
        'page': page_num,
        'area': 1
    }
    result = requests.get(url_vacancies, params = params).json()
    pprint.pprint(result)
    for i in range(4000):
        try:
            str_result = result['items'][i]['snippet']['requirement'].replace('<highlighttext>', ' ').replace('</highlighttext>', ' ')
            for simbol in [',','.','/',':','\\','(',')','?','!',';','+','-','0','1','2','3','4','5','6','7','8','9']:
                str_result = str_result.replace(simbol,' ')
            str_result = str_result.replace('     ', ' ')
            str_result = str_result.replace('    ', ' ')
            str_result = str_result.replace('   ', ' ')
            str_result = str_result.replace('  ',' ')
            str_result = str_result.split(' ')
            for word in str_result:
                if len(word) > 0:
                    if (word.lower().find('а') == -1) and (word.lower().find('в') == -1)and (word.lower().find('о') == -1)and (word.lower().find('п') == -1)and (word.lower().find('е') == -1)and (word.lower().find('и') == -1)and (word.lower().find('с') == -1)and (word.lower().find('д') == -1):
                        try:
                            dict_requirement[word.lower()] += 1
                        except:
                            dict_requirement[word.lower()] = 1
        except:
            print(f'Index:{i}')
            break

dict_requirement = sorted(dict_requirement.items(),key=lambda item: item[1],reverse=True)
pprint.pprint(dict_requirement)
with open('res.json','w') as f:
    json.dump(dict_requirement,f)


