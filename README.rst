Joe's Own ntpdate
=================

Set the date and time via NTP.

Assumes bsd or gnu date(1) and gnu hwclock(8) if applicable.

This implementation doesn't mess around.  It requires root privileges,
and sets the operating system and hardware clock to whatever value
is found by the given ntp server.
