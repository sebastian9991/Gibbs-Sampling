# Gibbs-Sampling
Method of approximation for variable elimination implemented in python

$$
\begin{align}
    P(A | B = b^{1}) 
    &= \frac{1}{Z}\sum_{DC}(\Phi_1(A,B) \Phi_2(B,C) \Phi_3(C, D) \Phi_4(D,A))\_{B = b^1} (Obs\\,B = b^{1})\\
    &= \frac{1}{Z}\sum\_{DC}((\Phi_1(A) \Phi_2(C) \Phi_3(C, D) \Phi_4(D,A))\_{B = b^1}(Elimination\\, Order\\, = C,D)\\
    &= \frac{1}{Z}(\Phi_1(A) \sum\_{D} \Phi_4(D,A)\sum_{C}\Phi_3(C,D) \Phi_2(C))(Sum\\, out\\,  C)\\
    &= \frac{1}{Z}(\Phi_1(A) \sum_{D} \Phi_4(D,A)\Phi_5(D))(Sum\\,out\\, D)\\
    &= \frac{1}{Z}(\Phi_1(A) \Phi_6(A))\\
    &\approx
\end{align}
$$

![image](https://github.com/sebastian9991/Gibbs-Sampling/assets/61892815/53620747-6544-44b9-9624-d1e49a506dc2)

## We show the process of the resulting factor tables: 

![image](https://github.com/sebastian9991/Gibbs-Sampling/assets/61892815/9aaf3901-af54-443f-b1a8-6e77d4d03bca)

![image](https://github.com/sebastian9991/Gibbs-Sampling/assets/61892815/9f5ee612-a6b7-425d-b691-5f231fb14fb0)

