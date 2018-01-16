def file_accessible(filepath, mode):
    ''' Check if a file exists and is accessible. '''
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False
 
    return True
if __name__ = '__main__':
	file_accesible(xyz,'r')
