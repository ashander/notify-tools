Command line productivity tools that use notifiers

```sh
timer -- ergonomic or productivity timer (e.g., pomodoro technique)
todo -- post todos (that may be sticky)
```

These rely on wrapping a CLI notifier. Currently only
[growlnotify](http://growl.info/downloads) is supported[^old].
But, pull requests are welcome.

[^old]: yes, my development environment is frighteningly old

## INSTALL

```sh
$ git clone https://github.com/ashander/notify-tools.git
$ cd notify-tools
$ pip install .
```

## Details

The nice CLI interface is made possible by [click](http://click.pocoo.org/4/)
