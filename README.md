
# Anubis

This script judge proxy instead of soul.



## Installation

Anubis still in beta, and not in pypi (yet). 

### From Source with Git
```bash
  pip3 install git+https://github.com/TheCrowClub/Anubis
```
    
### From srouce with http link
```bash
pip3 install https://github.com/TheCrowClub/Anubis/archive/refs/heads/master.zip
```
## Usage/Examples

```console
munin@thecrowclub:~$ anubis --help
Usage: anubis [OPTIONS]

Options:
  -f, --filename TEXT  [default: proxies.txt]
  -p, --protocol TEXT  Proxy Protocol. Ex: http,
                       https,socks4, socks5  [default:
                       http]
  -s, --sort           Sort as ping time.
  --help               Show this message and exit.
```

