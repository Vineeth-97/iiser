import numpy as np

N = 4

B = 0.5


def energy(N, conf):
    E_s = 0.0
    for i in range(N)-1:
        E_s += conf[i]*conf[i+1]
    E_s += conf[N-1]*conf[0]
    return E_s


def calculate(N, B):
    conf = []
    E_s = 0
    m_s = 0
    E = 0
    Z = 0
    m = 0
    for i in range(int(np.exp2(N))):
        k = i
        for j in range(N):
            # Generates all possible sequences containing + 1 and -1 and of size N
            conf[j] = (k % 2)*2 - 1
            k /= 2
            m_s += conf[j]

        E_s = energy(N, conf)
        m_s = 1.0*m_s/N  # Average magnetization is sum of each magnetic moment / number of sites

        E += E_s*1.0*np.exp(-1*B*E_s)
        # Numerator of average energy expression
        Z += 1.0*np.exp(-1*B*E_s)
        # Partition function calculation
        m += abs(m_s)*1.0*np.exp(-1*B*E_s)
        # Numerator of average absolute magnetization expression

        m_s = 0
        E_s = 0

    E /= Z
    m /= Z
    print(" Average Energy = ", E)
    print(" Average Magnetization = ", m)


calculate(N, B)
