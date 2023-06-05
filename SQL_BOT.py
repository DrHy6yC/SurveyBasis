import mysql.connector
from mysql.connector import Error


def get_keys_str(dict_atr):
    return_text = ""
    key = dict_atr.keys()
    for i in key:
        return_text += f"{str(i)}, "
    return return_text[:-2]


def get_values_str(dict_atr):
    return_text = ""
    key = dict_atr.values()
    for i in key:
        #print(type(i), type(i) == int)
        if type(i) == int:
            return_text += f"{i}, "
        else:
            return_text += f"'{i}', "
    return return_text[:-2]


def get_values_str_update(dict_atr):
    return_text = ""
    key = dict_atr.keys()
    for i in key:
        if type(i) == int:
            return_text += f"{i} = {dict_atr[i]}, "
        else:
            return_text += f"{i} = '{dict_atr[i]}', "
    return return_text[:-2]


def get_where(dict_where):
    return_text = ""
    if dict_where == dict():
        return return_text
    key = dict_where.keys()
    for i in key:
        if type(i) == int:
            return_text += f"and {i} = {dict_where[i]}"
        else:
            return_text += f"and {i} = '{dict_where[i]}'"
    return return_text


class SQL_BOT():
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="gfhjkzytn", database="BOT")
        self.cursor = self.conn.cursor()


    def end_con(self):
        self.cursor.close()
        self.conn.close()


    def SELECT_TABLE (self, table, dict_where=dict()):
        try:
            query = f"""
            SELECT * FROM {table}
            WHERE 1=1 {get_where(dict_where)};
            """
            result_list = list()
            print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for i in result:
                result_list.append(i)
            return result_list
        except Exception as error:
            print("SELECT_TABLE: ", error)


    def INSERT_TABLE(self, table, dict_atr):
        try:
            query = f"""
            INSERT INTO {table} ({get_keys_str(dict_atr)})
            VALUES({get_values_str(dict_atr)});
            """
            print(query)
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as error:
            print("INSERT_TABLE: ", error)


    def UPDATE_TABLE(self, table, dict_atr, dict_where=dict()):
        try:
            query = f"""
            UPDATE {table} SET {get_values_str_update(dict_atr)}
            WHERE 1=1 {get_where(dict_where)};"""
            print(query)
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as error:
            print("UPDATE_TABLE: ", error)


    def get_ONE_USER (self, USER_LOGIN):
        try:
            query = f"""
            SELECT * FROM USERS
            WHERE USER_LOGIN = '{USER_LOGIN}';
            """
            print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result
        except Exception as error:
            print("SELECT_TABLE: ", error)


if __name__ == '__main__':
    dict_test = {'USER_LEVEL': 3}
    dict_where = {"USER_LEVEL": 1}
    try:
        sql = SQL_BOT()
        sql.UPDATE_TABLE("USERS", dict_test, dict_where)
    except Exception as error:
        print(error)
    finally:
        sql.end_con()
