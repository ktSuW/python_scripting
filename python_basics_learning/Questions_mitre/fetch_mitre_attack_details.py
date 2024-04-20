import requests
from bs4 import BeautifulSoup

# Not working , need to debug this

def get_attack_id_from_user():
    attack_id = input("Enter the MITRE ATT&CK ID (e.g., T1548): ")
    return attack_id

def fetch_mitre_attack_details(attack_id):
    url = f"https://attack.mitre.org/techniques/{attack_id}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize results dictionary
    attack_details = {
        'Title': '',
        'Description': '',
        'Details': {
            'ID': attack_id,
            'Sub-techniques': [],
            'Other Details': {}
        }
    }

    # Extract title
    title_element = soup.find('h1', {'data-testid': 'page-title'})
    if title_element:
        attack_details['Title'] = title_element.text.strip()

    # Extract description
    description_element = soup.find('div', {'data-testid': 'description'})
    if description_element:
        attack_details['Description'] = description_element.text.strip()

    # Extract sub-techniques
    sub_techniques_links = soup.find_all('a', href=lambda href: href and 'subtechniques' in href)
    for link in sub_techniques_links:
        if link:
            attack_details['Details']['Sub-techniques'].append(link.text.strip())

    # Extract other details from detail tables
    details_table = soup.find_all('tr', {'class': 'details-table__row'})
    for row in details_table:
        th_element = row.find('th')
        td_element = row.find('td')
        if th_element and td_element:
            key = th_element.text.strip()
            value = td_element.text.strip()
            attack_details['Details']['Other Details'][key] = value
        
    return attack_details

def main():
    attack_id = get_attack_id_from_user()
    attack_details = fetch_mitre_attack_details(attack_id)
    print(attack_details)

if __name__ == '__main__':
    main()



"""
requests, https://pypi.org/project/requests/
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!


"""