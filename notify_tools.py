"""
Command line tools wrapping growlnotify.

timer -- ergonomic or productivity timer (e.g., pomodoro technique)
todo -- post todos (sticky by default)
"""

import time
import os
import click


@click.command()
@click.version_option()
@click.argument('rounds', default=5)
@click.option('work', '-w', '--work-time', default=26,
              help='minutes of work time between breaks')
@click.option('play', '-p', '--play-time', default=3,
              help='minutes of break')
@click.option('order', '-wf', '--work-first', flag_value='w', default=True,
              help='Work first. Default.')
@click.option('order', '-pf', '--play-first', flag_value='p',
              help='Play first.')
def timer(rounds, work, play, order):
    """Work play erognomic timer.

    Specify the work and play durations. An optional argument adds the number
    of work/play ROUNDS after which to exit (default = 5)

    EXAMPLE: to work for 10 rounds 15 with 1 minute breaks, with play first use:

    timer -w 15 -p 1 5

    Closing prior to ROUNDS done terribly: use CTL-C or kill PID.
    """
    current = 0
    while current < rounds:
        if order == 'w':
            _work(work)
            _play(play)
        elif order == 'p':
            _play(play)
            _work(work)
        current += 1
    return


def _play(play):
    for i in xrange(play * 12):
        _notify('go take a break for 1 min')
        time.sleep(5)


def _work(work):
    for i in xrange(work):
        _notify('WORK for 1 min')
        time.sleep(60)


@click.command()
@click.version_option()
@click.argument('item')
@click.option('--sticky', is_flag=True, default=True)
def todo(item, sticky):
    """growltodo

    growltodo item
    """
    _notify(item, sticky)


def _notify(msg, sticky=False):
    if sticky:
        os.system('growlnotify -s -m \'' + msg + '\'')
    else:
        os.system('growlnotify -m \'' + msg + '\'')
    return
