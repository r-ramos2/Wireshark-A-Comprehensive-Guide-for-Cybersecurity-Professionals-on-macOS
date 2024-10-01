import dpkt
import socket
import pygeoip

# Initialize the GeoIP object
gi = pygeoip.GeoIP('GeoLiteCity.dat')

def main():
    # Use a context manager to ensure the file is properly closed
    with open('wire.pcap', 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        kmlheader = (
            '<?xml version="1.0" encoding="UTF-8"?> \n'
            '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
            '<Document>\n'
            '<Style id="transBluePoly">'
            '<LineStyle>'
            '<width>1.5</width>'
            '<color>501400E6</color>'
            '</LineStyle>'
            '</Style>'
        )
        kmlfooter = '</Document>\n</kml>\n'
        kmldoc = kmlheader + plotIPs(pcap) + kmlfooter

    print(kmldoc)

def plotIPs(pcap):
    output = []
    for ts, buf in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data  # Get the IP layer directly
            if isinstance(ip, dpkt.ip.IP):  # Ensure it's an IP packet
                src_ip = socket.inet_ntoa(ip.src)
                loc = gi.record_by_addr(src_ip)
                if loc is not None:
                    output.append(
                        f'<Placemark><name>{src_ip}</name>'
                        f'<description>{loc[1]} {loc[2]}</description>'
                        f'<Point><coordinates>{loc[3]},{loc[2]}</coordinates></Point></Placemark>\n'
                    )
        except (dpkt.dpkt.NeedData, AttributeError) as e:
            # Handle exceptions for malformed packets or missing data
            print(f"Skipping packet due to error: {e}")
    return ''.join(output)  # Join the list into a single string

if __name__ == "__main__":
    main()
