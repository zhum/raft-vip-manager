#!/usr/bin/env python
# from pathlib import Path
# import sys
# path_root = Path(__file__)
# sys.path.append(str(path_root))

from raft.raft import RaftNode
import json
# import time

address_book_fname = 'address_book.json'


def status_change(node, state):
    print(f"--> callback new state: {state} ({node})")


if __name__ == '__main__':
    d = {"node0": {"ip": "127.0.0.1", "port": "5567"},
         "node1": {"ip": "127.0.0.1", "port": "5566"},
         "node2": {"ip": "127.0.0.1", "port": "5565"},
         "node3": {"ip": "127.0.0.1", "port": "5564"}}

    with open(address_book_fname, 'w') as outfile:
        json.dump(d, outfile)

    #    s0 = RaftNode(address_book_fname, 'node0', 'follower')
    s1 = RaftNode(address_book_fname, 'node1', 'follower',
                  callback=status_change)

    #    s0.start()
    s1.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        #        s0.stop()
        s1.stop()
