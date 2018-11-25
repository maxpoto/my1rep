import random
import xml.etree.ElementTree as ElTr
import json

dataj='''
[
{ "id" : "001",
"x" : "2",
"name" : "Chuck"
} ,
{ "id" : "009",
"x" : "7",
"name" : "Chuck"
}
]'''

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''

info = json.loads(dataj)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

print()

tree = ElTr.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print("CIAO a tutti " + str(random.random()))

elenco = ["Ciao", 23, 12, "WWW"]
dizionario = {"cazzi": 1, "fighe": 0, "culi": 3}
tupla = ("pippo", "baudo", 78)

selezione = input("Give me a number : ")
try:
    if int(selezione) > 10:
        print("Valid number %d" % int(selezione))
    else:
        print("Little number %d" & int(selezione))
except ValueError as err:
    print("ERROR : " + str(err))

print("CIAO \n".rstrip())
