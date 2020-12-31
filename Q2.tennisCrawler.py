import requests
import lxml.html
import random
import time

WIKI_PREFIX = 'https://en.wikipedia.org'


def crawl_url(url, xpaths):
    time.sleep(3)
    urls = []
    try:
        res = requests.get(url)
        doc = lxml.html.fromstring(res.content)
    except:
        return urls
    # Results are also appended to a text file
    # XPath expression: seek links to https address (or at least that contain 'https')
    for xpath in xpaths:
        for crawled_url in doc.xpath(xpath):
            urls.append(WIKI_PREFIX + crawled_url)
    return urls


def get_random_unvisited_url(from_list, visited_list):
    temp_set = set(from_list.copy())
    for iterate in range(100000):
        if len(temp_set) == 0:
            return None
        rand_url = random.choice(list(temp_set))
        if not rand_url in visited_list:
            return rand_url
        else:
            temp_set.discard(rand_url)
    if len(temp_set) == 0:
        return None


def get_closest_to_first(crawled_urls, visited_urls, urls_distance_from_first):
    sorted_by_dist_urls = dict(sorted(urls_distance_from_first.items(), key=lambda item: item[1])).keys()
    for i in sorted_by_dist_urls:
        if i not in visited_urls:
            return i


def ingest_urls(url_set, src_url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls):
    for i in url_set:
        if i not in crawled_urls:
            crawled_urls.append(i)
            crawled_urls_src[i] = src_url
            urls_distance_from_first[i] = urls_distance_from_first[src_url] + 1
    visited_urls.append(src_url)


def tennisCrawler(url, xpaths):
    visited_urls = []
    crawled_urls = []
    crawled_urls_src = {}
    urls_distance_from_first = {url: 0}

    first_url_set = set(crawl_url(url, xpaths))
    ingest_urls(first_url_set, url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls)

    while len(visited_urls) < 10:
        # do 3 DFS
        # 1 DFS
        random_url = get_random_unvisited_url(crawled_urls, visited_urls)
        url_set = set(crawl_url(random_url, xpaths))
        ingest_urls(url_set, random_url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls)
        # 2 DFS
        random_url = get_random_unvisited_url(url_set, visited_urls)
        if random_url is not None:
            url_set_2 = set(crawl_url(random_url, xpaths))
        else:
            random_url = get_random_unvisited_url(crawled_urls, visited_urls)
            url_set_2 = set(crawl_url(random_url, xpaths))
        ingest_urls(url_set_2, random_url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls)
        # 3 DFS
        random_url = get_random_unvisited_url(url_set_2, visited_urls)
        if random_url is not None:
            url_set_3 = set(crawl_url(random_url, xpaths))
        else:
            random_url = get_random_unvisited_url(url_set, visited_urls)
            if random_url is not None:
                url_set_3 = set(crawl_url(random_url, xpaths))
            else:
                random_url = get_random_unvisited_url(crawled_urls, visited_urls)
                url_set_3 = set(crawl_url(random_url, xpaths))
        ingest_urls(url_set_3, random_url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls)

        # do 1 BFS
        closest_url = get_closest_to_first(crawled_urls, visited_urls, urls_distance_from_first)
        url_set = set(crawl_url(closest_url, xpaths))
        ingest_urls(url_set, closest_url, crawled_urls, crawled_urls_src, urls_distance_from_first, visited_urls)


    # print(visited_urls)
    ret = [[crawled_urls_src[e], e] for e in crawled_urls]
    return ret



import main
tennisCrawler("https://en.wikipedia.org/wiki/Roger_Federer", [main.p2])
# for i in tennisCrawler("https://en.wikipedia.org/wiki/Roger_Federer", [main.p2]):
#     print(i)









