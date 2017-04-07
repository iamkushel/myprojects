from urllib import request


def download_file(url_file):
    file_open = request.urlopen(url_file)
    file_read = file_open.read()
    str_file_read = str(file_read)
    lines = str_file_read.split("\\n")
    dest_url = r'goog.csv'
    fx =open('dest_url', 'w')
    for line in lines:
        fx.write(line + '\n')


download_file('http://chart.finance.yahoo.com/table.csv?s=GOOG&a=1&b=21&c=2017&d=2&e=21&f=2017&g=d&ignore=.csv')
