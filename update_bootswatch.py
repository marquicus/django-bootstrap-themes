import os
import json
import urllib.request
import urllib.error

user_agent = 'Mozilla/5.0 (compatible)'

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', user_agent)]

theme_api = opener.open('http://bootswatch.com/api/3.json')
data = json.load(theme_api)
for theme in data['themes']:
    print (theme)
    less_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap_themes', 'static', 'bootstrap', 'themes', theme['name'].lower(), 'less'))
    print (less_path)
    if not os.access(less_path, os.F_OK):
        os.makedirs(less_path)
    if os.access(less_path, os.W_OK):
        try:
            theme_less = opener.open(theme['less'])
        except urllib.error.URLError as error:
            print ("Opening URL " + theme['less'] + " failed!")
            print ("Error: " + error.reason)
            continue;
        try:
            theme_less_file = open(os.path.join(less_path, 'bootswatch.less'), 'w')
            theme_less_file.write(str(theme_less.read()))
            theme_less_file.close()
            theme_less.close()
        except IOError:
            print ("Writing to file " + os.path.join(less_path, 'bootswatch.less') + " failed!")

        try:
            theme_less = opener.open(theme['lessVariables'])
        except urllib.error.URLError as error:
            print ("Opening URL " + theme['lessVariables'] + " failed!")
            print ("Error: " + error.reason)
            continue;
        try:
            theme_less_file = open(os.path.join(less_path, 'variables.less'), 'w')
            theme_less_file.write(str(theme_less.read()))
            theme_less_file.close()
            theme_less.close()
        except IOError:
            print ("Writing to file " + os.path.join(less_path, 'variables.less') + " failed!")

theme_list_file = open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap_themes', 'themes.py')), 'w')
theme_list_file.write('theme_data = ')
theme_list_file.write(json.dumps(data))
theme_list_file.close()
theme_api.close()
