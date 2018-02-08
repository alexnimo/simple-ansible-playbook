#!/usr/bin/env python

# notes: https://github.com/ansible/ansible/blob/stable-2.1/contrib/inventory/vagrant.py

import argparse
import json # required for output to be parsed by ansible
import sys # used for stdout

def parse_args():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--list', action='store_true')
    g.add_argument('--host')
    return p.parse_args()


def get_dynamic_hosts():
    # in the real world, this would make a call out to an external service or data source
    
    hosts = []
    hosts.append("rstahl-ve-001")
    return hosts


def get_dynamic_host_details(host):
    # in the real world, this would make a call out to an external service or data source.
    # for our purposes we will just return the same information regardless of hostname.
    
    return {'ve_mgmt_ip': '10.146.1.185/24',
            've_mgmt_ip_no_mask': '10.146.1.185',
	    've_mgmt_gw': '10.146.1.18',
            've_root_pass': 'Potatoes.1',
            've_admin_pass': 'Potatoes.1',
            've_src_file': '/home/rstahl/src/git/ansible-vmware-deploy-ve/img.nocommit/bigip-vmware-empty-properties.ova',
            've_net_ext': 'vro.lab.logical-internal',
            've_net_int': 'vro.lab.logical-internal',
            've_net_ha': 'vro.lab.logical-internal',
            've_net_mgmt': 'syseng_admin'}


def main():
    a = parse_args()
    if a.list: # group information
        h = get_dynamic_hosts()
        json.dump({'f5': h}, sys.stdout)
    else: # specific host
        h = get_dynamic_host_details(a.host)
        json.dump(h, sys.stdout)


if __name__ == '__main__':
    main()

# vim: set ts=4 sw=4 sts=4 et :
