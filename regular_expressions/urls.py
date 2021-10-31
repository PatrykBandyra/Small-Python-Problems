import re


if __name__ == '__main__':

    urls = '''
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    '''

    pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

    subbed_urls = pattern.sub(r'\2\3', urls)  # Substitution

    print(subbed_urls)

    # matches = pattern.finditer(urls)
    #
    # for match in matches:
    #     print(match.group(2))
