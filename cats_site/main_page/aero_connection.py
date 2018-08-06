# import the module
from __future__ import print_function
import aerospike
import random

def open_aero():
    # Configure the client
    config = {
    'hosts': [ ('*.*.*.*', 3000) ]
    }

    # Create a client and connect it to the cluster
    try:
        client = aerospike.client(config).connect()
    except:
        import sys
        print("failed to connect to the cluster with", config['hosts'])
        sys.exit(1)
    return client

def add_user(ip_adress, aero_client):
    # Records are addressable via a tuple of (namespace, set, key)
    key = ('catssite', 'users', ip_adress)
    meta = {'ttl': 60}
    rand_seed = random.randint(1, 10000000)
    
    try:
        # Write a record
        aero_client.put(key, {
            'seed': rand_seed
        }, meta)
        print(str(ip_adress) + " " + str(rand_seed) + " is added.")
    except Exception as e:
        import sys
        print("error: {0}".format(e), file=sys.stderr)
    return rand_seed

def check_user_seed(ip_adress, aero_client):
    # Key of the record
    key = ('catssite', 'users', ip_adress)
    # Retrieve the record using the key.
    (key, meta) = aero_client.exists(('catssite', 'users', ip_adress))
    if ( meta is None ):
        return add_user(ip_adress, aero_client)
    else:
        (key, meta, bins) = aero_client.get(('catssite', 'users', ip_adress))
        return bins['seed']

def close_aero(aero_client):
    aero_client.close()
