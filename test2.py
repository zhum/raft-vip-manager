#!/usr/bin/env python

from raft.raft import RaftNode
# import time

address_book_fname = 'address_book.json'


def status_change(node, state):
    print(f"--> callback new state: {state} ({node})")


if __name__ == '__main__':
    s2 = RaftNode(address_book_fname,
                  'node2',
                  'follower',
                  callback=status_change)
#    s3 = RaftNode(address_book_fname, 'node3', 'follower')

    s2.start()
#    s3.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s2.stop()
#        s3.stop()
