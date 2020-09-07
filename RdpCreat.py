def file_read(name: str):
    with open(name, 'r', encoding='utf-8') as f:
        content = list(f.read().split('\n'))
    return content


def create_file_name(ip_addr: str):
    ip_addr = ip_addr.replace(".", "-")
    # ip = ip.split(".")
    name = "Group1_rdp_session{0}_{0}.remmina".format(ip_addr)
    return name


def creat_content(ip_addr: str, mo_ban: list):
    content = ""
    for line in mo_ban:
        if line[:4] == "name":
            content += "name=rdp_{}:33890\n".format(ip_addr)
        elif line[:6] == "server":
            content += "server={}:33890\n".format(ip_addr)
        elif line == "":
            continue
        else:
            content += line + "\n"
    return content


if __name__ == '__main__':
    ips = file_read("ips.txt")
    model = file_read("rdps/model.remmina")
    for ip in ips:
        if ip == "":
            continue
        file_name = "rdps/" + create_file_name(ip)
        file_content = creat_content(ip, model)
        with open(file_name, 'a', encoding="utf8") as file:
            file.writelines(file_content)
