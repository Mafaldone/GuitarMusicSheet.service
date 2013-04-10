import web2py


@request.restful()
def api():
    response.view = 'generic.'+request.extension
    def GET(*args,**vars):
        patterns = [
            "/sheet[author]",
            "/sheet/{author.name.startswith}",
            "/sheet/{author.name}/:field",
            "/sheet/{author.name}/pets[pet.owner]",
            "/sheet/{person.name}/pet[pet.owner]/{pet.name}",
            "/sheet/{person.name}/pet[pet.owner]/{pet.name}/:field"
            ]
        parser = db.parse_as_rest(patterns,args,vars)
        if parser.status == 200:
            return dict(content=parser.response)
        else:
            raise HTTP(parser.status,parser.error)
    def POST(table_name,**vars):
        if table_name == 'person':
            return db.person.validate_and_insert(**vars)
        elif table_name == 'pet':
            return db.pet.validate_and_insert(**vars)
        else:
            raise HTTP(400)
    return locals()