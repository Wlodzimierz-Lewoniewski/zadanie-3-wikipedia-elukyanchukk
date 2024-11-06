from __future__ import unicode_literals
import urllib.parse
import urllib.request
import re

category=input()

category=category.strip()
category = category.strip()
encoded_category = urllib.parse.quote(category.replace(" ", "_"))
url = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Kategoria:" + encoded_category)
print("URL:", "https://pl.wikipedia.org/wiki/Kategoria:" + encoded_category)
mybytes = url.read()

html_content = mybytes.decode("utf8")
url.close()

pattern = r'<li><a\s+href="\/wiki\/[^"]+"\s+title="[^"]+">[^<]+<\/a>'

matches = re.findall(pattern, html_content)

# Get the first two matches
art1 = matches[0]
art2 = matches[1]

pattern_url = r'href="(.*?)"'


url_art1 = "https://pl.wikipedia.org/" + re.findall(pattern_url, art1)[0]
url_art2 = "https://pl.wikipedia.org/" + re.findall(pattern_url, art2)[0]

art1_urlopen = urllib.request.urlopen(url_art1)
art2_urlopen = urllib.request.urlopen(url_art2)

bytes_art1 = art1_urlopen.read()
bytes_art2 = art2_urlopen.read()

html_content_art1 = bytes_art1.decode("utf8")
html_content_art2 = bytes_art2.decode("utf8")

art1_urlopen.close()
art2_urlopen.close()

print(url_art1, url_art2)

# Linki wewnętrzne - art1

internal_links_1 = []

for link in re.findall(r'href="(\/wiki\/[^":#]*)"', html_content_art1):
    if re.findall(r'href="(\/wiki\/[^":#]*)"', html_content_art1):
        if (":" in link) or ("https://pl.wikipedia.org/"+link == url_art1) or (link == '/wiki/Ziemia'): 
            continue

        internal_links_1.append(urllib.parse.unquote(link).replace("_", " ").replace("/wiki/", ''))

        if len(internal_links_1) >= 5: 
            break

    else: 
        print("")

print(" | ".join(internal_links_1))

# Asresy URL do obrazków - art1

images_1 = []

for link in re.findall(r"src=[\"']?(//[^\"'\s]+?\.(?:jpg|png)(?:\/[^\"'\s]+)?)[\"']?", html_content_art1):
    if re.findall(r"src=[\"']?(//[^\"'\s]+?\.(?:jpg|png)(?:\/[^\"'\s]+)?)[\"']?", html_content_art1): 
        if link == '//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Geographylogo.svg/20px-Geographylogo.svg.png':
            continue

        images_1.append(urllib.parse.unquote(link))

        if len(images_1) >= 3: 
            break
    
    else: 
        print("")

print(" | ".join(images_1))

# Linki zewnętrzne - art 1

external_links_html = re.search(r'<div class="mw-references-wrap.*?</div>', html_content_art1, re.DOTALL)

if external_links_html: 

    start, end = external_links_html.span()
    html_references = html_content_art1[start:end]

    external_links_1 = []

    for link in re.findall(r'href="(http[s]?://[^"]+)"', html_references): 
        if re.findall(r'href="(http[s]?://[^"]+)"', html_references):
            external_links_1.append(urllib.parse.unquote(link))

            if len(external_links_1) >= 3: 
                break

        else:
            print("")

    print(" | ".join(external_links_1))

else: 
    print("")

# Kategorie - art 1

categories_html = re.search(r'<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks">.*?</div></div>', html_content_art1, re.DOTALL)

if categories_html:
    start, end = categories_html.span()
    html_references = html_content_art1[start:end]

    categories_1 = []

    for link in re.findall(r'title="Kategoria:([^"]+)"', html_references): 
        if re.findall(r'title="Kategoria:([^"]+)"', html_references):
            categories_1.append(urllib.parse.unquote(link))

            if len(categories_1) >= 3: 
                break

        else:
            print("")

    print(" | ".join(categories_1))

else: 
    print("")

# Linki wewnętrzne - art2

internal_links_2 = []

for link in re.findall(r'href="(\/wiki\/[^":#]*)"', html_content_art2):
    if re.findall(r'href="(\/wiki\/[^":#]*)"', html_content_art2):
        if (":" in link) or ("https://pl.wikipedia.org/"+link == url_art2) or (link == '/wiki/Ziemia'): 
            continue

        internal_links_2.append(urllib.parse.unquote(link).replace("_", " ").replace("/wiki/", ''))

        if len(internal_links_2) >= 5: 
            break
    
    else: 
        print("")

print(" | ".join(internal_links_2))

# Adresy URL do obrazków - art2

images_2 = []

for link in re.findall(r"src=[\"']?(//[^\"'\s]+?\.(?:jpg|png)(?:\/[^\"'\s]+)?)[\"']?", html_content_art2):
    if re.findall(r"src=[\"']?(//[^\"'\s]+?\.(?:jpg|png)(?:\/[^\"'\s]+)?)[\"']?", html_content_art2):
        if link == '//upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Geographylogo.svg/20px-Geographylogo.svg.png':
            continue

        images_2.append(urllib.parse.unquote(link))

        if len(images_2) >= 3: 
            break

    else:
        print("")

print(" | ".join(images_2))

# Linki zewnętrzne - art 2

external_links_html = re.search(r'<div class="mw-references-wrap.*?</div>', html_content_art2, re.DOTALL)

if external_links_html:
    start, end = external_links_html.span()
    html_references = html_content_art2[start:end]

    external_links_2 = []

    for link in re.findall(r'href="(http[s]?://[^"]+)"', html_references): 
        if re.findall(r'href="(http[s]?://[^"]+)"', html_references):
            external_links_2.append(urllib.parse.unquote(link))

            if len(external_links_2) >= 3: 
                break

        else:
            print("")

    print(" | ".join(external_links_2))

else:
    print("")
# Kategorie - art 2

categories_html = re.search(r'<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks">.*?</div></div>', html_content_art2, re.DOTALL)

if categories_html:
    start, end = categories_html.span()
    html_references = html_content_art2[start:end]

    categories_2 = []

    for link in re.findall(r'title="Kategoria:([^"]+)"', html_references): 
        if re.findall(r'title="Kategoria:([^"]+)"', html_references):
            categories_2.append(urllib.parse.unquote(link))

            if len(categories_2) >= 3: 
                break

        else: 
            print("")

    print(" | ".join(categories_2))

else:
    print("")