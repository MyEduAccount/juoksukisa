#-*- coding: UTF8 -*-
#
# """https://pypi.org/project/list-dict-DB/"""
#
# LIST-DICT-DB
#
import json
from createanyclass import createclassinstance as cci
from dictionaries import _dictionaries_
#
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
    def __init__(self, initbal=0):
        self.balance = initbal
       
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
        print("****** to sql frame ********")
        sql_string = """select * from items where role = 'guitar'"""
        sql_clause = sql_string.split()
        words = self.get_words()
        self.sql_to_db_frame(sql_clause, words)
        
    #
    # help function to create DataFrame search Strings
    def sql_to_db_frame(self,sql_clause:str,words:list):
        """[sql to db_frame string builder]

        Args:
            sql_clause (str): [description]
        """
        #
        list_wheres = []
        rpl1="item['"
        rpl2="']"
        left="["
        right="]"
        for index, elem in enumerate(sql_clause):
            if elem == '=':
                if (index+1 < len(sql_clause) and index - 1 >= 0):
                    #Check index bounds
                    prev_el = str(sql_clause[index-1])
                    prev_el = rpl1 + prev_el +rpl2
                    curr_el = str(elem)+str(elem)
                    next_el = str(sql_clause[index+1])

                    wheres = prev_el + curr_el + next_el
                    list_wheres.append(wheres)
        #
        print("sql_clause length : ",str(len(sql_clause)))
        print("words length : ",str(len(words)))
        tmp_str = ""
        i=0
        for each_word in sql_clause:
            for word in words:
                if each_word.lower() == list(word.keys())[0].lower():
                    print(each_word.lower(),' = ',list(word.keys())[0].lower())
                    tmp_str = tmp_str + list(word.values())[0].lower()
                else:
                    pass
        list_wheres = "".join(list_wheres) # to string
        #print(left + tmp_str + list_wheres + right)
        search1 = eval(left + tmp_str + list_wheres + right)
        #print(search1)
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
    print("*******Start********")
    ddb = dict_db(list([])) # create dict_db runtime object
    # For safety reasons may be better to leave main out !!!
    # For testing it is helpfull
    ddb.__main__() # call dict_db main method
    #ddb.main()

 
 
 
    
    

