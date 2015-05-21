.. image:: https://img.shields.io/travis/erikrose/joes-ntpdate.svg
    :alt: Travis Continous Integration
    :target: https://travis-ci.org/erikrose/joes-ntpdate/

.. image:: https://coveralls.io/repos/erikrose/joes-ntpdate/badge.png?branch=master
    :alt: Coveralls Code Coverage
    :target: https://coveralls.io/r/erikrose/joes-ntpdate?branch=master

.. image:: https://img.shields.io/pypi/v/joes-ntpdate.svg
    :alt: Latest Version
    :target: https://pypi.python.org/pypi/joes-ntpdate

.. image:: https://pypip.in/license/joes-ntpdate/badge.svg
    :alt: License
    :target: http://opensource.org/licenses/MIT

.. image:: https://img.shields.io/pypi/dm/joes-ntpdate.svg
    :alt: Downloads
    :target: https://pypi.python.org/pypi/joes-ntpdate


Joe's Own ntpdate
=================

Set the date and time via NTP.

Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable.

This implementation doesn't mess around.  It requires root privileges,
and sets the operating system and hardware clock to whatever value
is found by the given ntp server.

::

        usage: joes-ntpdate [-h] [--set-system] [--set-hwclock] [--retries [N]]
                            [--backoff-factor N]
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
          --backoff-factor N  retry backoff each step, sleep for {{<backoff-factor> *
                              <retry-step>}} (default: 2.0)

        Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable.
