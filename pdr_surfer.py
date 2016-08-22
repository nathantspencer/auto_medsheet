from bs4 import BeautifulSoup
import requests
import re
import code
import sys

def pdr_surf(medications):
    for medication in medications:
        med_link = ''
        first_letter = medication[0]
        for page_number in range(1,19):
            search_url = 'http://www.pdr.net/browse-by-drug-name?letter=' + \
                first_letter + '&currentpage=' + str(page_number)
            response = requests.get(search_url)
            soup = BeautifulSoup(response.text, 'lxml')
            pea_soup = soup.findAll('a', href=re.compile(medication.lower() + \
                '\?druglabelid'), text=re.compile(medication.title()))
            if len(pea_soup) > 0:
                soup_string = str(pea_soup.pop())
                href = re.search('a href="(.*?)"', soup_string)
                med_link = href.group(1)
                break;
            if page_number == 19:
                print('Could not find ' + medication + ' on PDR.net!')
                break;
        if med_link == '':
            break;
        response = requests.get(med_link);
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('PDR_SURFER -- Written by Nathan Spencer 2016')
        print('Usage: python pdr_surfer.py [drugName1] [drugName2] [...]')
    else:
        pdr_surf(sys.argv[1:])
