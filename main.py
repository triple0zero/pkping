from fwork import ConfigFile

cf = ConfigFile()

print('config:', cf.config)
print('hosts:', cf.hosts)

h = cf.get_host_description('8.8.8.8')
print(f'for 8.8.8.8 description= {h}')






