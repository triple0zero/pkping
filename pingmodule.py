from time import sleep
from multiping import MultiPing


class Pkping:

    def __init__(self):
        self.count = 0
        self.results = []

    def get_results(self, hosts):
        mp = MultiPing(hosts)
        mp.send()
        responses, no_responses = mp.receive(1)
        self.count += 1

        for host, rtt in responses.items():
            self.results.append({'host': host, 'if_answer': True, 'rtt': rtt})

        for host in no_responses:
            if no_responses:
                self.results.append({'host': host, 'if_answer': False})

        return self.results
