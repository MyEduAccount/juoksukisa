#-*- coding: UTF8 -*-
#
# """https://pypi.org/project/list-dict-DB/"""
#
# LIST-DICT-DB
#
import json
from createanyclass import create_class_instance 
from dictionaries import dictionaries as cci
from list_dict_DB import list_dict_DB
#
# Singleton class creates dict_db class if no instancies are running 
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    #
#    
class dict_db(metaclass=Singleton):
    def __init__(self):
        pass
    
    # Nice to know one way to build dictionary filter with simple sql like (not sql) syntax 
    # like "select * from items where first = 'Matti'"  
    def get_words(self):
        #
        # Should be build dynamically to get tbl/item and column/item[]
        words = []
        words = [{'select' : 'item for item '},
                {'from' : 'in '},
                {'items' : 'items '},
                {'where' : 'if '}]
        
        return words
    
    # ToDo: maybe wise to do with pickle not json
    # text = 'Hello'
    # data=json.dumps(text) # to json
    # text=json.loads(data) # to text
    #       
    def json_dump(self,db_json):
        """[dump to file from DB]

        Args:
            db_json ([type]): [description]
        """
        with open(db_json,'w') as F:
            eval('json.dump(DB1.items(),F)')
    
    def json_load(self,db_json):
        """[load from file to DB]

        Args:
            db_json ([type]): [description]
        """
        with open(db_json,'r') as F:
            pass
            #DB = list_dict_DB(json.load(F))
    
    def __main__(self):
        """[class main function]
        """
        #print("****** to sql frame ********")
        #-----------------1st-way------------------------
        # 1st way is sql like fech of data 
        sql_string = "select * from items where role = 'guitar'"
        sql_clause = sql_string.split() # to list
        words = self.get_words()
        #print("Search with sql like string")
        search1 = self.sql_to_db_frame(sql_clause, words)
        print(search1)
        #-----------------2nd-way------------------------
        # 2nd way is search string fetch of data
        #print("Search with [] string")
        dict_name = 'items' # dictionary name
        query_string = "[item for item in items if item['role']=='guitar']" # Query to get data
        search2 = self.get_dictionary_data(query_string,dict_name)
        print(search2)

    #
    def get_dictionary_data(self,query_string,dict_name):
        #print('cci.get_dict_' + dict_name + '(cci)')
        items = eval('cci.get_dict_' + dict_name + '(cci)')
        #print(query_string)
        return eval(query_string)
    
    #
    # help function to create DataFrame search Strings
    def sql_to_db_frame(self,sql_clause:str,words:list):
        """[sql to db_frame string builder]

        Args:
            sql_clause (str): [description]
        """
        #
        items = cci.get_dict_items(cci)
        list_wheres = [] # list of where clause items like (column_pc = 'computer')
        rplc1="item['"
        rplc2="']"
        for index, elem in enumerate(sql_clause):
            if elem == '=': # check for equal(=) sign and left is key and right is value
                if (index+1 < len(sql_clause) and index - 1 >= 0):
                    prev_el = str(sql_clause[index-1]) # previous in list
                    prev_el = rplc1 + prev_el +rplc2 # concatenate to right form with brackets
                    curr_el = str(elem)+str(elem) # center or current in list (here is =)
                    next_el = str(sql_clause[index+1]) # next in list

                    wheres = prev_el + curr_el + next_el # current where clause 
                    list_wheres.append(wheres) # current where clause added to list
        #
        tmp_str = ""
        i=0
        for each_word in sql_clause:
            for word in words:
                if each_word.lower() == list(word.keys())[0].lower():
                    tmp_str = tmp_str + list(word.values())[0].lower()
                else:
                    pass
        list_wheres = "".join(list_wheres) # join list to string
        left="["
        right="]"
        search1 = eval(left + tmp_str + list_wheres + right)
        return search1
    #
    #
    # DB_1 = obj_list[0]
    # DB = list_dict_DB(items1) # Will index them all
    # Q = DB.Qobj() 
    """result_1 = DB_1.query( Q().last == 'Meikäläinen' )
    print(result_1)
    result_2 = DB_1.query( (DB_1.Q().first!='Minna') & (DB_1.Q().last == 'Meikäläinen'))
    print(result_2)
    result_3 = DB_1( ~( (Q.role=='guitar') | (Q.role=='drums'))) # negate with ~
    print(result_3)

    # Filter lookup if role quitar is true
    filt = lambda item: True if item['role'] == 'guitar' else False
    result_4 = eval("DB1.query(Q.filter(filt)")
    print(result_4)"""
    
    #Templates
    # search_1 = [item for item in items_x if item['First']=='Mikko' and item['Last']=='Meikäläinen']
    #           select * from    tbl  where first == George  and last == Harrison
    # print(search_1)

    # search_2 = [item for item in items_x if item['Last']=='Meikäläinen']
    #           select * from    tbl  where first == George  and last == Harrison
    # print(search_2)
    #dict_race = {"0": {'Mikko Meikäläinen':{'Kisa' : 'Meikäläisten juoksukisa'}}
    #litems = list()   
    #search_1 = [item for item in items2 if item['first']=='George' and item['last']=='Harrison']
    #           select * from    tbl  where first == George  and last == Harrison
    #print(search_1)
    
            
if __name__ == "__main__":
    #print("*******Start********")
    ddb = dict_db(list([])) # create dict_db runtime object
    # For safety reasons may be better to leave main out !!!
    # For testing it is helpfull
    ddb.__main__() # call dict_db main method
    #ddb.main()

 
 
 
    
    

