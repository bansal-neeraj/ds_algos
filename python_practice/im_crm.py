import requests

dt_range = 'start_time=14-June-2022&end_time=20-June-2022'

# im_url = f'https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key=mR22F7xr4X3JSfet5HWM7l2Ko1vHnjI='
api_key = 'mR22F7xr4X3JSfet5HWM7l2Ko1vHnjI='
im_url = f'https://mapi.indiamart.com/wservce/crm/crmListing/v2/?glusr_crm_key={api_key}&{dt_range}'
print(im_url)
r = requests.get(im_url)
r = r.json()

print(r)

data = {'CODE': 200, 'STATUS': 'SUCCESS', 'MESSAGE': '', 'TOTAL_RECORDS': 3, 'RESPONSE': [
    {'UNIQUE_QUERY_ID': '377413064', 'QUERY_TYPE': 'P', 'QUERY_TIME': '2022-04-29 13:09:49',
     'SENDER_NAME': 'Vinayak Kondaskar', 'SENDER_MOBILE': '+91-7045104104', 'SENDER_EMAIL': 'vinayak@kanchidesigns.com',
     'SENDER_COMPANY': 'Kanchi Designs Pvt. Ltd.',
     'SENDER_ADDRESS': 'R-236, ITC Industrial Area, MIDC, Rabale, Navi Mumbai, Maharashtra,         400701',
     'SENDER_CITY': 'Navi Mumbai', 'SENDER_STATE': 'Maharashtra', 'SENDER_COUNTRY_ISO': 'IN', 'SENDER_MOBILE_ALT': '',
     'SENDER_EMAIL_ALT': '', 'QUERY_PRODUCT_NAME': '', 'QUERY_MESSAGE': '', 'CALL_DURATION': '314',
     'RECEIVER_MOBILE': '9833519187'},
    {'UNIQUE_QUERY_ID': '2131702729', 'QUERY_TYPE': 'W', 'QUERY_TIME': '2022-04-29 13:08:48',
     'SENDER_NAME': 'Vinayak Kondaskar', 'SENDER_MOBILE': '+91-7045104104', 'SENDER_EMAIL': 'vinayak@kanchidesigns.com',
     'SENDER_COMPANY': 'Kanchi Designs Pvt. Ltd.',
     'SENDER_ADDRESS': 'R-236, ITC Industrial Area, MIDC, Rabale, Navi Mumbai, Maharashtra,         400701',
     'SENDER_CITY': 'Navi Mumbai', 'SENDER_STATE': 'Maharashtra', 'SENDER_COUNTRY_ISO': 'IN', 'SENDER_MOBILE_ALT': '',
     'SENDER_EMAIL_ALT': '', 'QUERY_PRODUCT_NAME': '',
     'QUERY_MESSAGE': 'QR code activation on our Home furnishing fabrics with details<br>', 'CALL_DURATION': '',
     'RECEIVER_MOBILE': ''},
    {'UNIQUE_QUERY_ID': '468562708', 'QUERY_TYPE': 'B', 'QUERY_TIME': '2022-04-29 13:07:45',
      'SENDER_NAME': 'Manish Kumar', 'SENDER_MOBILE': '+91-8802886205',
      'SENDER_EMAIL': 'mkumar57089@gmail.com', 'SENDER_COMPANY': '',
      'SENDER_ADDRESS': 'Delhi, Delhi', 'SENDER_CITY': 'Delhi', 'SENDER_STATE': 'Delhi',
      'SENDER_COUNTRY_ISO': 'IN', 'SENDER_MOBILE_ALT': '', 'SENDER_EMAIL_ALT': '',
      'QUERY_PRODUCT_NAME': 'Pathology Laboratory Reporting Software',
      'QUERY_MESSAGE': 'My Requirement is for Pathology Laboratory Reporting Software. Kindly send me price and other details.<br>Quantity : 1 Piece<br>Probable Order Value : Rs. 10,000 to 20,000<br>Probable Requirement Type : Business Use<br>',
      'CALL_DURATION': '', 'RECEIVER_MOBILE': ''}]}
