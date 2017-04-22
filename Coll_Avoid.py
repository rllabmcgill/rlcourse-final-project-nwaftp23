from CC_functions import *
from Test_policy import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


state = math.floor(div_y*(s_y/SCREEN_HEIGHT))*div_x+math.ceil(div_y*(s_x/SCREEN_WIDTH))
alpha = 70
beta = .02
theta = np.zeros(n)
w = np.random.randn(ns)
# Assistance for plain PG
theta[0::4]+=1
theta[2::4]+=1
var = 10
lamb = 100
print(state)

np.random.seed(10)
CMDP = PG_CC(state, alpha , beta, theta, lamb)
MDP = PG(state, theta)
#MDP_AC = AC(state,theta,w)
#MDP_ACCC = AC_CC(state, var , theta, w, lamb, alpha, beta)
theta2=CMDP[0]
theta3 = MDP

m=10000
x = test_policy(state, theta2, m)
x2 = test_policy(state, theta3, m)
num_bins = 20

print(np.mean(x))
print(np.std(x))
print(np.mean(x2))
print(np.std(x2))
fig1 = plt.figure()
ax1 = fig1.add_subplot(2, 1, 1)
ax2 = fig1.add_subplot(2, 1, 2)
n, bins, patches = ax1.hist(x,bins=range(min(x), max(x) + 20, 20),facecolor='blue', edgecolor='black',lw=2)
ax1.set_ylabel('Frequency')
ax1.grid(True)

#ax2 = fig2.add_subplot(1, 1, 1)
n, bins, patches = ax2.hist(x2,bins=range(min(x2), max(x2) + 20, 20),facecolor='green',edgecolor='black',lw=2)
ax2.set_xlabel('Cost')
ax2.set_ylabel('Frequency')
plt.grid(True)

plt.show()
