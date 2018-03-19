import redis


def make_conn():
    properties = get_properties()
    host = properties[0]
    port = properties[1]
    db = properties[2]
    r = redis.Redis(
    host=host,
    port=port, 
    db=db)
    return r

def get_properties():
    host='103.14.99.239'
    port='6379'
    db = '2'
    return host, port, db

def setup():
    cnx = make_conn()
    print('Connected')    
    #set_func(cnx)
    return 1

def set_func(cnx):
    #hashfunc = cnx.hget("LuaHashKeys:lua", "audience_search")
    

if __name__ == "__main__":
    setup()
    