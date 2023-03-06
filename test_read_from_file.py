import pathlib

import pandas

path = pathlib.Path("test.html")

dfs = pandas.read_html(path)
print(type(dfs))

for i in range(4):
    try:
        print(dfs[i].head())
    except IndexError:
        break

    try:
        df = dfs[i]
        print(df[["ports", "enc", "dec"]])
    except IndexError:
        break
