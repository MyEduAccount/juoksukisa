#-*- coding: UTF8 -*-
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
class dictionaries(metaclass=Singleton):
    def __init__(self):
        self.dict_items
        self.dict_competitors
        self.dict_competiton
        self.dict_distance
        self.dict_time
        self.dict_items2
           
    #
    def get_dict_items(self):
        self.dict_items = [
                
                {'first':'Mikko',   'last':'Meikäläinen','born':1940,'role':'guitar'},
                {'first':'Maija',   'last':'Meikäläinen','born':1942,'role':'bass'},
                {'first':'Mia',     'last':'Meikäläinen','born':1943,'role':'guitar'},
                {'first':'Matti',   'last':'Meikäläinen','born':1940,'role':'drums'},
                {'first':'Minna',   'last':'Meikäläinen','born':1926,'role':'producer'}
            ]
        
        return self.dict_items
    
    #id,name,kisa,matka,aika
    def get_dict_competitors(self):
        self.dict_competitors =  {
        
                "Mikko Meikäläinen"         : '0',
                "Maija Meikäläinen"         : '1',
                "Mia Meikäläinen"           : '2',
                "Matti Meikäläinen"         : '3',
                "Minna Meikäläinen"         : '4'  
                
            }
            
        return self.dict_competitors
    
    def get_dict_competitors(self):
        self.dict_competiton = dict_competiton = {
        
                "Meikäläisten jussinjuoksut"    : '2020-06-24',
                "Meikäläisten kevätjuoksut"     : '2020-04-24'  
                
            }
        
        return self.dict_competiton

    def get_dict_distance(self):
        self.dict_distance = {
        
                "Maastojuoksu"              : '3000m',
                "Katujuoksu"                : '10000m',
                "Ratajuoksu"                : '5000m'

            }
        
        return self.dict_distance

    def get_dict_time(self):
        self.dict_time = {
        
                ""         : '0',
                "Maija Meikäläinen"         : '1',
                "Mia Meikäläinen"           : '2',
                "Matti Meikäläinen"         : '3',
                "Minna Meikäläinen"         : '4'  
                
            }
        
        return self.dict_time  
    
    def get_dict_items2(self):
        self.dict_items2 = [
        
                {'first':'John', 'last':'Lennon','born':1940,'role':'guitar'},
                {'first':'Paul', 'last':'McCartney','born':1942,'role':'bass'},
                {'first':'George','last':'Harrison','born':1943,'role':'guitar'},
                {'first':'Ringo','last':'Starr','born':1940,'role':'drums'},
                {'first':'George','last':'Martin','born':1926,'role':'producer'}
            ]
        
        return self.dict_items2