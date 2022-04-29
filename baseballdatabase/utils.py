
def get_header_dict(header):
    header_dict = {}
    index = 0
    for col in header:
        header_dict[col] = index
        index += 1
    return header_dict
