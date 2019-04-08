#!C:\Python27\python.exe

import cgi

def htmlTop():
    print("""Content-type:text/html\n\n
             <!DOCTYPE html>
             <html lang ="en">
                  <head>
                      <meta charset="utf-8"/>
                      <title>My Server-side template</title>
                  </head>
                  <body>""")  

def htmlTail():
    print("""</body>
            </html>""")

#main program
if __name__=="__main__":
    try:
        htmlTop()
        print("<h1>Hello World!!</h1>")
        htmlTail()
    except:
        cgi.print_exception()
          
