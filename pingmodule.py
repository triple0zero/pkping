from time import sleep
from multiping import MultiPing


class Pkping:

    def __init__(self):
        self.count = 0

    def get_results(self, hosts):
        results = []
        mp = MultiPing(hosts)
        mp.send()
        responses, no_responses = mp.receive(1)
        self.count += 1

        for host, rtt in responses.items():
            results.append({'host': host, 'if_answer': True, 'rtt': rtt})

        for host in no_responses:
            if no_responses:
                results.append({'host': host, 'if_answer': False})

        if len(no_responses) == 0:
            sleep(1)

        return results
