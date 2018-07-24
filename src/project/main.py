from keystoneauth1.identity import v3
from keystoneclient.v3 import client
from keystoneauth1 import session
from opslib.lib import opsbase
import openstack
openstack.enable_logging(debug=True)


def main():
    auth = v3.Password(
        auth_url='http://172.16.4.200:5000/v3/',
        user_id='659edb24617f4ca785f35dcb9d926f2b',
        password='Welcome123',
        project_id='91e4db1098934a3e9cc7babf97edf007',
        project_domain_name='default',
        user_domain_name='default'
    )

    sess = session.Session(auth=auth)
    sess.get('http://172.16.4.200:5000/v3/',
                    authenticated=True)
    keystone = client.Client(session=sess)
    print(type(sess))
    print(type(keystone))
    print(keystone.users.list())

    conn = openstack.connect(
        auth_url='http://172.16.4.200:5000/v3/',
        session = sess,
        identity_api_version='3',
        region_name='RegionOne',
        compute_api_version='2',
        identity_interface='internal'
    )
    for image in conn.image.images():            
        print(image)
                
if __name__ == '__main__':
    main()    