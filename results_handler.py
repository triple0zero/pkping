from pprint import pprint


class RHandler:

    def __init__(self):
        self.general_array = []

    def add_result_to_general_array(self, rlist):

        self.general_array.extend(rlist)
        return self.general_array

    def get_lost_percent(self, host, q):
        lost_count, final_rtt = 0, 0
        rlist_for_host = []
        q=int(q)

        for line in self.general_array:
            # pprint(line)
            if host == line['host']:
                rlist_for_host.append(line)
                if line['if_answer'] is False:
                    lost_count += 1
                else:
                    final_rtt += line['rtt']
        if q > 0:
            rlist_for_host = rlist_for_host[len(rlist_for_host):len(rlist_for_host)-q+1:-1]
        elif q == 0:
            pass
        else:
            print('Error: Unknown queue size')

        # pprint(rlist_for_host)
        general_count = len(rlist_for_host)
        if general_count > 0:
            lost_p = round((lost_count / general_count) * 100, 3)
            good_count = general_count - lost_count
            if good_count > 0:
                average = round((1000 * final_rtt / good_count), 3)
            else:
                average = '-'
            # print(f'host: {host}, lost percent: {lost_p}, average: {average}')

            return general_count, lost_p, average, self.print_respond(rlist_for_host)
        else:
            return print('Error: unknown host')

    def print_respond(self, array):
        responds = ''
        for line in array:
            # pprint(line)
            if line['if_answer']:
                responds += '!'
            else:
                responds += '.'
        return responds


    # def resort(self, host):
    #     return
