# TRANSFORM-METHODS

Analysis and simulation of a second-order analog filter using Fourier and Laplace methods.  
The project derives the transfer function $H(s)$, computes the analytical step response, generates Bode magnitude/phase plots, and evaluates the square-wave response using the first five Fourier harmonics. Results are validated against circuit simulation in LTspice.  
All analysis is implemented in Python (`scipy.signal`, `matplotlib`).

![Filter diagram](assets/img/Filter.png)

---

### Task 1 — Transfer function (impedance method)
- Replace components with Laplace impedances $Z_R=R$, $Z_C=\tfrac{1}{sC}$.  
- Derive the transfer function $H(s)=\tfrac{V_{\text{out}}(s)}{V_{\text{in}}(s)}$.  

### Task 2 — Step Response
- Derive the step response from $Y(s) = H(s)\*X(s)$ using inverse Laplace.  
- Implement and visualize the closed-form solution in Python.  
- Verify by comparing with SciPy’s `signal.step`.  

### Task 3 — Bode Plot
- Generate amplitude and phase diagrams of the filter using Python.  
- Analyze the filter type based on the Bode response.  

### Task 4 — Square Wave Input
- Expand the periodic square wave (0–1 V, period $T_0$) into a Fourier series.  
- Construct a table for the first five nonzero terms (input signal, frequency, gain, phase shift, output signal).  
- Compute gains and phase shifts from the frequency response.  

### Task 5 — Simulation Verification
- Implement the filter circuit in a graphical simulator (LTspice / CircuitLab).  
- Compare simulated step response and Bode plot with analytical and numerical results.  


