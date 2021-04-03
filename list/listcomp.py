##  def a function in which we check the data type if the data type is int or float then we print this in string
# ex:['str','tyr','1','2.0','6.3'] = output is ['1','2.0','6.3']
# 
def list_string(l):
    return [str(i) for i in l if( type(i) == int  or type(i) == float)] 
print(list_string([True,False,3,6,9.0,6.3]))




