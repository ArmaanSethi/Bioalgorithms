import numpy as np
# ssh chicken@142.93.55.188
def viterbi(obs_seq):
        # returns the most likely state sequence given observed sequence x
        # using the Viterbi algorithm
        T = len(obs_seq)
        N = A.shape[0]
        delta = np.zeros((T, N))
        psi = np.zeros((T, N))
        delta[0] = pi*B[:,obs_seq[0]]
        for t in range(1, T):
            for j in range(N):
                delta[t,j] = np.max(delta[t-1]*A[:,j]) * B[j, obs_seq[t]]
                psi[t,j] = np.argmax(delta[t-1]*A[:,j])

        # backtrack
        states = np.zeros(T, dtype=np.int32)
        states[T-1] = np.argmax(delta[T-1])
        for t in range(T-2, -1, -1):
            states[t] = psi[t+1, states[t+1]]
        return states
    
def forward(obs_seq, pi, A, B):
    T = len(obs_seq)
    N = A.shape[0]
    alpha = np.zeros((T, N))
    alpha[0] = pi*B[:,obs_seq[0]]
    for t in range(1, T):
        alpha[t] = np.inner(alpha[t-1],A) * B[:, obs_seq[t]]
    return alpha

def likelihood(alpha):
    # returns log P(Y  \mid  model)
    # using the forward part of the forward-backward algorithm
    return  alpha[-1].sum()

def backward(obs_seq, A, B):
    N = A.shape[0]
    T = len(obs_seq)

    beta = np.zeros((N,T))
    beta[:,-1:] = 1

    for t in reversed(range(T-1)):
        for n in range(N):
            beta[n,t] = np.sum(beta[:,t+1] * A[n,:] * B[:, obs_seq[t+1]])

    return beta

def gamma(alpha, beta): #calculates posteriors
    obs_prob = likelihood(alpha)
    return (np.multiply(alpha,beta.T) / obs_prob)


states = ('N', 'I')
observations = ('A', 'C', 'G', 'T')
pi = np.array([0.5, 0.5])  #initial probability 
A = np.array([[0.3, 0.2, 0.2, 0.3],[0.1, 0.4, 0.4, 0.1]]) #Transmission probability 
B = np.array([[0.9, 0.1],[0.2,0.8]]) #Emission probability
seq = "TCATAATCTGGGGGTCGGCGCGGGGGGCCGGACGG"
tos = []
for i in range(len(seq)):
    if seq[i] == "A":
        tos.append(0)
    if seq[i] == "C":
        tos.append(1)
    if seq[i] == "T":
        tos.append(2)
    if seq[i] == "G":
        tos.append(3)

# print(tos)
input(tos)
tosses = np.array(tos) #THHH
decoded=viterbi(tosses)

print("Viterbi Decoding:", list(map(lambda y: states[y], decoded)))

alpha = forward(tosses, pi, A, B) #forward pass
print(alpha)
beta=backward(tosses, A, B) #backward pass
print(beta)
posterior = gamma(alpha, beta) #posterior probabilities (i.e. probability of hidden state at each toss)
print(posterior)
print("What is the 2nd probabilities of\n", states,'\n', posterior[1])
