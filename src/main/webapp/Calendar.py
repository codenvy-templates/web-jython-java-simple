from javax.servlet.http import HttpServlet


class Calendar(HttpServlet):
    def doGet(self, request, response):
        response.setContentType("text/html")
        out = response.getWriter()

        out.println("""
    <html>
      <head>
        <title>Hello World</title>
      </head>
      <body>
        <h1>Python servlet!</h1>
        <pre>Servlet path: %s</pre>
      </body>
    </html>
    """ % request.getServletPath())