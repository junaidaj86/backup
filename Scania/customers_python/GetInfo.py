import yaml
import pandas as pd

def get_authentication_info(customer):
    authentication_info = []
    for mapping in customer.get('principalMappings', []):
        mapping_type = 'mtls' if 'mtls' in mapping else 'oauth'
        service_account = mapping['serviceAccount']
        key = mapping[mapping_type]
        authentication_info.append({'serviceAccount': service_account, 'type': mapping_type, 'key': key})
    return authentication_info

def extract_authentication_info(data):
    result = []
    for customer in data.get('customers', []):
        customer_name = customer.get('name', '')
        authentication_info = get_authentication_info(customer)
        for auth_info in authentication_info:
            result.append({
                'Customer': customer_name,
                'Authentication Type': auth_info['type'],
                'Service Account': auth_info['serviceAccount'],
                'Key': auth_info['key']
            })
    return result

# Load YAML file
with open('customers.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Extract information
customer_info = extract_authentication_info(data)

# Create a DataFrame
df = pd.DataFrame(customer_info)

# Save to Excel file
excel_file_path = 'customer_info.xlsx'
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Excel file saved at: {excel_file_path}")
