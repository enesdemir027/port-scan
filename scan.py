import socket

# Yaygın kullanılan portlar
ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

# Riskli olabilecek portlar
risky = {
    21: "FTP genelde güvensiz olabilir",
    23: "Telnet şifreleme kullanmaz",
    445: "SMB saldırılara açık olabilir",
    3389: "RDP brute-force saldırılarına açık olabilir"
}

def port_kontrol(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        sonuc = s.connect_ex((ip, port))
        s.close()

        return sonuc == 0
    except:
        return False

def main():
    hedef = input("Hedef IP gir: ")

    print("\nTarama başlıyor...\n")

    acik_portlar = []

    for port, isim in ports.items():
        if port_kontrol(hedef, port):
            print(f"[AÇIK] {port} - {isim}")
            acik_portlar.append(port)

    print("\nAnaliz:\n")

    if not acik_portlar:
        print("Açık port bulunamadı.")
    else:
        for port in acik_portlar:
            if port in risky:
                print(f"[UYARI] {port}: {risky[port]}")

    print("\nTarama bitti.")

if __name__ == "__main__":
    main()