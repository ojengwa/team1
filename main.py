import urllib2
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import re


def analyse_web(root,max_depth):
    if type(max_depth) == str:
        max_depth = int(max_depth)
    print "*** Fetching external links for "+root
    page1, stat= get_page(root)
    stat = re.sub("[!@#$']", '', stat.encode('utf8'))
    external = get_external(page1,root)
    crawled = {}
    crawldepth = {}
    crawled[stat]={'parent':'root'}
    print "*** "+`len(external)`+" link(s) found on "+root
    for check in external:
        if check != "":
            domain = get_domain(check)
        else:
            continue

        filter_domain = [domain]
        #set domain and depth
        tocrawl = [[check,1]]
        
        

        while tocrawl: 
            crawl_ele = tocrawl.pop()
            link = crawl_ele[0]
            depth = crawl_ele[1]


            
            
            if link not in crawled.keys():
                if link is not None and link != '#' and link != '/' and link != '?':
                    print "*** Fetching data from "+link
                content, title = get_page(link)
                title = re.sub("[!@#$']", '', title.encode('utf8'))
                

                if content == None:
                    
                    continue
                else:
                    crawldepth[depth]=title
                host = get_domain(link)
                
                
                if depth < max_depth and host in filter_domain :

                    outlinks = get_all_links(content,link)
                    print "*** "+`len(outlinks)`+" link(s) found on "+link
                   
                    add_to_tocrawl(crawled.keys(),tocrawl, outlinks, depth+1)
                
                

                if depth == 1:
                    crawled[title]={'parent':stat}
                else:
                    
                    crawled[title]={'parent':crawldepth[depth-1]}
                
                
       
    return crawled

def get_external(soup,url):
    
    return [l.get('href') for l in soup.findAll('a') if is_external(url,l.get('href'))]
    

def get_domain(url):
    
    hostname = urlparse(url).hostname
    
    if len(re.findall( r'[0-9]+(?:\.[0-9]+){3}', hostname)) > 0:
        return hostname
    elif len(hostname.split('.')) == 0:
        hostname
    elif hostname.find('www.') != -1:
        return hostname.split('.')[0]
    else:
        return hostname.split('.')[1]

def is_external(root,host):
    if len(host) > 0:

        if host[0] == '/' or host[0] == '#' or host[0] == '?':
            return False
    host = urlparse(host).hostname
    hostname = urlparse(root).hostname
    if host == None:
        return False
    return host != hostname and host.find(hostname) == -1
    
def get_page(url):
    try:
        response = urllib2.urlopen(url)
        soup = BeautifulSoup(response)
        
        return soup, soup.title.string
    except urllib2.HTTPError,e:
        return None, str(e.code)
    except urllib2.URLError,e:
        return None, 'Invalid Url'
    except:
        return None, 'Wrong Url'
    


def get_all_links(page,parent):
    return [l.get('href') for l in page.findAll('a') ]
    


def add_to_tocrawl(crawled, tocrawl, newlinks, depth):
    for link in newlinks:
        if link not in tocrawl and link not in crawled:
            tocrawl.append([link,depth])



