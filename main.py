import dns.resolver


def dns_lookup(domain_name):
    try:
        answers = dns.resolver.resolve(domain_name, 'MX')
        print("")
        for rdata in answers:
            print('\n[+] Host', rdata.exchange, 'has preference', rdata.preference)
    except dns.resolver.NoAnswer:
        print("/n[+] MX Mailserver record not available")


    a_answers = dns.resolver.resolve(domain_name,'A')
    print("\n[+] IP addresses associated with " +domain_name + ": ")
    for data in a_answers:
        print(str(data))

    try:
        aaaa_answers = dns.resolver.resolve(domain_name, 'AAAA')
        for rdata in aaaa_answers:
            print(rdata)
    except dns.resolver.NoAnswer:
        print("\n[+] IPV6 AAAA record not available")

    txt_answer = dns.resolver.resolve(domain_name, 'TXT')
    print("\n[+] TXT records: ")
    for data in txt_answer:
        print(data)

if __name__ == "__main__":
    domain_name = input("[+] Please enter domain name: ")
    if domain_name.startswith("http://www."):
        dns_lookup(domain_name.replace("http://www.",""))
    elif domain_name.startswith("https://www."):
        dns_lookup(domain_name = domain_name.replace("https://www.",""))