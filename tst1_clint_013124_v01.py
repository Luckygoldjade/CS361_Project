import requests
from clint.textui import puts, colored

response = requests.get('https://api.github.com/users/octocat')
data = response.json()

puts(colored.green(data['name']))
puts(colored.red(data['location']))

# run using python3 tst1_clint_013124_v01.py
# shows the name and location of the user in color
