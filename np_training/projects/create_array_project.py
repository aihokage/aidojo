import numpy as np

if __name__ == '__main__':
    A = np.zeros(shape=(5, 5, 5))
    for i in range(5):
        A[i, i, i] = 1
    print(A)
    print()

    # ----

    B = np.ones(shape=(3, 2))
    print(B)
    print()

    # ----

    C = np.full(shape=(2, 5), fill_value=6)
    print(C)
    print()

    # ----

    D = np.arange(5, 101 + 1, 8)
    print(D)
    print()

    # ----

    E = np.linspace(7, 12, 20)
    print(E)
    print()

    # ----

    F = np.zeros(shape=(4, 4))
    for i in range(4):
        F[i, i] = i + 1
    print(F)
    print()

    # ----

    G = np.ones(shape=(10, 10, 3)).reshape((2, 150))
    print(G)
    print()

    # ----

    H = np.array([[1, 2, 3], [4, 5, 6]]).reshape((6,))
    print(H)
    print()

    # ----

    J = np.arange(1, 5).reshape((2, 2))
    print(int(np.linalg.det(J)))
    print()

    # ----

    K = np.linspace(2, 16, 16).reshape(4, 4)
    print(K.trace())
    print()

    # ----

    L = np.array([[1., 2.], [3., 4.]])
    print(np.linalg.inv(L))
    print()

    # ----

    M = np.array([4, 5, 6, 13])
    N = np.array([5, 0, 6, 11])

    assert len(M) == len(N)
    for i in range(len(M)):
        if M[i] > N[i]:
            print(f'Element {M[i]} greater than element {N[i]} at position {i}')
