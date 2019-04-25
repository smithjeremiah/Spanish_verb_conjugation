import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

import sqlite3



while True:

    verb = input('Enter Spanish verb here:')

    url = 'https://www.123teachme.com/spanish_verb_conjugation/' + verb

    fh = urllib.request.urlopen(url)


    soup = BeautifulSoup(fh,'html.parser')

    arr =['None','English', 'Yo', 'Tu', 'Ud., el, ella', 'nosotros', 'vosotros', 'Uds., ellos, ellas']

    pst = soup('td')

    lrst =[]
    cnt = 1

    for i in pst:
        lrst.append(i.string)


    try:
        while cnt < 8:

            print(arr[cnt] + ' ' + lrst[cnt])
            cnt += 1
    except:
        print('Verb not found. Please enter the infinitive form of a valid Spanish verb.')
        continue









    # for i in pst:
    #     print(i.string)
