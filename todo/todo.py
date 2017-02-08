import web

db = web.database(dbn = 'sqlite', db = 'TODO.db')
render = web.template.render('templates/', cache = False)

def get_by_id(item_id):
    theitem = db.select('todoitem', where='id==$item_id', vars=locals())
    if not theitem:
        return False
    return theitem[0]

urls = (
    '/', 'Index',
    '/item/(\d+)', 'MyItem',
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

class MyItem:
    def GET(self, item_id):
        todo = get_by_id(item_id)
        if not todo:
            return render.error('Not Found')
        return render.item(todo)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()