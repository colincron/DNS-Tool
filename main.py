import dns.resolver


def dns_lookup(domain_name):
    try:
        mx_answers = dns.resolver.resolve(domain_name, 'MX')
        print("\n[+] MX mail servers associated with " + domain_name + ": ")
        for rdata in mx_answers:
            print('Host', rdata.exchange, 'has preference', rdata.preference)
    except dns.resolver.NoAnswer:
        print("/n[+] MX Mailserver record not available")


    a_answers = dns.resolver.resolve(domain_name,'A')
    print("\n[+] IPV4 addresses associated with " +domain_name + ": ")
    for data in a_answers:
        print(str(data))

    try:
        aaaa_answers = dns.resolver.resolve(domain_name, 'AAAA')
        print("\n[+] IPV6 addresses associated with " + domain_name + ": ")
        for rdata in aaaa_answers:
            print(rdata)
    except dns.resolver.NoAnswer:
        print("\n[+] IPV6 AAAA record not available")

    txt_answer = dns.resolver.resolve(domain_name, 'TXT')
    print("\n[+] TXT records: ")
    for data in txt_answer:
        print(data)

def sanitize_user_input(d_name):
    if d_name.startswith("http://www."):
        return d_name.replace("http://www.","")
    elif d_name.startswith("https://www."):
        return d_name.replace("https://www.","")
    elif d_name.startswith("https://"):
        return d_name.replace("https://","")
    elif d_name.startswith("http://"):
        return d_name.replace("http://","")
    else:
        return d_name

if __name__ == "__main__":
    domain_name = input("[+] Please enter domain name: ")
    dns_lookup(sanitize_user_input(domain_name))