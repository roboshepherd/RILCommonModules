import time
DATA_SEP = ";"
FILE_EXT = ".txt"

class DataCtx:
    def __init__(self, name,  label, desc, sep = DATA_SEP):
        self.name = name
        self.label = label
        self.desc = desc
        self.sep = sep

class DataWriter:
    def __init__(self, obj_type, data_ctx, time_stamp, obj_id="", ext=\
        FILE_EXT):
        # init data file
        self.fn = obj_type + obj_id + "-"+  data_ctx.name + "-" +\
         str(time_stamp) + ext
        f = open(self.fn, 'w')
        header = "##" + data_ctx.sep + "##\n"
        header += "@" + data_ctx.name + ": " + data_ctx.desc + "\n" 
        header +=  data_ctx.label
        f.write(header)
        f.close()
    
    def AppendData(self, data):
        f = open(self.fn, 'a')
        f.write(data)
        f.close()
    
    def AppendComment(self, comment):
        f = open(self.fn, 'a')
        c = "#" + comment
        f.write(c)
        f.close()
        

