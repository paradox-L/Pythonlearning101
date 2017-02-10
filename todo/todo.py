import web
import datetime

db = web.database(dbn = 'sqlite', db = 'TODO.db')
render = web.template.render('templates/', cache = False)

def get_by_id(id):
    item = db.select('todoitem', where='id=$id', vars=locals())
    return list(item)[0] 

urls = (
    '/', 'Index',
    '/delete/(\d+)', 'DeleteItem',
    '/item/new', 'AddNew',
)

class Index:
    def GET(self):
        items = db.select('todoitem')
        count = db.query('SELECT COUNT(*) AS COUNT FROM todoitem')[0]['COUNT']
        return render.index(items, count)

    def POST(self):
        typein = web.input()
        condition = r'content like "%' + typein.keyword +r'%"'
        items = db.select('todoitem', where = condition)
        count = db.query('SELECT COUNT(*) AS COUNT FROM todoitem WHERE ' + condition)[0]['COUNT']
        return render.index(items, count)

class DeleteItem:
    def GET(self, id):
        item = get_by_id(id)
        if not item:
            return render.error('No Record in Database')
        return render.delete(item)
    def POST(self, id):
        db.delete('todoitem', where = 'id=$id', vars=locals())
        raise web.seeother('/')


class AddNew:
    form = web.form.Form(
        web.form.Textbox('content', web.form.notnull, description = "I'd love to: "),
        web.form.Button('Add item'),
    )

    def GET(self):
        form = self.form
        return render.new(form)

    def POST(self):
        form = self.form
        if not form.validates():
            return render.error('Please enter content.')
        db.insert('todoitem', content=form.d.content, itemdate=datetime.date.today())
        raise web.seeother('/')
  
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()