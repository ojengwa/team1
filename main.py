import urllib2
from BeautifulSoup import BeautifulSoup
from urlparse import urljoin
from urlparse import urlparse
import re
from tree import Tree


def analyse_web(root,max_depth):
    #get root domain
    
    
    #crawl
    tree = Tree()
    page1, stat= get_page(root)
    external = get_external(root)
    crawled = {}
    tree.add_node(stat.encode('utf8'))
    print "**root**"
    print stat
    for check in external:
        if check != "":
            domain = get_domain(check)
        else:
            continue

        filter_domain = [domain]
        #set domain and depth
        tocrawl = [[check,1]]
        
        count=0;
        child = stat





  # root node


        while tocrawl: 
            crawl_ele = tocrawl.pop()
            link = crawl_ele[0]
            depth = crawl_ele[1]
            
            if link not in crawled.keys():
                content, title = get_page(link)
                
                if content == None:
                    #link = link.encode('latin-1')
                    #title = title.encode('latin-1')
                    crawled[link]= title
                    tree.add_node(title.encode('utf8'), child.encode('utf8'))
                    print "**child**"
                    print "top: "+title, "child: "+child
                    child = title
                    continue
                host = get_domain(link)
                
                
                if depth < max_depth and host in filter_domain :

                    outlinks = get_all_links(content,link)
                    
                   
                    add_to_tocrawl(crawled.keys(),tocrawl, outlinks, depth+1)
                
                crawled[link]= title
                tree.add_node(title.encode('utf8'), child.encode('utf8'))
                print "**child2**"
                print "top: "+title, "child: "+child
                
        """f = open('site_health.txt', 'w')
        for url,status in crawled.iteritems():
            f.write(url)
            f.write('\t')
            f.write('\t')
            f.write(status)
            f.write('\n')
        f.close()"""
    tree.display(stat)

def get_external(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
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
    #print url
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
    
def get_next_target(page,parent):
    
    page.findAll('a')
    page.get('href')
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    url = urljoin(parent,url)
    return url, end_quote

def get_all_links(page,parent):
    return [l.get('href') for l in page.findAll('a') ]
    


def add_to_tocrawl(crawled, tocrawl, newlinks, depth):
    for link in newlinks:
        if link not in tocrawl and link not in crawled:
            tocrawl.append([link,depth])


analyse_web('http://andela.co',2)
