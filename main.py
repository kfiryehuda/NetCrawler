import requests
import lxml.etree
import lxml.html

p1 = "//p/a[not(preceding::a/. = .)]/@href[starts-with(.,'/wiki/') and contains(.,'_') and not(contains(.,':')) and not(contains(.,'(')) and not(contains(.,'#')) and not(contains(.,'.')) and not(contains(substring-after(., '_'), '_'))]"
p2 = "//p/a[not(preceding::a/. = .)]/@href[starts-with(.,'/wiki/') " \
     "and contains(.,'_') and not(contains(.,':')) and not(contains(.,',')) and not(contains(.,'#')) and not(contains(.,'.'))" \
     "and not(contains(substring-after(., '_'), '_')) and contains('ABCDEFGHIJKLMNOPQRSTUVWXYZ', substring(substring-after(., '_'), 1, 1))" \
     "and not(contains(., 'International')) " \
     "and not(contains(., 'medal')) " \
     "and not(contains(., 'Cup')) " \
     "and not(contains(., 'Fighter')) " \
     "and not(contains(., 'language')) " \
     "and not(contains(., 'Open')) " \
     "and not(contains(., 'merica')) and not(contains(., 'Africa')) and not(contains(., 'Asia')) and not(contains(., 'Antarctica')) and not(contains(., 'Europe')) and not(contains(., 'Australia'))" \
     "and not(contains(., 'Strings')) " \
     "and not(contains(., 'Serve')) " \
     "and not(contains(., 'Nike')) " \
     "and not(contains(., 'Inc.')) " \
     "and not(contains(., 'Masters')) " \
     "and not(contains(., 'Skyhook')) " \
     "and not(contains(., 'Ball')) " \
     "and not(contains(., 'Sports')) " \
     "and not(contains(., 'Bagel')) " \
     "and not(contains(., 'Indoors')) " \
     "and not(contains(., 'Finals')) " \
     "and not(contains(., 'Championships')) " \
     "and not(contains(., 'Smash')) " \
     "and not(contains(., 'brand')) " \
     "and not(contains(., 'Tweener')) " \
     "and not(contains(., 'Award')) " \
     "and not(contains(., 'Academy')) " \
     "and not(contains(., 'ATP')) and not(contains(., 'niversity'))  and not(contains(., 'Classic'))  and not(contains(., 'Rankings')) and not(contains(., 'States'))]"

path_1 = "/html/body//table/tbody/tr[1]/th[5][contains(text(), 'Opponent') or contains(text(), 'Partner')]/../../tr/td[position()=5]/a[string-length(@href)<35]/@href[starts-with(.,'/wiki/')]"
path_2 = "/html/body//table/tbody/tr[1]/th[6][contains(text(), 'Opponent') or contains(text(), 'Partner')]/../../tr/td[position()=6]/a[string-length(@href)<35]/@href[starts-with(.,'/wiki/')]"
path_3 = "/html/body//table/tbody/tr[1]/th[7][contains(text(), 'Opponent') or contains(text(), 'Partner')]/../../tr/td[position()=7]/a[string-length(@href)<35]/@href[starts-with(.,'/wiki/')]"

def main():
    # page = requests.get("https://en.wikipedia.org/wiki/Roger_Federer")
    page = requests.get("https://en.wikipedia.org/wiki/Rafael_Nadal")
    # page = requests.get("https://en.wikipedia.org/wiki/Andy_Ram")
    doc = lxml.html.fromstring(page.content)
    urls = doc.xpath(p2)
    for url in urls:
        print('https://en.wikipedia.org' +url)
    print(len(urls))


if __name__ == '__main__':
    main()

