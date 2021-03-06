#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

execfile("../slow/slow_analy_head.py")

tlen=50 # 50 or 100. or 200? # 200 is not that good.
pridir=homedir+"prime_ppcc/"

# ---

def load_ad_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_avg_%d_%d_50.txt"%(st, st+lt))


def load_ad_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_ad_std_%d_%d_50.txt"%(st, st+lt))


def load_od_avg(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_avg_%d_%d_50.txt"%(st, st+lt))


def load_od_std(st, lt): #start time, length of time period
    return loadtxt(pridir+"ppcc_od_std_%d_%d_50.txt"%(st, st+lt))

# ---

if tlen == 50:
    x1=load_od_avg(1000, tlen)
    y1=load_ad_avg(1000, tlen)
    d1=load_ad_std(1000, tlen)

    x15=load_od_avg(1050, tlen)
    y15=load_ad_avg(1050, tlen)
    d15=load_ad_std(1050, tlen)

    x2=load_od_avg(1100, tlen)
    y2=load_ad_avg(1100, tlen)
    d2=load_ad_std(1100, tlen)

    x25=load_od_avg(1150, tlen)
    y25=load_ad_avg(1150, tlen)
    d25=load_ad_std(1150, tlen)

    x3=load_od_avg(1200, tlen)
    y3=load_ad_avg(1200, tlen)
    d3=load_ad_std(1200, tlen)

    x35=load_od_avg(1250, tlen)
    y35=load_ad_avg(1250, tlen)
    d35=load_ad_std(1250, tlen)

    x4=load_od_avg(1300, tlen)
    y4=load_ad_avg(1300, tlen)
    d4=load_ad_std(1300, tlen)

    x45=load_od_avg(1350, tlen)
    y45=load_ad_avg(1350, tlen)
    d45=load_ad_std(1350, tlen)

    x5=load_od_avg(1400, tlen)
    y5=load_ad_avg(1400, tlen)
    d5=load_ad_std(1400, tlen)

    x55=load_od_avg(1450, tlen)
    y55=load_ad_avg(1450, tlen)
    d55=load_ad_std(1450, tlen)

    x6=load_od_avg(1500, tlen)
    y6=load_ad_avg(1500, tlen)
    d6=load_ad_std(1500, tlen)

    x65=load_od_avg(1550, tlen)
    y65=load_ad_avg(1550, tlen)
    d65=load_ad_std(1550, tlen)

    x7=load_od_avg(1600, tlen)
    y7=load_ad_avg(1600, tlen)
    d7=load_ad_std(1600, tlen)

    x75=load_od_avg(1650, tlen)
    y75=load_ad_avg(1650, tlen)
    d75=load_ad_std(1650, tlen)

    x8=load_od_avg(1700, tlen)
    y8=load_ad_avg(1700, tlen)
    d8=load_ad_std(1700, tlen)

    x85=load_od_avg(1750, tlen)
    y85=load_ad_avg(1750, tlen)
    d85=load_ad_std(1750, tlen)

    x9=load_od_avg(1800, tlen)
    y9=load_ad_avg(1800, tlen)
    d9=load_ad_std(1800, tlen)

    x95=load_od_avg(1850, tlen)
    y95=load_ad_avg(1850, tlen)
    d95=load_ad_std(1850, tlen)

    xa=load_od_avg(1900, tlen)
    ya=load_ad_avg(1900, tlen)
    da=load_ad_std(1900, tlen)

    xa5=load_od_avg(1950, tlen)
    ya5=load_ad_avg(1950, tlen)
    da5=load_ad_std(1950, tlen)

    xb=load_od_avg(2000, tlen)
    yb=load_ad_avg(2000, tlen)
    db=load_ad_std(2000, tlen)


    #fill_between(x=x1, y1=y1-d1, y2=y1+d1, alpha=0.2, antialiased=true) #, color="#089FFF"
    #fill_between(x=x15, y1=y15-d15, y2=y15+d15, alpha=0.2, antialiased=true) #, color="#089FFF"
    #fill_between(x=x2, y1=y2-d2, y2=y2+d2, alpha=0.2, antialiased=true) #, color="#089FFF"
    #fill_between(x=x25, y1=y25-d25, y2=y25+d25, alpha=0.2, antialiased=true) #, color="#089FFF"
    #fill_between(x=x3, y1=y3-d3, y2=y3+d3, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x35, y1=y35-d35, y2=y35+d35, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x4, y1=y4-d4, y2=y4+d4, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x45, y1=y45-d45, y2=y45+d45, alpha=0.2, antialiased=true) #, color="#089FFF"
    #fill_between(x=x5, y1=y5-d5, y2=y5+d5, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x55, y1=y55-d55, y2=y55+d55, alpha=0.2, antialiased=true) #, color="#089FFF"
#    fill_between(x=xb, y1=yb-db, y2=yb+db, alpha=0.2, antialiased=true) #, color="#089FFF"

    plot(x1,y1, '.-', markersize=3, label="1000");
    #plot(x15, y15,  '.-', markersize=3, label="1050");
    plot(x2,y2, '.-', markersize=4, label="1100");
    #plot(x25, y25,  '.-', markersize=4, label="1150");
    plot(x3,y3, '.-', markersize=4, label="1200");
    # plot(x35, y35,  '.-', markersize=4, label="1250");
    # plot(x4,y4, '.-', markersize=4, label="1300");
    # plot(x45, y45,  '.-', markersize=4, label="1350");
    #plot(x5,y5, '.-', markersize=4, label="1400");
    # plot(x55, y55,  '.-', markersize=4, label="1450");
    plot(xb,yb, '.-', markersize=4, label="2000");

# --- ---

if tlen == 100:

    x1=load_od_avg(1000, tlen)
    y1=load_ad_avg(1000, tlen)
    d1=load_ad_std(1000, tlen)

    x2=load_od_avg(1100, tlen)
    y2=load_ad_avg(1100, tlen)
    d2=load_ad_std(1100, tlen)

    x3=load_od_avg(1200, tlen)
    y3=load_ad_avg(1200, tlen)
    d3=load_ad_std(1200, tlen)

    x4=load_od_avg(1300, tlen)
    y4=load_ad_avg(1300, tlen)
    d4=load_ad_std(1300, tlen)

    x5=load_od_avg(1400, tlen)
    y5=load_ad_avg(1400, tlen)
    d5=load_ad_std(1400, tlen)

    x6=load_od_avg(1500, tlen)
    y6=load_ad_avg(1500, tlen)
    d6=load_ad_std(1500, tlen)

    x7=load_od_avg(1600, tlen)
    y7=load_ad_avg(1600, tlen)
    d7=load_ad_std(1600, tlen)

    x8=load_od_avg(1700, tlen)
    y8=load_ad_avg(1700, tlen)
    d8=load_ad_std(1700, tlen)

    x9=load_od_avg(1800, tlen)
    y9=load_ad_avg(1800, tlen)
    d9=load_ad_std(1800, tlen)

    xa=load_od_avg(1900, tlen)
    ya=load_ad_avg(1900, tlen)
    da=load_ad_std(1900, tlen)

    fill_between(x=x1, y1=y1-d1, y2=y1+d1, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x2, y1=y2-d2, y2=y2+d2, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x3, y1=y3-d3, y2=y3+d3, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x4, y1=y4-d4, y2=y4+d4, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x5, y1=y5-d5, y2=y5+d5, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x6, y1=y6-d6, y2=y6+d6, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x7, y1=y7-d7, y2=y7+d7, alpha=0.2, antialiased=true) #, color="#089FFF"

    plot(x1,y1, '.-', markersize=3, label="1000");
    plot(x2,y2, '.-', markersize=4, label="1100");
    plot(x3,y3, '.-', markersize=4, label="1200");
    # plot(x4,y4, '.-', markersize=4, label="1300");
    plot(x5,y5, '.-', markersize=4, label="1400");
    # plot(x6,y6, '.-', markersize=4, label="3500");
    # plot(x7,y7, '.-', markersize=4, label="3600");

# --- ---

if tlen == 200:

    x1=load_od_avg(1000, tlen)
    y1=load_ad_avg(1000, tlen)
    d1=load_ad_std(1000, tlen)

    x2=load_od_avg(1200, tlen)
    y2=load_ad_avg(1200, tlen)
    d2=load_ad_std(1200, tlen)

    x3=load_od_avg(1400, tlen)
    y3=load_ad_avg(1400, tlen)
    d3=load_ad_std(1400, tlen)

    x4=load_od_avg(1600, tlen)
    y4=load_ad_avg(1600, tlen)
    d4=load_ad_std(1600, tlen)

    x5=load_od_avg(1800, tlen)
    y5=load_ad_avg(1800, tlen)
    d5=load_ad_std(1800, tlen)

    fill_between(x=x1, y1=y1-d1, y2=y1+d1, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x2, y1=y2-d2, y2=y2+d2, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x3, y1=y3-d3, y2=y3+d3, alpha=0.2, antialiased=true) #, color="#089FFF"
    # fill_between(x=x4, y1=y4-d4, y2=y4+d4, alpha=0.2, antialiased=true) #, color="#089FFF"
    fill_between(x=x5, y1=y5-d5, y2=y5+d5, alpha=0.2, antialiased=true) #, color="#089FFF"

    plot(x1,y1, '.-', markersize=3, label="1000");
    plot(x2,y2, '.-', markersize=4, label="1200");
    plot(x3,y3, '.-', markersize=4, label="1400");
    # plot(x4,y4, '.-', markersize=4, label="1600");
    plot(x5,y5, '.-', markersize=4, label="1800");


# --- ---

fplot("y=x", [-1,1])
xlim([-0.2, 1.0])
ylim([-0.2, 1.0])
legend(loc='lower right', prop={'size':10})
xlabel("PPCC between stimulus")
ylabel("PPCC between representation")
savefig("PPCC_%d.jpg"%tlen)
savefig("PPCC_%d.eps"%tlen)
clf()
