import glob
from enum import Enum

import unidecode


class PageTranslator:
    class Token:
        def __init__(self, name, func):
            self.name = name
            self.func = func
        
        def parse(self,x):
            self.func(x)


    def __init__(self, 
                from_f: str, 
                to_f: str,
                extension: str = ""):
        self.from_f = from_f
        self.to_f = to_f
        self.extension = extension
        
        self.begin = "{% extends 'base.html' %}\n{% block content %}\n"
        self.end = "\n</div>\n{% endblock %}"
        
        self.header_imgpath = '<header class="masthead bg-primary text-white text-center mb-5 img-fluid responsive-bg-image" style="background-image:url({{{{url_for(\'static\',filename=\'{}\')}}}});" >'
        self.header_title = '<h1 class="text-uppercase mb-0 text-shadow">{}</h1>'
        self.header_subtitle = '<h2 class="font-weight-light mb-0 text-shadow">{}</h2>\n</header>\n<div class="text-dark mb-3">'
        
        self.topic_counter = 0
        self.sub_counter = 0
        self.topic_format = "{top}.{sub} - "

        self.isHeaderDone = False
        
        self.__hashdict =   {
                                "#subtitle": lambda x : self.header_subtitle.format(self.cleanToken(x)),
                                "#imgpath": lambda x : self.header_imgpath.format(self.cleanToken(x)),
                                "#title": lambda x : self.header_title.format(self.cleanToken(x)),
                                "#": self.__h,
                                "**_else_**": self._else,
                            }
        self.shouldEndSection = False

    def _else(self, x):
        if "<br>" in x:
            return '<p class="text-justify paragraph-block">{}</p><br>'.format(self.cleanToken(x))
        else:
            return '<p class="text-justify paragraph-block">{}</p>'.format(self.cleanToken(x))

    @property
    def topic_div(self):
        return self.topic_format.format(top=self.topic_counter, sub=self.sub_counter)

    def cleanToken(self, t): return t.strip(" #").replace("<br>","")

    def incrementTopic(self, count):
        newSubTopic = count == 1
        if newSubTopic :
            self.sub_counter = 0 # Make non sub_topic
            self.topic_counter += 1 # Increase main topic
        else: self.sub_counter += 1 

    def __h(self,z:str):
        count = z.count("#")
        z = self.cleanToken(z)
        if(count == 0): return ""
        self.incrementTopic(count)
        
        id_name = "".join( c for c in unidecode.unidecode(z.lower()) if c.isalpha() ) + "-t"
        #z = self.topic_div + z
        
        extra = ('<hr width="60%">\n</section>\n' * (self.sub_counter > 0 or self.topic_counter > 1 )) +('</div>\n' * (count == 1 and self.topic_counter > 1)) + ('<div class="text-body">\n' * (count == 1)) + \
        '<section style="margin: 20px {v_margin}%; padding: 5px 0px 0px {v_margin}%;">\n'.format(v_margin=(4 * count) - 4)
        
        isMainTopic = count == 1
        if isMainTopic:
            code = \
'''
<div class="d-flex  title-transition"  id="{id}">
    <h3 class="text-uppercase mr-auto">{}</h3>
    <a class="nav-link " data-toggle="modal" href="#exampleModal"><i class="material-icons">contact_mail</i></a>
</div>\n
'''.format(z,id=id_name)
        else:
            code = \
'''
<div class="subtitle-transition">
<h{c} class="text-uppercase" id="{id}">{}</h{c}>
</div>\n
'''.format(z,id=id_name,c=2 + count//2)
        h = extra + code

        self.shouldEndSection = True

        return h
        
    def __getLinks(self):
        to_glob = self.from_f + "*" + self.extension
        
        return glob.glob(to_glob)

    def __hash(self,z):
        for k,v in self.__hashdict.items():
            if z[:len(k)] == k: 
                if ( k == "#"):
                    return v(z)
                else:
                    return v(z[len(k):])
        return self.__hashdict["**_else_**"](z)

    def translate(self):
        files = self.__getLinks()
        for filename in files:
            ffname = filename.split("\\")[-1]
            with open(filename, "r") as f:
                print(f"Translating: {ffname}")
                try:
                    data = f.read().split('\n')
                except UnicodeDecodeError as e:
                    print(f"Error at file {filename} | from: {e.start} to: {e.end}")
                    raise e
                code = self.begin + "\n".join(self.__hash(l) for l in data if l) + ('<hr width="60%">\n</section>\n</div>\n' * self.shouldEndSection) + self.end
            to_path = self.to_f + ((ffname).split(".")[0] + ".html")
            
            with open(to_path, "w+") as f:
                f.write(code)
            self.topic_counter = 0
            self.sub_counter = 0
            self.shouldEndSection = False