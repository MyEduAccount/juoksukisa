#-*- coding: UTF8 -*-

import importlib

class createclassinstance:
    def __init__(self, initbal=0):
        self.balance = initbal
            
    def hello(self):
        print(" hello from ",str(type(self))[8:-2])
                
    def create_instance(self,class_str:str):
        """
        Create a class instance from a full path to a class constructor
        :param class_str: module name plus '.' plus class name and optional parens with arguments for the class's
            __init__() method. For example, "a.b.ClassB.ClassB('World')"
        :return: an instance of the class specified.
        """
        try:
            if "(" in class_str:
                full_class_name, args = class_name = class_str.rsplit('(', 1)
                args = '(' + args
            else:
                full_class_name = class_str
                args = ()
            # Get the class object
            module_path, _, class_name = full_class_name.rpartition('.')
            mod = importlib.import_module(module_path)
            klazz = getattr(mod, class_name)
            # Alias the the class so its constructor can be called, see the following link.
            # See https://www.programiz.com/python-programming/methods/built-in/eval
            alias = class_name + "Alias"
            instance = eval(alias + args, { alias: klazz})
            
            return instance
        
        except (ImportError, AttributeError) as e:
            raise ImportError(class_str)


if __name__ == "__main__":
    #instance = create_instance()
    inst = createclassinstance()
    inst.hello()
