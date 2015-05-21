Joe's Own ntpdate
=================

Set the date and time via NTP.

Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable.

This implementation doesn't mess around.  It requires root privileges,
and sets the operating system and hardware clock to whatever value
is found by the given ntp server.

::

        usage: __init__.py [-h] [--set-system] [--set-hwclock] [--retries [N]]
                           [--backoff_factor N]
                           [ntp_host]

        Joe's own ntpdate: report or set clock by remote ntp host.

        positional arguments:
          ntp_host            remote ntp host to synchronize clock with. (default:
                              pool.ntp.org)

        optional arguments:
          -h, --help          show this help message and exit
          --set-system        Set system clock to remote time. (default: False)
          --set-hwclock       additionally, set hardware clock. May do nothing on
                              platforms without hwclock(8) (default: False)
          --retries [N]       retry on failure up to N times. (default: 30)
          --backoff_factor N  retry backoff each step, sleep for {{<backoff-factor> *
                              <retry-step>}} (default: 2.0)

        Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable.

This package uses `ntplib <https://pypi.python.org/pypi/ntplib/>`_
