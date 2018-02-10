import os
import ipfsapi


try:
    filename = 'tmpfile'
    with open(filename, 'w') as fp:
        fp.write('hello world')
        api = ipfsapi.connect()
        resp = api.add(files=filename)
        print(resp)
except Exception as err:
    raise err
finally:
    os.remove(filename)

