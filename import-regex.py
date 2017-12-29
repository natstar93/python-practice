import re
for item in ['abc', '$%^']:
    if re.match('\w', item):
        print('👍 Yay a match: {item}'.format(item=item))
    else:
        print('😡 Boo, not a match: {item}'.format(item=item))
