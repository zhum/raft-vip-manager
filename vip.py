#!/usr/bin/env python

from raft.raft import RaftNode
import logging as log
from argparse import ArgumentParser
import time
import os
# address_book_fname = 'address_book.json'

DEF_PORT = 5567

vip = None
iface = None
nodename = None


def status_change(node, state):
    log.info(f"--> callback new state: {state} ({node})")
    log.info(f"==> {nodename} {iface} {vip}")

    if state == 'leader':
        # add VIP
        time.sleep(2)
        log.info(f"ip address add {vip} dev {iface}")
        os.popen(f"ip address add {vip} dev {iface}")
    elif state == 'follower':
        log.info(f"ip address del {vip} dev {iface}")
        os.popen(f"ip address del {vip} dev {iface}")


if __name__ == '__main__':
    log.basicConfig(
        filename=None,
        format='%(asctime)s: %(levelname)s %(message)s',
        level=log.WARNING,
    )

    # d = {"node0": {"ip": "127.0.0.1", "port": "5567"},
    #      "node1": {"ip": "127.0.0.1", "port": "5566"},
    #      "node2": {"ip": "127.0.0.1", "port": "5565"},
    #      "node3": {"ip": "127.0.0.1", "port": "5564"}}
    conf = {}

    p = ArgumentParser(description="Virtual IP manager", allow_abbrev=True)
    # p.add_argument('-h', '--help', help='Show help', nargs="*")
    p.add_argument('-n', '--node',
                   help="This node name", required=True)
    p.add_argument('-v', '--virtual-ip', dest='vip',
                   help="Virtual IP", required=True)
    p.add_argument('-i', '--interface',
                   help="Interface", required=True)
    p.add_argument('-V', '--verbose',
                   help="Be verbose", action='store_true')
    p.add_argument(
        '-l',
        '--list',
        help="List of nodes in format nodename:IP[:port],...",
        required=True)
    args = p.parse_args()

    if args.verbose:
        log.getLogger().setLevel(log.INFO)
    nodename = args.node
    vip = args.vip
    list = args.list
    iface = args.interface

    for n in list.split(sep=','):
        parts = n.split(sep=':')
        port = parts[2] if parts[2] else DEF_PORT
        conf[parts[0]] = {'ip': parts[1], 'port': port}

    if conf.get(nodename) is None:
        log.error(f"Nodename '{nodename}' is missing in the list ({','.join(conf.keys())})")  # noqa: E501

    log.warning(f"Staring node '{nodename}:{conf[nodename]['port']}'")
    log.warning(f"List of nodes: {', '.join(conf.keys())}")
    log.warning(f"Interface: {iface}, IP: {vip}")

    node = RaftNode(conf, nodename, 'follower',
                    callback=status_change)

    node.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        node.stop()
