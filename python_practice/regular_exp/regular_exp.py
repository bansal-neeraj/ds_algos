import re

# pattern = re.compile(r'\d')
pattern = re.compile(r'[<]{2}[\w]+[>]{2}')

txt_srh = 'This the status report for'
# txt_srh = 'This the status report for <<actual_end_date>>'
# txt_srh = 'This a lead <<to_be_contacted_date>> tempate <<PROFILE_first_name>>'
# txt_srh = '<<assigned_date>><<assigned_division>>'
# txt_srh = '"aa6?9"'

matches = pattern.finditer(txt_srh)
found = pattern.search(txt_srh)
print(found)
# loc_list = []
# for match in matches:
#     print(match.span())
#     st, end = match.span()
#     loc_list.append(st)
#     print(txt_srh[st+2:end-2])
#     # print(st,end)
#     # print(txt_srh[st])
#     # print(txt_srh[end-1])
#
# pattern = re.compile('[a]+')
# text = 'abbaacaaa'
#
# matches = pattern.finditer(text)
# for match in matches:
#     print(match.group())