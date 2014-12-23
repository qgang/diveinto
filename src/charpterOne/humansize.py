from _ast import keyword
SUFFIXES = {1000:['KB','MB','GB','TB','PB','EB','ZB','YB'],
            1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.
    
    keyword argument:
    size -- file size in bytes
    '''