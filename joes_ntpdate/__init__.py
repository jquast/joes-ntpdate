#!/usr/bin/env python
from __future__ import print_function
#
# Joe's own ntpdate: set the date and time via NTP
#
# This implementation doesn't mess around.  It requires root privileges,
# and sets the operating system and hardware clock to whatever value
# is found by the given ntp server.

# std imports
import subprocess
import argparse
import time
import sys

# 3rd-party
import ntplib

DATEHELP_STRFTIME_MAP = {
  'MMDDhhmm[[CC]YY][.ss]': '%m%d%H%M%Y.%S',  # gnu
  '[[[mm]dd]HH]MM[[cc]yy][.ss]]': '%m%d%H%M%Y.%S',  # osx
  '[[[[[[cc]yy]mm]dd]HH]MM[.SS]]': '%Y%m%d%H%M.%S',  # openbsd
}

def has_hwclock():
    try:
        _stdout, _stderr = subprocess.Popen(
                ['hwclock', '--version'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE).communicate()
    except OSError, err:
        if err.errno == 2:
            return False # no such file or directory
        raise
    return (_stdout + _stderr).startswith('hwclock from util-linux')

def get_strftime_fmt():
    _stdout, _stderr = subprocess.Popen(
            ['date', '--help'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE).communicate()

    for desc_fmt, strftime_fmt in DATEHELP_STRFTIME_MAP.items():
        if desc_fmt in (_stdout + _stderr):
            return strftime_fmt
    assert False, ("Could not determine system strftime, please file "
                   "a bug report: github.com/jquast/joes-ntpdate ",
                   (_stdout, _stderr))

def do_set_hwclock(struct_time):
    subprocess.check_call(['hwclock', '--systohc'])

def do_set_system(struct_time):
    # date(1): display or set date and time
    # -u: set date in UTC (Coordinated Universal) time.
    cmd_args = ['date', '-u', time.strftime(get_strftime_fmt(), struct_time)]
    proc = subprocess.Popen(cmd_args, cwd='/', shell=False,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    retcode = proc.wait()
    assert retcode == 0, (
            "\nReturned non-zero ({retcode}): {cmd_args}\n\n"
            "stdout: {stdout}\nstderr: {stderr}\n\n"
            "are you root?".format(
                retcode=retcode, cmd_args=cmd_args,
                stdout=stdout, stderr=stderr))

def ntpdate(ntp_host,
        retries=30, backoff_factor=2.0,
        set_hwclock=False, set_system=False):
    """ Program entry point. """

    assert not (set_hwclock and not set_system), (
            "To set hardware clock, you must also set system clock, "
            "as value is received by the system clock time."
            )

    ntpc = ntplib.NTPClient()

    for _try_num in range(retries):
        print('ntp host {0}: '.format(ntp_host), end='')
        try:
            resp = ntpc.request(ntp_host)

            remote_time = time.gmtime(resp.tx_time)

            if set_system:
                do_set_system(struct_time=remote_time)
                if set_hwclock and has_hwclock():
                    do_set_hwclock()
            synced = (
                    'synced OK, ' if (set_system or set_hwclock)
                    else '')
            print('{synced}stratum {resp.stratum} reports offset '
                  '{resp.offset:2.4f} seconds'
                  .format(resp=resp, synced=synced))
            return 0

        except ntplib.NTPException as err:
            print('NTPException: {0}'.format(err), end='')

            pause = backoff_factor * _try_num
            if pause:
                print('(sleeping {0}s)'.format(pause))
                time.sleep(pause)
            else:
                print()

    print('fatal: Gave up after {0} attempts.'.format(tries))
    return 1

def parse_args(args):
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description=(
                "Joe's own ntpdate: report or set clock by remote ntp host."
                ),
            epilog=(
                "Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable."
            ))

    parser.add_argument('--set-system', action='store_true',
            help='Set system clock to remote time.')
    parser.add_argument('--set-hwclock', action='store_true',
            help=('additionally, set hardware clock.  May do nothing '
                  'on platforms without hwclock(8)'))
    parser.add_argument('--retries', default=30, metavar='N',
            action='store', type=int, nargs='?',
            help='retry on failure up to N times.')
    parser.add_argument('--backoff_factor', default=2.0,
            action='store', type=float, nargs=1, metavar='N',
            help='retry backoff each step, sleep for {{<backoff-factor> * <retry-step>}}')
    parser.add_argument('ntp_host', default='pool.ntp.org',
            nargs='?',
            help='remote ntp host to synchronize clock with.'
            )

    return dict(parser.parse_args(args)._get_kwargs())

def main():
    exit(ntpdate(**parse_args(sys.argv[1:])))

if __name__ == '__main__':
    main()
