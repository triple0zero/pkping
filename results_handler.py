from pprint import pprint

class RHandler:

    def __init__(self, rlist):
        self.rlist = rlist

    def get_lost_percent(self, host):
        lost_count, final_rtt = 0, 0
        rlist_for_host = []
        for line in self.rlist:
            # print(line)
            if host == line['host']:
                rlist_for_host.append(line)
                if line['if_answer'] is False:
                    lost_count += 1
                else:
                    final_rtt += line['rtt']
        # pprint(rlist_for_host)
        if len(rlist_for_host) > 0:
            lost_p = round((lost_count / len(rlist_for_host)) * 100, 3)
            good_count = len(rlist_for_host) - lost_count
            if good_count > 0:
                average = round((1000 * final_rtt / good_count), 3)
            else:
                average = '-'
            print(f'host: {host}, lost percent: {lost_p}, average: {average}')
            return lost_p, average
        else:
            return print('Error: Not unknown host')


    # def resort(self, host):
    #     return
