from fwork import ConfigFile
from pingmodule import Pkping
from results_handler import RHandler
from pprint import pprint

cf = ConfigFile()

# h = cf.get_host_description('8.8.8.8')
# print(f'for 8.8.8.8 description= {h}')

pp = Pkping()
r = []
rh = RHandler()
for i in range(10):
    r = pp.get_results(cf.hosts)
    print('-'*5, 'result by multiping for all hosts', '-'*5, '\n')
    pprint(r)
    print('-' * 5, 'Create RHandler', '-' * 5, '\n')
    rh.add_result_to_general_array(r)
    for host in cf.hosts:
        rh.get_lost_percent(host)

# print('-'*5, 'Create RHandler', '-'*5, '\n')
# rh = RHandler(r)
# for host in cf.hosts:
#     rh.get_lost_percent(host)
