# flake8: noqa E501
import pandas

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>


  <input type="hidden" name="uin" id="uin" value="i-06a9ca87d0f09344a">
<form>

  <input type="hidden" name="uin" id="uin" value="i-06a9ca87d0f09344a">

<table><tr><th>#<th>enc<th>dec<th>ports<th>created<th>time left<th>

<tr><th>1<td><b><font color=#001020>$SBXMCH</font></b><td><b><font color=#001020>$RWO0WI</font></b><td>1800-1809<td>2023.03.06 08:05:54<td>03:18:41<td><a href=light_status.php onclick="Apply(3, 1, '$SBXMCH', '$RWO0WI'); return false;">delete this</a>
<tr><th>2<td><b><font color=#001020>$S21NYI</font></b><td><b><font color=#001020>$R8RUAB</font></b><td>2003<td>2023.03.06 14:46:48<td>00:59:35<td><a href=light_status.php onclick="Apply(3, 2, '$S21NYI', '$R8RUAB'); return false;">delete this</a>
<tr><th>*<td colspan=4><a href="sreq.php">Request public session from broker</a><br/>

</table>
  <input type="hidden" name="uin" id="uin" value="i-06a9ca87d0f09344a">
</form>


</body>

</html>
"""


dfs = pandas.read_html(html)
print(type(dfs))

for i in range(4):
    print(f"count: {i}")
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
