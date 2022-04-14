# Sanare_CRM
<h2> Description</h2>

Project I did using pgAdmin, Flask, and Insomnia for Python backend web application that manages employees and refferal accounts.

<h2> Retrospective</h2>

<h3>How did the project's design evolve over time?</h3>
The project evolved mainly in the way of database relationships and API endpoints. I adjusted some of the relationships in order to be able to generate specific lists that would be useful to the company.
<h3>Did you choose to use an ORM or raw SQL? Why?</h3>
I chose ORM because the web app is mostly basic updates, creates, and deletes. I also chose ORM, because the application is built with a Python oop approach, so I wanted to use that approach when managing the database.
<h3>What future improvements are in store, if any?</h3>
In the future, I want to change the relationship of the contacts table and refferal_accounts table to many-to-many so I can query results that would help make business decisions for the company. I also want to implement some data visualization into the project to make it easier to understand the data and more effective. 

<h2>API Refference Table</h2>

| Endpoint Paths      | Methods | Parameters     |
| :---        |    :----:   |          :--- |
| {{ _.baseURL }}/employees      | GET       | N/A   |
| {{ _.baseURL }}/employees/{employee_id}   | Patch        | {employee_id}     |
| {{ _.baseURL }}/refferal-accounts    | GET       | N/A   |
| {{ _.baseURL }}/refferal-accounts  | Post        | {<br>"id": 101, "company_name": "testing",<br>"phone": "205-123-6543",<br>"email": "test.email",<br>"address": "103 test dr",<br>"city": "tester",<br>"state": "TE",<br>"zip_code": "65434",<br>"industry": "testing",<br>"employee_id": 10<br>}	|
| /refferal-accounts/{refferal_account_id}   | Delete       | {refferal_account_id}   |


