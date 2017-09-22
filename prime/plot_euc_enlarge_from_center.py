execfile("../slow/slow_analy_head.py")

tbgn=1150 # comment this region when runing outside
tlen=50
tend=tbgn+tlen
td=50   # comment this region when runing outside

print("\nthis is yet another new version of plot_euc.py")
print(" --- it computes Euc distance from each trial to the center of all trial vectors")
print("time period:", tbgn,tend)

def dist_from_Qcs_to_center_avg_std_ls(c,s, tb,te,td):
    # for given odor (defined by c and s),
    # compute all trials avg&std distance of this odor to center,
    # tb te td defines the begin end and length of the sf duration.
    # the yls is for all trials.
    xls=[load_sf_from_file(c,s,t,tb,te,td) for t in range(trial_number)]
    center=mean(xls,0)
    yls=[norm(i-center) for i in xls]
    return avg(yls), std(yls), yls


def dist_ls_for_a_couple_avg_std(c, tb,te,td):
    # for the given couple (c),
    # compute the distance between (1) each its shifts and (2) the center of all shifts
    d_avg, d_std = zeros(shift_number), zeros(shift_number)
    for i,s in enum(shift_list):
        d_avg[i],d_std[i],_ = dist_from_Qcs_to_center_avg_std_ls(c,s,tbgn,tend, td)
    return d_avg, d_std


print("odor decorr in AL")
print("begin time=%d, end time=%d"%(tbgn,tend))


od_avg  , od_std = dist_ls_for_a_couple_avg_std(odor_coupling,tbgn,tend,td)
rd_avg0 ,rd_std0 = dist_ls_for_a_couple_avg_std(0, tbgn,tend, td)
rd_avg1 ,rd_std1 = dist_ls_for_a_couple_avg_std(1, tbgn,tend, td)
rd_avg2 ,rd_std2 = dist_ls_for_a_couple_avg_std(2, tbgn,tend, td)
rd_avg3 ,rd_std3 = dist_ls_for_a_couple_avg_std(3, tbgn,tend, td)
rd_avg4 ,rd_std4 = dist_ls_for_a_couple_avg_std(4, tbgn,tend, td)
"""
    rd_avg5 ,rd_std5 = dist_ls_for_a_couple_avg_std(5, tbgn,tend, td)
    rd_avg6 ,rd_std6 = dist_ls_for_a_couple_avg_std(6, tbgn,tend, td)
    rd_avg7 ,rd_std7 = dist_ls_for_a_couple_avg_std(7, tbgn,tend, td)
    rd_avg8 ,rd_std8 = dist_ls_for_a_couple_avg_std(8, tbgn,tend, td)
    rd_avg9 ,rd_std9 = dist_ls_for_a_couple_avg_std(9, tbgn,tend, td)
    rd_avg10,rd_std10= dist_ls_for_a_couple_avg_std(10,tbgn,tend, td)
    rd_avg11,rd_std11= dist_ls_for_a_couple_avg_std(11,tbgn,tend, td)
    rd_avg12,rd_std12= dist_ls_for_a_couple_avg_std(12,tbgn,tend, td)
    rd_avg13,rd_std13= dist_ls_for_a_couple_avg_std(13,tbgn,tend, td)
    rd_avg14,rd_std14= dist_ls_for_a_couple_avg_std(14,tbgn,tend, td)
    rd_avg15,rd_std15= dist_ls_for_a_couple_avg_std(15,tbgn,tend, td)
    rd_avg16,rd_std16= dist_ls_for_a_couple_avg_std(16,tbgn,tend, td)
    rd_avg17,rd_std17= dist_ls_for_a_couple_avg_std(17,tbgn,tend, td)
    rd_avg18,rd_std18= dist_ls_for_a_couple_avg_std(18,tbgn,tend, td)
    rd_avg19,rd_std19= dist_ls_for_a_couple_avg_std(19,tbgn,tend, td)
"""

# Now let's do average over couples. since they have just been loadded in couple
ad_avg =mean([rd_avg0, rd_avg1, rd_avg2, rd_avg3, rd_avg4], 0)#rd_avg5, rd_avg6, \
              #rd_avg7, rd_avg8, rd_avg9, rd_avg10, rd_avg11, rd_avg12, rd_avg13,\
              #rd_avg14, rd_avg15, rd_avg16, rd_avg17, rd_avg18, rd_avg19], 0)

ad_std =mean([rd_std0, rd_std1, rd_std2, rd_std3,  rd_std4], 0)#rd_std5,rd_std6, \
              #rd_std7, rd_std8, rd_std9, rd_std10, rd_std11, rd_std12, rd_std13,\
              #rd_std14,rd_std15,rd_std16,rd_std17, rd_std18, rd_std19], 0)


savetxt("euc2center_od_avg_%d_%d_%d.txt"%(tbgn,tend,tlen), od_avg)
savetxt("euc2center_od_std_%d_%d_%d.txt"%(tbgn,tend,tlen), od_std)
savetxt("euc2center_ad_avg_%d_%d_%d.txt"%(tbgn,tend,tlen), ad_avg)
savetxt("euc2center_ad_std_%d_%d_%d.txt"%(tbgn,tend,tlen), ad_std)


fplot("y=x", [0,500])
fill_between(x=od_avg, y1=ad_avg-ad_std, y2=ad_avg+ad_std, \
             alpha=0.2, color="#089FFF", antialiased=true)
plot(od_avg, ad_avg, '.-', color='m'); #white');

#xlim([0,400])
#ylim([0,400])
xlabel("stimulation distance")
ylabel("representation distance")
savefig("dis2center_%d_%d_%d_new.jpg"%(tbgn,tend,tlen))
savefig("dis2center_%d_%d_%d_new.eps"%(tbgn,tend,tlen))
show()
clf()

# ...

stp=4
sls=[]
# remove the items of shift1-shift5
# shift1-5 are no longer in the shift_list
#od_avg = array([od_avg[i] for i in range(shift_number) if i==0 or i>=6])
#ad_avg = array([ad_avg[i] for i in range(shift_number) if i==0 or i>=6])

for i in range(len(od_avg)-stp):
    x=od_avg[i:i+stp]
    y=ad_avg[i:i+stp]
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    sls.append(slope)

xlabel("#")
ylabel("slope")
plot(sls, '.-')

savefig("dis2center_slope_%d_%d_%d_new.jpg"%(tbgn,tend,tlen))
savefig("dis2center_slope_%d_%d_%d_new.eps"%(tbgn,tend,tlen))
show()
clf()
