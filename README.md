# djangoMySQLproject

<p>This project has two parts: Back (API) and Front.</p>

<h2>BACK</h2>
<p>Api returns a list of customers.</p>

<p>localhost:8000/api/</p>
<p>returns all customers (customerName, contactLastName, customerFirstName, lastOrderDate, Number of Orders, Agency (responsible for the customer), ...)</p>

<p>localhost:8000/(year)/(month)/(day)/</p>
<p>returns all customers with a "last order date" after the date (year-month-day).</p>
<p>  (It is a small database so there are orders bewtween 2003 and 2005)</p>
  
<p>localhost:8000/(agency)/
<p>returns all customers related to the "agency".</p>
<p>  ("agencies": ["San Francisco", "Boston", "NYC", "Paris", "Tokyo", "Sydney", "London"])</p>
  
<p>localhost:8000/(year)/(month)/(day)/(agency)/<p>
<p>returns all customers with a "last order date" after the date (year-month-day) and related to the "agency".</p>
  
<p>Api returns json format, where first element is a list of agencies and second is a list of customers.</p>
  

<h2>FRONT</h2>
<p>Two filters (agency, date).</p>
<p>Customers table.</p>
<p>Pagination.</p>


<h2>DATABASE</h2>
Datas are taken from remote database. Unfortunately it is NOT stable.
