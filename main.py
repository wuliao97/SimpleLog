import src


obj = src.PySimpleLog()

obj.println("aaa")
obj.println("Error", mode=obj.E)

new = src.PySimpleLog(color=src.Color.C)

new.println("test")