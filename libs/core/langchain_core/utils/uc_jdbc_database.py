from databricks import sql

class UCJDBCDatabase:
    """A wrapper around the Databricks JDBC connection."""
  
    def __init__(self, server_hostname, http_path, access_token, catalog, schema):
        self.server_hostname = server_hostname
        self.http_path       = http_path
        self.access_token    = access_token
        self.catalog         = catalog
        self.schema          = schema
    
    def __enter__(self):
        self.connection = sql.connect(server_hostname = self.server_hostname,
                                    http_path       = self.http_path,
                                    access_token    = self.access_token,
                                    catalog = self.catalog, 
                                    schema =  self.schema)
        return self.connection
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

    def connect(self):
        return self.__enter__()
    
    def execute(self, query):
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


