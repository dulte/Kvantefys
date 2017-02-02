using PyPlot

r = collect(-3.0:.01:3.0)

V(r) = (r)^1e9

#xkcd()
xlabel("r/a")
ylabel("V(r)")
title("V(r) for store k")
plot(r,map(V,r),"r", -1.2,0,1.2,1)
show()
