import requests
from bs4 import BeautifulSoup

def get_attack_id_from_user():
    attack_id = input("Enter the MITRE ATT&CK ID (e.g., T1548): ")
    return attack_id

def fetch_mitre_attack_details(attack_id):
    url = f"https://attack.mitre.org/techniques/{attack_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.RequestException as e:
        return {"Error": str(e)}

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
    title_element = soup.find('h1')
    if title_element:
        attack_details['Title'] = title_element.text.strip()

    # Extract description 
    description_element = soup.find('div', {'class': 'description'})  # Assuming class is 'description'
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
