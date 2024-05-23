import psycopg2
import numpy as np
import matplotlib.pyplot as mp
a = 2;
if a == 1:


    con = psycopg2.connect("dbname=BASE_SELIVERSTOV user=postgres host=localhost port=5432 password=qweasdzxc123")

    cur = con.cursor()
    cur.execute("SELECT x, y FROM fn  ORDER BY x;")
    #cur.execute("SELECT x, y FROM positive  ORDER BY x;")
    arr = cur.fetchall()

    cur.close()
    con.close()

    f = open("scen.csv", "w" )

    for row in arr:
        f.write(f"{row[0]}, {row[1]}\n")

    f.close()
else :
    con = psycopg2.connect("dbname=BASE_SELIVERSTOV user=postgres host=localhost port=5432 password=qweasdzxc123")

    cur = con.cursor()
    #cur.execute("SELECT x, y FROM fn ORDER BY x;")
    cur.execute("SELECT x , y FROM fn_file ORDER BY x;")
    #cur.execute("SELECT x, y FROM positive  ORDER BY x;")
    #cur.execute("SELECT x, y FROM fn_view  ORDER BY x;")
    
    arr = cur.fetchall()

    cur.close()
    con.close()

    x , y = np.array(arr).T

    mp.scatter(x, y, s = 0.3)

    mp.title('sin wave')
    mp.xlabel('x')
    mp.ylabel('y = sin(x)')

    mp.grid(True, which ='both')
    mp.axhline(y = 0, color = 'k')

    mp.show()