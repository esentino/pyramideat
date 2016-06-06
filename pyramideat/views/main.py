from pyramid.view import view_config


@view_config(route_name='home', renderer='pyramideat:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pyramideat'}
