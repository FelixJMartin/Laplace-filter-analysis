## Härledning av filteröverföringsfunktionen

I detta avsnitt härleds överföringsfunktionen mellan in- och utspänningsnivåerna i kretsen genom att använda impedansmetoden i Laplace-domänen.

### 2.1 Härledning med impedansmetoden
Överföringsfunktionen \(H(s)\) kan uttryckas som:
$$
H(s)=\frac{V_{\text{out}}(s)}{V_{\text{in}}(s)}
= \frac{s^{2} C L R + R}{s^{2} C L R + Ls + R}.
$$

### Step response (analytical)

Given the transfer function
$$
H(s)=\frac{s^{2} C L R + R}{s^{2} C L R + Ls + R},
$$
the unit–step input is \(U(s)=\frac{1}{s}\), so
$$
Y(s)=H(s)U(s)=\frac{1}{s}\,\frac{s^{2} C L R + R}{s^{2} C L R + Ls + R}.
$$

**Partial fractions:**  
\[
Y(s)=\frac{A}{s}+\frac{Bs+C}{s^{2} C L R + Ls + R}
\quad\Rightarrow\quad A=1,\; B=0,\; C=-L.
\]
Hence
$$
Y(s)=\frac{1}{s}-\frac{L}{s^{2} C L R + Ls + R}
     =\frac{1}{s}-\frac{1}{C R}\,\frac{1}{(s+\alpha)^2+\beta^2},
$$
with
\[
\alpha=\frac{1}{2CR},\qquad
\beta=\sqrt{\frac{1}{LC}-\frac{1}{(2CR)^2}}.
\]

**Inverse Laplace (step response):**
$$
\boxed{\;
y(t)=1-\frac{1}{CR\,\beta}\,e^{-\alpha t}\,\sin(\beta t),\qquad t\ge0.
\;}
$$

## Numerical values (example)
For \(L=50\,\text{mH}\), \(C=20\,\text{nF}\), \(R=5\,\text{k}\Omega\):
\[
\alpha=5000\ \text{s}^{-1},\quad
\beta=\sqrt{9.75\times10^{8}}\approx 31224.99\ \text{s}^{-1},\quad
\frac{1}{CR\beta}\approx 0.320256.
\]
So
\[
\boxed{\; y(t)=1-0.320256\,e^{-5000t}\,\sin(31224.99\,t)\;}\quad(\text{t in seconds}).
\]


