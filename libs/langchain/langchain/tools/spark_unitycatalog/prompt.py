# flake8: noqa
QUERY_CHECKER = """
{query}
Double check the {dialect} query above for common mistakes, including:
- Using NOT IN with NULL values
- Using UNION when UNION ALL should have been used
- Using BETWEEN for exclusive ranges
- Data type mismatch in predicates
- Properly quoting identifiers
- Using the correct number of arguments for functions
- Casting to the correct data type
- Using the proper columns for joins

If there are any of the above mistakes, rewrite the query. If there are no mistakes, just reproduce the original query.

Output the final SQL query only.

SQL Query: """


SQL_QUERY_VALIDATOR = """
Act as a SQL Query Validator. Check if the columns in the generated sql_query matches with the columns with the schema of tables. 
Add limit 10 to the sql query if it not present and return the sql_query
The schema is passed as a key value pair where key is the table name and value is the schema of the table.
The sql_query is passed as a string.
If the check is passed return the sql_query and use sql_db_query tool to execute the query.
If the check is failed return an error message and ask the llm to generate correct sql query by using sql_db_schema tool.
Return only the updated sql query.
Return the response as The Final SQL Query is <sql_query>
The schema is {db_schema}.
The sql_query is {query}.
Begin SQL Query Validation.

"""


SQL_QUERY_CREATOR = """### Instructions:
Your task is convert a question into a SQL query, given a schema which is databricks sql compatible.
Adhere to these rules:
- **Deliberately go through the question and database schema word by word** to appropriately answer the question
- **Use Table Aliases** to prevent ambiguity. For example, `SELECT table1.col1, table2.col1 FROM table1 JOIN table2 ON table1.id = table2.id`.
- When creating a ratio, always cast the numerator as float
You are an AI research assistant in the senior living industry.
You have access to a database that contains the information about different communities, their amenities, residents, expenses, budget, revenue and other finances, facilities, beds, events
When querying the database, given an input question, create a syntactically correct query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 10 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

### Input:
Generate a SQL query that answers the question `{user_input}`.
This query will run on a database whose schema is represented in this string:
'{db_schema}'
Use the following examples to generate the sql query:
'{few_shot_examples}'
### Response:
Based on your instructions, here is the SQL query I have generated to answer '{user_input}'
```sql"""

