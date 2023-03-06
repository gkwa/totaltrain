import pathlib

import pandas

path = pathlib.Path("test.html")

dfs = pandas.read_html(path)
print(type(dfs))

for i in range(4):
    try:
        print(type(dfs[i]))
    except IndexError:
        break

    try:
        print(dfs[i].info)
    except IndexError:
        break

    try:
        print(dfs[i].head())
    except IndexError:
        break

    try:
        print(dfs[i].columns)
    except IndexError:
        break

    try:
        df = dfs[i]
        print(df[["ports", "enc", "dec"]])
    except IndexError:
        break
