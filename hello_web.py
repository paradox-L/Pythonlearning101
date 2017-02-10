import web

render = web.template.render('templates/')

urls = (
    #A website is like 'http://webpy.org/docs/0.3/tutorial'
    # '/'is a regular expression or text rule if you like,means find all str like '/blabla'(url)
    #The( ) mean capture that piece of the matched data for use later on
    #index is a class(just like a function here) we'll define later,to recieve our request(like GET and POST)and handle url
    '/(.*)', 'index'
)

class index:
    #GET is used to get a page,POST is to hand in form
    def GET(self,name):
        #This GET function will get called when someone makes a GET request for /.->return "Hello World"
        #index is a name of one of the templates
        #name means put in the arg
        print render.index(name)

#tell web.py to start a web page
if __name__ == "__main__":
    #First we tell web.py to create an application with the urls,and search corresponding class in the global namespace of this file
    app = web.application(urls, globals())
    app.run()