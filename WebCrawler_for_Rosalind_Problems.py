from bs4 import BeautifulSoup
import requests, sys, os
'''
Download all the questions from Rosalind website
'''
class downloader(object):
    '''
    Initialzation: change self.target when downloading other topics rather than bioinformatics textbook track
    '''
    def __init__(self):
        self.server = "http://rosalind.info"
        self.target = 'http://rosalind.info/problems/list-view/?location=bioinformatics-textbook-track'
        self.names = []
        self.ulrs = []
        self.nums = 0
    
    '''
    Get name and url link for each problem, as well as the total number of problems
    '''
    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        #print bf
        tables = bf.find_all('table', class_="problem-list table table-striped table-bordered table-condensed")
        a_bf = BeautifulSoup(str(tables[0]), "lxml")
        list_of_problems = a_bf.find_all('a')
        for each_idx in range(0, len(list_of_problems), 2):
            each = list_of_problems[each_idx]
            ulrs_link = str(self.server + each.get('href'))
            self.ulrs.append(ulrs_link)
            self.names.append(ulrs_link.split("/")[-2])
            self.nums += 1
    '''
    Parse the content of each problem and return as a text string
    '''
            
    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, "lxml")
        texts = bf.find_all('div', class_="problem-statement problem-statement-bordered")
        only_texts = texts[0].text
        
        textlines = str(only_texts).replace('$', '').rstrip().split("\n")
        end_flag = False
        start_idx = 1
        end_idx = len(textlines)
        for i in range(len(textlines)):
            if "Problem" in textlines[i]:
                start_idx = i
            if textlines[i] == "Sample Output":
                end_flag = True
            if end_flag and textlines[i]=='':
                end_idx = i #in python if end_idx is i, the string will end at position i-1
                break
           
        return "\n".join(textlines[1:end_idx])
    '''
    write the content into a txt file under a given path
    '''
    
    def write(self, path, text):
        write_flag = True
        with open(path, 'a') as f:
            f.write(text)
        f.close()
        
if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    dl = downloader()
    dl.get_download_url()
    print "Start Downloading: Rosalind Bioinformatics Textbook Tracks"
    for i in range(dl.nums):
        fname = dl.names[i].upper()+'.txt'
        os.mkdir(dl.names[i].upper())
        path = './'+dl.names[i].upper()+'/' + fname
        dl.write(path, dl.get_contents(dl.ulrs[i]).rstrip())
        sys.stdout.write("\n Now writing %s\n" % fname)
        sys.stdout.write("\n Finished %.2f%%" % (float(i)/dl.nums*100) + '\r\n')
        sys.stdout.flush()
    print ("\n Finished 100%!")
