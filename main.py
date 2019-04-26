import os
import signal
from terminaltables import AsciiTable
from fwork import ConfigFile
from pingmodule import Pkping
from results_handler import RHandler
from pprint import pprint

cf = ConfigFile()
pp = Pkping()
rh = RHandler()

# h = cf.get_host_description('8.8.8.8')
# # print(f'for 8.8.8.8 description= {h}')

os.system('cls')
print('PkPing Test [v.0.1]')
print('Press ctrl+c for quit\n')

for i in range(500):

    signal.signal(signal.SIGINT, lambda *_: os._exit(1))
    table_data = list()
    table_data.append(['Host', 'Description', 'Count', 'Lost, %', 'Av. rtt, ms',
                       'Lost 1m, %', 'Av. rtt 1m, ms', 'Lost 5m, %', 'Av. rtt 5m, ms', 'Responds'])

    # table_data.append(['Host', 'Description', 'Count', 'Lost, %', 'Av. rtt, ms'])

    responds = pp.get_results(cf.hosts)

    rh.add_result_to_general_array(responds)
    for host in cf.hosts:
        general_count, lost_percent, average_rtt, responds_string = rh.get_lost_percent(host, 0)
        lost_percent_1m, average_rtt_1m = lost_percent, average_rtt
        lost_percent_5m, average_rtt_5m = lost_percent, average_rtt

        if general_count > 60:
            count_1m, lost_percent_1m, average_rtt_1m, responds_string_1m = \
                rh.get_lost_percent(host, 60)

        if general_count > 300:
            count_5m, lost_percent_5m, average_rtt_1m, responds_string_1m = \
                rh.get_lost_percent(host, 300)

        table_line = [host, cf.get_host_description(host), general_count,
                      lost_percent, average_rtt, lost_percent_1m, average_rtt_1m,
                      lost_percent_5m, lost_percent_5m, responds_string]
        table_data.append(table_line)

    resultTable = AsciiTable(table_data)
    resultTable.inner_heading_row_border = True
    resultTable.outer_border = False
    resultTable.inner_row_border = False
    print('\033[3;0H', resultTable.table)


# print('-'*5, 'Create RHandler', '-'*5, '\n')
# rh = RHandler(r)
# for host in cf.hosts:
#     rh.get_lost_percent(host)
