from django.http import JsonResponse, HttpResponse
import mysql.connector

mydb = mysql.connector.connect(
    host="eu-cdbr-west-02.cleardb.net",
    user="bbd8d02721070b",
    password="8b0cd746",
    database="heroku_d2d55dc4dd51c32"
)

mycursor = mydb.cursor()
keys = ('customerName', 'contactLastName', 'contactFirstName', 'lastOrderDate', 'numOrders', 'Agency', 'phone',
        'addressLine', 'city', 'country')


def get_data(where='', having=''):
    mycursor.execute(f"""SELECT cus.customerNumber ,cus.customerName, cus.contactLastName, cus.contactFirstName,
    MAX(ord.orderDate) AS lastOrderDate, COUNT(ord.orderNumber) AS numOrders,  off.city AS Agency, cus.phone,
    cus.addressLine1, cus.city, cus.country
    FROM customers AS cus JOIN orders AS ord JOIN employees AS emp JOIN offices AS off
    WHERE ord.customerNumber = cus.customerNumber AND emp.employeeNumber = cus.salesRepEmployeeNumber AND
    emp.officeCode = off.officeCode {where}
    GROUP BY ord.customerNumber {having};""")

    myresult = mycursor.fetchall()

    mycursor.execute("SELECT distinct city FROM offices;")
    myagen = mycursor.fetchall()

    myagen = tuple(x[0] for x in myagen)

    data = {'agencies': myagen, 'customers': dict()}
    for x in myresult:
        data['customers'][x[0]] = dict(zip(keys, x[1:]))
    try:
        return JsonResponse(data)
    except:
        return HttpResponse("<h1>Hello World</h1>")


# Create your views here.
def myapi(request):
    return get_data()


def myapi_agen(request, agen):
    where = f"AND off.city = '{agen}'"
    return get_data(where=where)


def myapi_date(request, year, month, day):
    having = f"HAVING MAX(ord.orderDate) >= '{year}-{month}-{day}'"
    return get_data(having=having)


def myapi_date_agen(request, year, month, day, agen):
    having = f"HAVING MAX(ord.orderDate) >= '{year}-{month}-{day}'"
    where = f"AND off.city = '{agen}'"
    return get_data(where=where, having=having)
