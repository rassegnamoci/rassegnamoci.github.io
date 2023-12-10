''' 
Generates ../movieslist.html from ../rawdata/movieslist.csv as downloaded,
using ../templates/movieslist_template.html 
'''

import pandas as pd
from jinja2 import Template

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../rawdata/movieslist.csv')
df = df[['Data proiezione', 'Film',	'Selezionatore', 'Tema', 'Anno', 'Regista/i', 'Durata',	'Paese/i di produzione', 'Link IMDb']]

# Sort by last movie
df.set_index(['Data proiezione'])
df = df.sort_index(ascending = False)

with open('../templates/movieslist_template.html','r') as f:
    template = f.read()

data = {'table': df.to_html(index = False, formatters={'Link IMDb': lambda x: '<a href="'+x+'" target="_blank">'+x+'</a>'}).replace('&lt;','<').replace('&gt;','>')}

j2_template = Template(template)

with open('../movieslist.html', 'w') as f:
    f.write(j2_template.render(data))

