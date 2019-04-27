from query import Query
class UncachedQuery(Query):
    def exec_query(self,query_string):
        self.cursor.execute(query_string)
        rows = self.cursor.fetchall()
        return rows