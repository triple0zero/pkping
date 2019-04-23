from fwork import ConfigFile
from pingmodule import Pkping
from pprint import pprint

cf = ConfigFile()
print('-'*5, 'cf.config', '-'*5, '\n')
pprint(cf.config)
print('-'*5, 'cf.hosts', '-'*5, '\n')
pprint(cf.hosts)

print('-'*5, 'search host description by ip', '-'*5, '\n')
h = cf.get_host_description('8.8.8.8')
print(f'for 8.8.8.8 description= {h}')

pp = Pkping()
r = pp.get_results(cf.hosts)

print('-'*5, 'result by multiping one time for all hosts', '-'*5, '\n')

pprint(r)


