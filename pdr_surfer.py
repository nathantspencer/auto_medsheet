from bs4 import BeautifulSoup
import requests
import re
import code
import sys

# pdr_surf function
def pdr_surf(medications):

    # for each medication passed...
    for medication in medications:

        # search all pages of drugs starting with that letter
        search_url = 'http://www.pdr.net/search-results?q=' + \
            medication.lower()
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'lxml')
        pea_soup = soup.findAll('a', href=re.compile(medication.lower() + \
            '\?druglabelid'), text=re.compile(medication.title()))

        # if found, grab the link to the drug page
        if len(pea_soup) > 0:
            soup_string = str(pea_soup.pop())
            href = re.search('a href="(.*?)"', soup_string)
            med_link = href.group(1)

        # otherwise, break out of the loop
        else:
            print('Could not find "' + medication + '" on PDR.net!')
            break;

        # otherwise, navigate to the drug summary page
        response = requests.get(med_link);
        soup = BeautifulSoup(response.text, 'lxml')
        pea_soup = soup.findAll('a', text=re.compile('Drug Summary'))
        soup_string = str(pea_soup.pop())
        href = re.search('a href="(.*?)"', soup_string)
        reponse = requests.get(href.group(1))

        # parse drug summary page for...
        soup = BeautifulSoup(response.text, 'lxml')

        # medication name

        # generic name

        # class

        # mechanism of action

        # assessment

        # contraindications

# help text and launch of pdr_surf
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('PDR_SURFER -- Written by Nathan Spencer 2016')
        print('Usage: python pdr_surfer.py [drugName1] [drugName2] [...]')
    else:
        pdr_surf(sys.argv[1:])
