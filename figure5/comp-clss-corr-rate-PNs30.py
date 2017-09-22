execfile('../slow/slow_analy_head.py')

idx = range(PN_number)
tb = 1100
te = 1350
use_num = 30  #use 30 PNs (of 830 PNs)
print('use %d PNs'%use_num)


def dist_to_cent(x, cent_ls):
    # distance from x to each center (each mean)
    return [norm(x-i) for i in cent_ls]

def if_class_corr(x, s, cent_ls):
    # if the nearest neighbor of x is the correct center?:
    #    True  --- correct
    #    False --- wrong
    dist_ls = dist_to_cent(x, cent_ls)
    s = int(round(s/6))
    if 0.99999<(1.0*dist_ls[s]/min(dist_ls))<1.00001:
        return 1 # True
    return 0 #False


try_num = 100 # try 100 times (selsect 100 group PNs)
resp_ccr = zeros(try_num)
stim_ccr = zeros(try_num)
stim_coup = 100
resp_coup = 0


for the_ith_try in range(try_num):
    print('\n\ntry:',the_ith_try)
    use_idx = choice(idx,use_num) # random select the PNs
    print('PNs:', use_idx)
    stim_cent_ls = [load_sf_avged_over_trial(stim_coup,s,tb,te)[use_idx] for s in shift_list]
    resp_cent_ls = [load_sf_avged_over_trial(resp_coup,s,tb,te)[use_idx] for s in shift_list]

    resp_corr_num = 0
    resp_total_num = 0
    for s in shift_list:  # how many trials of s-th odor(shift) correctly classfied??
        for t in range(trial_number): # all the shifts and trials are considered...
            resp_total_num += 1
            x=load_sf_from_file(resp_coup,s,t,tb,te)[use_idx]
            resp_corr_num += if_class_corr(x,s,resp_cent_ls)
    resp_this_ccr=1.0*resp_corr_num/resp_total_num
    print('for couple', resp_coup, ', the classify correct ratio is:', resp_this_ccr)
    resp_ccr[the_ith_try]=resp_this_ccr

    stim_corr_num = 0
    stim_total_num = 0
    for s in shift_list:  # same with above
        for t in range(trial_number):
            stim_total_num += 1
            x=load_sf_from_file(stim_coup,s,t,tb,te)[use_idx]
            stim_corr_num += if_class_corr(x,s,stim_cent_ls)
    stim_this_ccr=1.0*stim_corr_num/stim_total_num
    print('for couple', stim_coup, ', the classify correct ratio is:', stim_this_ccr)
    stim_ccr[the_ith_try]=stim_this_ccr


savetxt('./data/clss-corr-rate-couple0-use%dPNs.txt'%use_num, resp_ccr)
savetxt('./data/clss-corr-rate-couple100-use%dPNs.txt'%use_num, stim_ccr)
