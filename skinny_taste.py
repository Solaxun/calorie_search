import requests
from lxml import html

response = requests.get('http://www.skinnytaste.com/recipes/page/1/')
page = html.fromstring(response.text)
ignore_links = ['vegetarian','quick','paleo','low-carb','gluten-free',
'freezer-friendly','slow-cooker','kid-friendly']
ignore_links = {'http://www.skinnytaste.com/recipes/'+endlink+'/' for endlink in ignore_links}

pages = [pg for pg in page.xpath('//div[@class="archives"]//a/@href')
    if pg not in ignore_links]

print(pages)
        
