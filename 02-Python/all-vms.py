#!/usr/bin/env python
import os
from keystoneauth1.identity import v3
from keystoneauth1 import session
import novaclient.client

os_auth_url =  os.environ.get('OS_AUTH_URL')
os_tenant_id = os.environ.get('OS_TENANT_ID')
os_tenant_name = os.environ.get('OS_TENANT_NAME')
os_username = os.environ.get('OS_USERNAME')
os_password = os.environ.get('OS_PASSWORD')
os_domain_id = os.environ.get('OS_USER_DOMAIN_ID')

auth = v3.Password(auth_url=os_auth_url, 
                 username=os_username, 
                password=os_password, 
                project_name=os_tenant_name,
                project_domain_name="pipeline",
                user_domain_id=os_domain_id )
sess = session.Session(auth=auth)
novac = novaclient.client.Client(2, session=sess)
for server in novac.servers.list(search_opts={'all_tenants' : 1}):
    print server.id, server.name, server.status
