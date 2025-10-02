# TRANSFORM-METHODS
Analysis and simulation of a second-order analog filter using Fourier and Laplace methods. The project derives the transfer function $H(s)$, computes the analytical step response and verifies it numerically, generates Bode magnitude/phase plots, and evaluates the square-wave response using the first five Fourier harmonics. Results are validated against circuit simulation in LTspice, and all analysis is implemented in Python (`scipy.signal`, `matplotlib`).


![Filter diagram](assets/img/Filter.png)


### Task 1 — Transfer function (impedance method)

Replaced components with Laplace impedances $Z_R=R$, $Z_C=\tfrac{1}{sC}$, solved for $H(s)=\tfrac{V_{\text{out}}(s)}{V_{\text{in}}(s)}$;

### Task 2 — Step Response

**Analytical:** Derived the step response from $Y(s) = H(s)\*X(s)$ using inverse Laplace.  
**Plot:** Implemented and visualized the closed-form solution in Python (Matplotlib).  
**Verification:** Compared with SciPy’s `signal.step`; results matched well.  

### Task 3 — Bode Plot

**Computation:** Generated amplitude and phase diagrams of the filter using Python (`scipy.signal`, `matplotlib`).  
**Analysis:** The magnitude response shows a sharp attenuation around 5 kHz, while frequencies below and above this point pass with little loss.  
**Conclusion:** From the Bode diagram the filter is classified as a **notch filter**, suppressing signals at approximately 5 kHz.


### Task 4 — Square Wave Input

**a. Fourier series:** Expanded the periodic square wave (0–1 V, period T₀) into its sine components using standard Fourier series.  
**b. Table:** Constructed a table for the first five nonzero terms with columns: input signal, frequency, gain, phase shift, and output signal.  
**Computation:** Gains and phase shifts were obtained from the frequency response (verified both via Bode plot and manual FRF calculation).  
**Result:** The table shows how the filter attenuates and phase-shifts each harmonic, illustrating the output as the filtered sum of harmonics.  

### Task 5 — Simulation Verification

**Method:** Implemented the filter circuit in a graphical simulator (LTspice / CircuitLab).  
**Comparison:** Simulated step response and Bode plot against analytical and numerical results from Tasks 3–4.  
**Result:** Simulation confirmed the earlier calculations, validating both amplitude/phase behavior and square wave output.  

