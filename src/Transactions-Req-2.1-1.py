import mysql.connector as mariadb

print("This program outputs credit card transactions for customers by zipcode \nfor a given month and a year in descending order by the day of the month.")

# Setup database connection.
dbConnection = mariadb.connect(host="localhost",user="root",password="password",database="creditcard_capstone")

cursor = dbConnection.cursor()

# Get transactions for customers by zipcode for a given month and a year
# in descending order by days of the month.
def GetTransactionsForCustomersByZipCodeAndDate(zipcode, month, year):

    sqlStatement = "SELECT tran.* FROM cdw_sapp_credit_card tran \
        INNER JOIN cdw_sapp_customer cust \
            ON cust.SSN = tran.CUST_SSN \
        WHERE cust.CUST_ZIP = '{}' \
            AND MONTH(STR_TO_DATE(tran.TIMEID, '%Y%m%d')) = {} \
            AND YEAR(STR_TO_DATE(tran.TIMEID, '%Y%m%d')) = {} \
        ORDER BY DAY(STR_TO_DATE(tran.TIMEID, '%Y%m%d')) DESC"

    cursor.execute(sqlStatement.format(zipcode, month, year))

    result = cursor.fetchall()
    print(result)

# Get user input.
zipcode = input("Enter a zipcode: ")
year = input("Enter the year for which you would like the transaction records: ")
month = input("Enter the month for which you would like the transaction records in a numberic format (1-12):")

GetTransactionsForCustomersByZipCodeAndDate(zipcode, month, year)