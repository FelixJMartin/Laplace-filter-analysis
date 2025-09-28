# TRANSFORM-METHODS
Analysis and simulation of a 2nd-order analog filter using Fourier/Laplace methods: derive  𝐻 ( 𝑠 ) H(s), step response, Bode plots, square-wave response, and validate against circuit simulation.


I analyze a linear second-order analog filter using Fourier and Laplace transforms: derive the transfer function 
𝐻
(
𝑠
)
, compute the closed-form step response and verify it numerically, generate Bode magnitude/phase plots, and evaluate the square-wave response via the first five Fourier harmonics. Results are validated against circuit simulation in LTspice. Code is in Python (scipy.signal, matplotlib).

![Filter diagram](assets/img/Filter.png)


### Task 1 — Transfer function (impedance method)

Replaced components with Laplace impedances $Z_R=R$, $Z_C=\tfrac{1}{sC}$, solved for $H(s)=\tfrac{V_{\text{out}}(s)}{V_{\text{in}}(s)}$; sanity-checked $H(0)$ and $\lim_{s\to\infty}H(s)$.


### Task 2 — Step Response

**Analytical:** Derived the step response from \(Y(s) = H(s)/s\) using inverse Laplace.  
**Plot:** Implemented and visualized the closed-form solution in Python (Matplotlib).  
**Verification:** Compared with SciPy’s `signal.step`; results matched well.  

### Task 3 — Bode Plot

**Computation:** Generated amplitude and phase diagrams of the filter using Python (SciPy/Matplotlib).  
**Analysis:** By visual inspection, the response shows low attenuation at low frequencies and strong attenuation at high frequencies.  
**Conclusion:** The filter is identified as a **low-pass filter**.

### Task 4 — Square Wave Input

**a. Fourier series:** Expanded the periodic square wave (0–1 V, period T₀) into its sine components using standard Fourier series.  
**b. Table:** Constructed a table for the first five nonzero terms with columns: input signal, frequency, gain, phase shift, and output signal.  
**Computation:** Gains and phase shifts were obtained from the frequency response (verified both via Bode plot and manual FRF calculation).  
**Result:** The table shows how the filter attenuates and phase-shifts each harmonic, illustrating the output as the filtered sum of harmonics.  

### Task 5 — Simulation Verification

**Method:** Implemented the filter circuit in a graphical simulator (LTspice / CircuitLab).  
**Comparison:** Simulated step response and Bode plot against analytical and numerical results from Tasks 3–4.  
**Result:** Simulation confirmed the earlier calculations, validating both amplitude/phase behavior and square wave output.  

