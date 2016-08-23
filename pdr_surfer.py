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
            print('\nFound ' + medication.title() + ' on PDR.net!')
            soup_string = str(pea_soup.pop())
            href = re.search('a href="(.*?)"', soup_string)
            med_link = href.group(1)

        # otherwise, break out of the loop
        else:
            print('\nWARNING: Could not find ' + medication.title() + \
                ' on PDR.net!')
            continue;

        # otherwise, navigate to the drug summary page
        response = requests.get(med_link);
        soup = BeautifulSoup(response.text, 'lxml')
        pea_soup = soup.findAll('a', text=re.compile('Drug Summary'))
        soup_string = str(pea_soup.pop())
        href = re.search('a href="(.*?)"', soup_string)
        drug_summary_link = href.group(1)
        response = requests.get(drug_summary_link)

        # parse drug summary page for...
        soup = BeautifulSoup(response.text, 'lxml')

        # medication name
        medication_name = ''
        pea_soup = soup.findAll('div', { "class" : "drugSummaryLabel" }, \
            text=re.compile(medication.title()))
        if(len(pea_soup) > 0):
            print('Found medication name for ' + medication.title() + '.')
            soup_string = str(pea_soup.pop())
            medication_name = re.search('>(.*?)<', soup_string)
            medication_name = medication_name.group(1)
        else:
            print('WARNING: Could not find medication name for ' + \
                medication.title() + '.')

        # generic name
        generic_name = ''
        pea_soup = soup.findAll('div', { "class" : "drugSummaryLabel" }, \
            text=re.compile('\((.*?)\)'))
        if(len(pea_soup) > 0):
            print('Found generic name for ' + medication.title() + '.')
            soup_string = str(pea_soup.pop())
            generic_name = re.search('\((.*?)\)', soup_string)
            generic_name = generic_name.group(1)
        else:
            print('WARNING: Could not find generic name for ' + \
                medication.title() + '.')

        # therapeutic class
        therapeutic_class = ''
        pea_soup = soup.findAll('h3', { "class" : "drugSummary" }, \
            text=re.compile('THERAPEUTIC CLASS'))
        if(len(pea_soup) > 0):
            print('Found therapeutic class for ' + medication.title() + '.')
            therapeutic_class = pea_soup.pop().nextSibling.nextSibling.text
        else:
            print('WARNING: Could not find therapeutic class for ' + \
                medication.title() + '.')

        # mechanism of action
        mech_of_action = ''
        pea_soup = soup.findAll('h3', { "class" : "drugSummary" }, \
            text=re.compile('MECHANISM OF ACTION'))
        if(len(pea_soup) > 0):
            print('Found mechanism of action for ' + medication.title() + '.')
            mech_of_action = pea_soup.pop().nextSibling.nextSibling.text
        else:
            print('WARNING: Could not find mechanism of action for ' + \
                medication.title() + '.')

        # nursing assessment
        assessment = ''
        pea_soup = soup.findAll('h3', { "class" : "drugSummary" }, \
            text=re.compile('ASSESSMENT'))
        if(len(pea_soup) > 0):
            print('Found nursing assessment for ' + medication.title() + '.')
            assessment = pea_soup.pop().nextSibling.nextSibling.text
        else:
            print('WARNING: Could not find nursing assessment for ' + \
                medication.title() + '.')

        # adverse reactions
        adverse_reactions = ''
        pea_soup = soup.findAll('h3', { "class" : "drugSummary" }, \
            text=re.compile('ADVERSE REACTIONS'))
        if(len(pea_soup) > 0):
            print('Found adverse reactions for ' + medication.title() + '.')
            adverse_reactions = pea_soup.pop().nextSibling.nextSibling.text
        else:
            print('WARNING: Could not find adverse reactions for ' + \
                medication.title() + '.')

    print('')

# help text and launch of pdr_surf
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('PDR_SURFER -- Written by Nathan Spencer 2016')
        print('Usage: python pdr_surfer.py [drugName1] [drugName2] [...]')
    else:
        pdr_surf(sys.argv[1:])
