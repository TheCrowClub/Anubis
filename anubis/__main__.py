from os import path

import click
from validators import ipv4

from anubis import is_good, sort_list


@click.command()
@click.option("-f", "--filename", "dest", default="proxies.txt", show_default=True)
@click.option(
    "-p",
    "--protocol",
    "protocol",
    show_default=True,
    default="http",
    help="Proxy Protocol. Ex: http, https,socks4, socks5",
)
@click.option(
    "-s", "--sort", "sort", is_flag=True, help="Sort as ping time.", show_default=True
)
def main(dest, protocol, sort):
    if path.exists(dest):
        with open(dest) as f:
            ips = [line.rstrip("\n") for line in f]
    else:
        print(f"File {dest} doesn't exists.")
    valid_ips = []
    for ip in ips:
        try:
            if ipv4(ip[0 : ip.index(":")]):
                valid_ips.append(ip)
        except Exception:
            pass

    good_ips = []
    for ip in valid_ips:
        active = is_good(protocol, ip)
        if active:
            good_ips.append(active)

    with open("goodips.txt", "w") as f:
        if sort:
            for ip, _ in sort_list(good_ips):
                f.write(ip)
        else:
            for ip, _ in good_ips:
                f.write(ip)


main()
