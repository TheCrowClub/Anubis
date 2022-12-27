from os import path

import rich_click as click
from rich.live import Live
from rich.table import Table
from validators import ipv4

from anubis import is_good, sort_list

table = Table(title="Anubis")
table.add_column("IP")
table.add_column("Status")
table.add_column("Ping Time (ms)")


@click.command()
@click.option(
    "-f", "--filename", "dest", default="proxies.txt", show_default=True
)
@click.option(
    "-p",
    "--protocol",
    "protocol",
    show_default=True,
    default="http",
    help="Proxy Protocol. Ex: http, https,socks4, socks5",
)
@click.option(
    "-s",
    "--sort",
    "sort",
    is_flag=True,
    help="Sort as ping time.",
    show_default=True,
)
def main(dest, protocol, sort):
    if path.exists(dest):
        with open(dest) as f:
            ips = [line.rstrip("\n") for line in f]
    else:
        exit(f"File {dest} doesn't exists.")
    valid_ips = []
    for ip in ips:
        try:
            if ipv4(ip[0 : ip.index(":")]):
                valid_ips.append(ip)
        except Exception:
            pass

    good_ips = []
    with Live(table):
        for ip in valid_ips:
            active = is_good(protocol, ip)
            if active:
                table.add_row(ip, "[green]Success", str(active))
                good_ips.append(ip)
            else:
                table.add_row(ip, "[red]Error")

    with open("goodips.txt", "w") as f:
        if sort:
            for ip in sort_list(good_ips):
                f.write(f"{ip}\n")
        else:
            for ip in good_ips:
                f.write(f"{ip}\n")


if __name__ == "__main__":
    main()
