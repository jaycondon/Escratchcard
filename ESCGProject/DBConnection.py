import mysql.connector
#from mysql.connector import errorcode

#try:
# cnx = mysql.connector.connect(user='scott',
#                               database='testt')
##except mysql.connector.Error as err:
#  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#    print("Something is wrong with your user name or password")
#  elif err.errno == errorcode.ER_BAD_DB_ERROR:
#    print("Database does not exist")
#  else:
#    print(err)
#else:
#  cnx.close()

class UseDatabase:
    def __init__(self, configuration):
        """ Initialisation code which executes the context manager
            is CREATED. """
        self.host = configuration['DB_HOST']
        self.user = configuration['DB_USER']
        self.passwd = configuration['DB_PASSWD']
        self.db = configuration['DB']

    def __enter__(self):
        """ Set-up code which executes BEFORE the body of the 
            with statement. """
        self.conn = mysql.connector.connect(host=self.host,
                                            user=self.user,
                                            password=self.passwd,
                                            database=self.db,)
        self.cursor = self.conn.cursor()
        return(self.cursor)

    def __exit__(self, exc_type, exv_value, exc_traceback):
        """ Tear-down code with executes AFTER the body of the
            with statement.
            The three extra parameters to __exit__() contain information
            related to any exception which may have occurred while running
            the body of the with statement. """
        self.cursor.close()
        self.conn.commit()
        self.conn.close()


