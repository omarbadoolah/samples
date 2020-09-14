'''
Skeleton file to demonstrate how to create a web server
using aiohttp on Python
'''

from aiohttp import web

# Initialize routes
routes = web.RouteTableDef()


# GET /
# Note the @routes annotations map the function to the route
@routes.get('/')
async def index(request):
    return web.Response(text="text", content_type='text/html')

# POST /files
@routes.post('/files')
async def upload(request):
    body = await request.post()
    upload = body.get("input_name")
    # Redirect after the post
    raise web.HTTPFound(location='/pending')

# GET /pending
@routes.get('/pending')
async def getPending(request):
    return web.Response(content_type='text/html', text="pending page")


def start():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)

'''
<html>

<head>

<title>Finance</title>

</head>

<! CSS styling for current page />
<style> 
    body { font-family:"Courier New" } 
    table { text-align:right} 
</style>

<body>

<! HTML form with file upload input />

<form enctype = "multipart/form-data" action="files" method="post">
    Filename: 
    <input type = "file" name = "input_name" accept=".csv,.CSV" >
    <input type = "submit" value = "Upload">
</form>

<a href="/">Home</a/>

</body>

</html>