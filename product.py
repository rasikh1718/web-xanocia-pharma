#!C:\Users\lenovo\AppData\Local\Programs\Python\Python39\python
import cgi
import pymysql

print("content-type:text/html")
print()
# print('ok')
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<link rel='stylesheet' href='product.css'>")
print("<div class='container'><br><br>")

form=cgi.FieldStorage()
tablet=form.getvalue("tablet")


print("<h2 class='display-5'>Xanocia's  "+tablet+" Product range </h2>")
print("<hr>")

con=pymysql.connect(host='bsdd0rpqqz9qvrkzcnhr-mysql.services.clever-cloud.com',user='uyu0gdfgiasqmkeq',passwd='12RKXpmWmMEOS2cDWJA5',database='bsdd0rpqqz9qvrkzcnhr')
curs=con.cursor()
curs.execute("select * from tablet")
# data=curs.fetchall()
# print(data)rec=curs.fetchone()
data=curs.fetchall()
# while data:
#     print(data)
#     data=curs.fetchone()


print("<ul>")
for rec in data:
    print("<li>"+rec[1]+"&nbsp;&nbsp;&nbsp;&nbsp;"+rec[2]+"&nbsp;&nbsp;&nbsp;&nbsp;-------&nbsp;&nbsp;&nbsp;&emsp;&emsp;"+rec[3])
    

print("</ul>")
print("<br><a class='btn-info' href='index.html'>Home</a>")
con.close()
print('success')