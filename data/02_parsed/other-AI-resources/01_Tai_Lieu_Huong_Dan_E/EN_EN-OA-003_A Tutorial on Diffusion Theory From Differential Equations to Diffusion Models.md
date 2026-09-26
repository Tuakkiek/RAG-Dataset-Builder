<!-- page: 1 -->

# A Tutorial on Diffusion Theory: From Differential Equations to Diffusion Models

Jiayi Fu, Yuxia Wang

INSAIT, Sofia University "St. Kliment Ohridski", Bulgaria

jiayi.fu@insait.ai, yuxia.wang@insait.ai

**Abstract**

Diffusion models have emerged as a dominant framework for generative modeling, but their mathematical foundations are often presented separately through diffusion probabilistic models, score-based modeling, stochastic differential equations, and numerical sampling methods. We write this tutorial to provide a unified and self-contained account of these viewpoints from the perspective of differential equations. Starting from a conditional Gaussian noising process, we derive ordinary differential equation (ODE) and stochastic differential equation (SDE) representations, pass to the corresponding marginal forward dynamics, and then obtain the reverse-time SDE and probability-flow ODE that make generation possible. We show that the central unknown quantity in reverse sampling is the marginal score, explain how score matching becomes the standard denoising objective under a noise-prediction parameterization, and discuss practical reverse-time sampling and guidance. We further place DDPM, DDIM, flow matching, and score-based SDEs in a common framework, and conclude with diffusion language models in continuous embedding space together with a brief discussion of discrete masked-token diffusion. The tutorial is intended as a bridge between the analytical foundations of diffusion processes and the modern generative algorithms built upon them.

## Contents

Introduction 3

Setup 3

1 Conditional Forward Process 4

1.1 Conditional Gaussian forward path . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

1.2 Conditional ODE that generates the conditional forward process . . . . . . . . . . . 5

1.3 Conditional SDE that generates the conditional forward process . . . . . . . . . . . . 7

2 Marginalized Forward Process 9

2.1 Marginalized forward path . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.2 Marginalized ODE that generates the marginalized forward process . . . . . . . . . . 9

2.3 Marginalized SDE that generates the marginalized forward process . . . . . . . . . . 10

3 Reverse Process and Reverse Dynamics 11

3.1 Definition of the reverse process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3.2 Reverse density equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3.3 Reverse SDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3.4 Reverse probability-flow ODE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

1

arXiv:2605.22586v3 [cs.LG] 27 May 2026

<!-- page: 2 -->

4 Learning the Score for Reverse Sampling 14

4.1 The unknown part of the reverse ODE and reverse SDE . . . . . . . . . . . . . . . . 14

4.2 A neural score model and score matching . . . . . . . . . . . . . . . . . . . . . . . . 14

4.3 The score as a conditional expectation of the forward noise . . . . . . . . . . . . . . 14

4.4 Reparameterizing the score model as a noise predictor . . . . . . . . . . . . . . . . . 15

4.5 The learned reverse SDE and reverse ODE . . . . . . . . . . . . . . . . . . . . . . . . 16

5 Sampling from the Reverse ODE and SDE 17

5.1 Terminal distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

5.2 Basic reverse SDE sampler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

5.3 Basic reverse ODE sampler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

5.4 Fast sampling in the style of DPM-Solver . . . . . . . . . . . . . . . . . . . . . . . . 18

6 Guided Diffusion 20

6.1 Classifier guidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

6.2 Classifier-free guidance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

7 Unifying DDPM, DDIM in the Reverse ODE/SDE Framework 23

7.1 Continuizing the DDPM forward process and constructing its SDE . . . . . . . . . . 23

7.2 DDPM training and its relation to the reverse SDE loss . . . . . . . . . . . . . . . . 27

7.3 DDPM inference and its relation to the reverse SDE . . . . . . . . . . . . . . . . . . 29

7.4 DDIM inference and its relation to the reverse ODE . . . . . . . . . . . . . . . . . . 35

8 Comparison with Flow Matching and Score-Based SDEs 38

8.1 Flow models, flow matching, diffusion models, and score matching . . . . . . . . . . 38

8.2 Comparison with *Flow Matching for Generative Modeling* . . . . . . . . . . . . . . . 38

8.3 Comparison with *Score-Based Generative Modeling through Stochastic Differential Equations* . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

9 Diffusion Language Models in Continuous Embedding Space 46

9.1 Prompt-Response Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

9.2 Training Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

9.3 Inference by DDIM-Stochastic Rollout . . . . . . . . . . . . . . . . . . . . . . . . . . 48

9.4 Connection to the Reverse ODE/SDE Framework . . . . . . . . . . . . . . . . . . . . 49

9.5 A Brief Note on Discrete Diffusion LLMs . . . . . . . . . . . . . . . . . . . . . . . . 51

A Differential Operators 52

B Brownian Motion in Forward and Reverse Time 52

C Deterministic ItĂ´ Integrals and ItĂ´ Isometry 56

D Continuity Equation 60

E Fokkerâ€“Planck Equation 61

F Conditional-to-Marginal Averaging Lemmas 62

G Fisher's Identity 63

2

<!-- page: 3 -->

H Orthogonality Identity Used in the Denoising Loss 64

References 65

## Introduction

Diffusion models now occupy a central position in modern generative modeling. Their contemporary development combines the diffusion-probabilistic line initiated by nonequilibrium thermodynamics and latent-variable learning [24, 6, 18, 11] with the score-based line built on score matching and denoising score matching [9, 30, 26, 27, 28]. These ideas have supported a broad range of influential generative systems, including methods for large-scale image synthesis, guidance, editing, and latent-space generation [4, 7, 17, 16, 21, 22].

Despite this success, the literature remains technically fragmented. Reverse-time diffusion theory is often discussed through stochastic calculus and Fokkerâ€“Planck equations [1, 19, 20]; deterministic probability-flow viewpoints are frequently introduced through DDIM and modern ODE solvers [25, 14, 15, 10, 23]; and recent unifying perspectives connect diffusion to neural ODEs and flow matching [3, 13, 8]. As a result, readers often encounter DDPM, score-based SDEs, reverse ODEs, flow matching, and noise-prediction losses as distinct constructions, even though they are closely related mathematically. This tutorial is written to make those relationships explicit within a single, coherent narrative.

The main body of the tutorial starts from the conditional Gaussian forward process and derives its ODE and SDE representations before passing to the corresponding marginal dynamics. We then show how reverse-time sampling arises from the reverse SDE and the probability-flow ODE, and why the marginal score \(\nabla \log p_t(x)\) is the central unknown quantity that must be learned. This viewpoint leads naturally to score matching, to the denoising objective used in practical diffusion models, and to a unified interpretation of DDPM and DDIM as discretizations of reverse-time continuous dynamics. We also discuss guided generation and fast sampling from the reverse equations.

A second goal is to position diffusion models within neighboring generative frameworks. Accordingly, we compare the reverse-time presentation used in the main text with the generative-time formulations of flow matching and score-based SDE modeling [13, 28]. We then show how the same continuous-state formalism extends to diffusion language models in embedding space [12, 29, 5], while briefly situating discrete masked-token diffusion models [2] outside the main scope of the tutorial. The appendices collect the analytical tools used throughout, including differential operators, Brownian motion under time reversal, continuity and Fokkerâ€“Planck equations, Fisher's identity, and the orthogonality argument behind the denoising loss.

## Setup

Let \(X_0 \in \mathbb{R}^d\) be a data-valued random variable with density \(p_0(x_0)\), and let \(t \in [0, 1]\) denote forward time. Throughout the main development, we assume that the noising schedules \(\alpha_t\) and \(\sigma_t\) are differentiable functions of \(t\) satisfying

$$
\alpha_0 = 1, \quad \alpha_1 = 0, \quad \sigma_0 = 0, \quad \sigma_1 = 1, \qquad \alpha_t \geq 0, \ \sigma_t \geq 0 \text{ for all } t \in [0, 1],
$$

and that the induced diffusion coefficient is nonnegative:

$$
\frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 - 2\frac{\dot{\alpha}_t}{\alpha_t}\sigma_t^2 \geq 0.
$$

3

<!-- page: 4 -->

Typically, \(\alpha_t\) decreases while \(\sigma_t\) increases, so that the forward process progressively corrupts the data and terminates at Gaussian noise. We then define

$$
f_t := \frac{\dot{\alpha}_t}{\alpha_t}, \qquad g_t^2 := \frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 - 2\frac{\dot{\alpha}_t}{\alpha_t}\sigma_t^2. \tag{1}
$$

The conditional Gaussian forward kernel is

$$
p_t(x \mid x_0) := \mathcal{N}(x; \alpha_t x_0, \sigma_t^2 I), \tag{2}
$$

and the corresponding marginal forward density is

$$
p_t(x) := \int_{\mathbb{R}^d} p_t(x \mid x_0) p_0(x_0) \,\mathrm{d}x_0. \tag{3}
$$

To describe reverse-time dynamics, we introduce the reverse-time variable

$$
\tau := 1 - t, \tag{4}
$$

and define the reverse process by

$$
Y_\tau := X_{1-\tau}. \tag{5}
$$

Its density is

$$
q_\tau(x) := p_{1-\tau}(x). \tag{6}
$$

Unless explicitly stated otherwise, all gradients, divergences, and Laplacians are taken with respect to the state variable. We write \(W_t\) for a standard Brownian motion when an SDE is expressed in forward time \(t\). When the reverse SDE is written in the reverse-time variable \(\tau\), its driving Brownian motion is denoted by \(W_\tau^{\mathrm{rev}}\). When the same reverse SDE is written using the original label \(t : 1 \to 0\), we denote the corresponding reverse-time Brownian motion by \(\bar{W}_t\), where

$$
\bar{W}_t := W_{1-t}^{\mathrm{rev}}.
$$

Thus \(W_\tau^{\mathrm{rev}}\) and \(\bar{W}_t\) represent the same reverse-time noise under two different time parametrizations. Appendix B gives a detailed discussion.

## 1 Conditional Forward Process

### 1.1 Conditional Gaussian forward path

The conditional forward process is the family of random variables

$$
X_t \mid X_0 = x_0, \qquad 0 \leq t \leq 1,
$$

whose density path is prescribed by the Gaussian kernel (2). Equivalently, if \(\varepsilon \sim \mathcal{N}(0, I)\), then

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon \tag{7}
$$

has conditional law

$$
X_t \mid X_0 = x_0 \sim p_t(\cdot \mid x_0).
$$

**Proposition 1.1** (Conditional score). *The score of the conditional Gaussian path is*

$$
\nabla \log p_t(x \mid x_0) = -\frac{x - \alpha_t x_0}{\sigma_t^2}. \tag{8}
$$

*Proof.* Since

$$
\log p_t(x \mid x_0) = C_t - \frac{1}{2\sigma_t^2}\|x - \alpha_t x_0\|_2^2,
$$

where \(C_t\) is independent of \(x\), differentiating with respect to \(x\) gives (8). â–¡

4

<!-- page: 5 -->

[FIGURE: Figure 1: Conditional forward process.]

Text in figure:

- \(X_{t_0}\)
- \(X_{t_n}\)
- \(X_{t_{n+1}}\)
- \(X_{t_N}\)
- ODE : \(X_{t_{n+1}} = X_{t_n} + u_{t_n}(X_{t_n} \mid x_0) \cdot (t_{n+1} - t_n)\)
- SDE : \(X_{t_{n+1}} = X_{t_n} + f_{t_n} X_{t_n} \cdot (t_{n+1} - t_n) + g_{t_n} z\)

Figure 1: Conditional forward process. Given a time grid \(0 = t_0 < \cdots < t_n < t_{n+1} < \cdots < t_N = 1\) and an initial clean sample \(X_0\), the forward Gaussian path progressively corrupts the sample. The same path may be viewed either as repeated Gaussian perturbation on the grid or as the solution of the conditional forward ODE/SDE, where \(z \sim \mathcal{N}(0, (t_{n+1} - t_n)I)\). The terminal state is approximately pure Gaussian noise.

### 1.2 Conditional ODE that generates the conditional forward process

**Theorem 1.2** (Conditional forward ODE). *For every fixed \(x_0\), the conditional Gaussian path (2) is generated by the ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_t(X_t \mid x_0), \tag{9}
$$

*with velocity field*

$$
u_t(x \mid x_0) := \left(\dot{\alpha}_t - \frac{\dot{\sigma}_t}{\sigma_t}\alpha_t\right)x_0 + \frac{\dot{\sigma}_t}{\sigma_t}x. \tag{10}
$$

*Equivalently, the conditional density satisfies the conditional continuity equation*

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \big(p_t(x \mid x_0) u_t(x \mid x_0)\big). \tag{11}
$$

*Proof.* Fix \(x_0\) and define

$$
r_t(x) := x - \alpha_t x_0.
$$

From (7),

$$
X_t = \alpha_t x_0 + \sigma_t \varepsilon.
$$

Differentiating with respect to \(t\) gives

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = \dot{\alpha}_t x_0 + \dot{\sigma}_t \varepsilon = \dot{\alpha}_t x_0 + \dot{\sigma}_t \frac{X_t - \alpha_t x_0}{\sigma_t},
$$

which simplifies to (10). Thus the ODE (9) indeed generates the conditional Gaussian path.

We now verify (11) by exact algebra. Since

$$
p_t(x \mid x_0) = \frac{1}{(2\pi\sigma_t^2)^{d/2}}\exp\left(-\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right),
$$

we have

$$
\log p_t(x \mid x_0) = -\frac{d}{2}\log(2\pi\sigma_t^2) - \frac{\|r_t(x)\|_2^2}{2\sigma_t^2}.
$$

Because

$$
\partial_t r_t(x) = -\dot{\alpha}_t x_0, \qquad \partial_t \|r_t(x)\|_2^2 = -2\dot{\alpha}_t r_t(x)^\top x_0,
$$

5

<!-- page: 6 -->

we obtain

$$
\begin{aligned}
\partial_t \log p_t(x \mid x_0) &= -d\frac{\dot{\sigma}_t}{\sigma_t} - \partial_t\left(\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right)\\
&= -d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2.
\end{aligned}
$$

Therefore

$$
\partial_t p_t(x \mid x_0) = p_t(x \mid x_0)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right]. \tag{12}
$$

Next,

$$
\nabla p_t(x \mid x_0) = p_t(x \mid x_0)\nabla \log p_t(x \mid x_0) = -p_t(x \mid x_0)\frac{r_t(x)}{\sigma_t^2}.
$$

Since

$$
u_t(x \mid x_0) = \dot{\alpha}_t x_0 + \frac{\dot{\sigma}_t}{\sigma_t}r_t(x),
$$

we get

$$
u_t(x \mid x_0)^\top \nabla p_t(x \mid x_0) = -p_t(x \mid x_0)\left[\frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right].
$$

Also,

$$
\nabla \cdot u_t(x \mid x_0) = \frac{\dot{\sigma}_t}{\sigma_t}\nabla \cdot r_t(x) = d\frac{\dot{\sigma}_t}{\sigma_t},
$$

because \(r_t(x) = x - \alpha_t x_0\) and \(\nabla \cdot x = d\). Hence

$$
\begin{aligned}
\nabla \cdot \big(p_t(x \mid x_0)u_t(x \mid x_0)\big) &= u_t(x \mid x_0)^\top \nabla p_t(x \mid x_0) + p_t(x \mid x_0)\nabla \cdot u_t(x \mid x_0)\\
&= p_t(x \mid x_0)\left[-\frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 - \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2 + d\frac{\dot{\sigma}_t}{\sigma_t}\right].
\end{aligned}
$$

Therefore

$$
-\nabla \cdot \big(p_t(x \mid x_0)u_t(x \mid x_0)\big) = p_t(x \mid x_0)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right]. \tag{13}
$$

Comparing (12) and (13) proves (11). â–¡

**Lemma 1.3** (Score form of the conditional forward velocity). *The velocity field (10) can be rewritten as*

$$
u_t(x \mid x_0) = f_t x - \frac{1}{2}g_t^2 \nabla \log p_t(x \mid x_0). \tag{14}
$$

*Proof.* By (8),

$$
-\frac{1}{2}g_t^2 \nabla \log p_t(x \mid x_0) = \frac{g_t^2}{2\sigma_t^2}(x - \alpha_t x_0).
$$

Using (1),

$$
g_t^2 = \frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 - 2f_t\sigma_t^2 = 2\sigma_t\dot{\sigma}_t - 2f_t\sigma_t^2,
$$

so

$$
\frac{g_t^2}{2\sigma_t^2} = \frac{\dot{\sigma}_t}{\sigma_t} - f_t.
$$

6

<!-- page: 7 -->

Therefore

$$
\begin{aligned}
f_t x - \frac{1}{2}g_t^2 \nabla \log p_t(x \mid x_0) &= f_t x + \left(\frac{\dot{\sigma}_t}{\sigma_t} - f_t\right)(x - \alpha_t x_0)\\
&= \frac{\dot{\sigma}_t}{\sigma_t}x + \left(\dot{\alpha}_t - \frac{\dot{\sigma}_t}{\sigma_t}\alpha_t\right)x_0\\
&= u_t(x \mid x_0). \qquad \square
\end{aligned}
$$

### 1.3 Conditional SDE that generates the conditional forward process

**Theorem 1.4** (Conditional forward SDE). *For every fixed \(x_0\), the SDE*

$$
\mathrm{d}X_t = f_t X_t \,\mathrm{d}t + g_t \,\mathrm{d}W_t, \qquad X_0 = x_0, \tag{15}
$$

*has conditional density path (2). Equivalently, the density (2) satisfies the conditional Fokkerâ€“Planck equation*

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big) + \frac{1}{2}g_t^2 \Delta p_t(x \mid x_0). \tag{16}
$$

*Proof.* We keep the notation \(r_t(x) = x - \alpha_t x_0\). From the previous proof,

$$
\partial_t p_t(x \mid x_0) = p_t(x \mid x_0)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right]. \tag{17}
$$

We now compute the right-hand side of (16). First,

$$
\nabla p_t(x \mid x_0) = -p_t(x \mid x_0)\frac{r_t(x)}{\sigma_t^2}.
$$

Hence

$$
\begin{aligned}
\Delta p_t(x \mid x_0) &= \nabla \cdot \left(-p_t(x \mid x_0)\frac{r_t(x)}{\sigma_t^2}\right)\\
&= -\frac{1}{\sigma_t^2}\left(r_t(x)^\top \nabla p_t(x \mid x_0) + p_t(x \mid x_0)\nabla \cdot r_t(x)\right)\\
&= -\frac{1}{\sigma_t^2}\left(-p_t(x \mid x_0)\frac{\|r_t(x)\|_2^2}{\sigma_t^2} + d\, p_t(x \mid x_0)\right)\\
&= p_t(x \mid x_0)\left(\frac{\|r_t(x)\|_2^2}{\sigma_t^4} - \frac{d}{\sigma_t^2}\right).
\end{aligned}
$$

Next,

$$
\begin{aligned}
\nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big) &= f_t \nabla \cdot \big(x\, p_t(x \mid x_0)\big)\\
&= f_t\left(d\, p_t(x \mid x_0) + x^\top \nabla p_t(x \mid x_0)\right)\\
&= f_t d\, p_t(x \mid x_0) - f_t p_t(x \mid x_0)\frac{x^\top r_t(x)}{\sigma_t^2}.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
&-\nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big) + \frac{1}{2}g_t^2\Delta p_t(x \mid x_0)\\
&\quad = p_t(x \mid x_0)\left[-f_t d + f_t\frac{x^\top r_t(x)}{\sigma_t^2} + \frac{g_t^2}{2}\left(\frac{\|r_t(x)\|_2^2}{\sigma_t^4} - \frac{d}{\sigma_t^2}\right)\right].
\end{aligned}
$$

7

<!-- page: 8 -->

Because \(x = r_t(x) + \alpha_t x_0\),

$$
x^\top r_t(x) = \|r_t(x)\|_2^2 + \alpha_t x_0^\top r_t(x).
$$

Also \(f_t \alpha_t = \dot{\alpha}_t\), and

$$
\frac{g_t^2}{2\sigma_t^2} = \frac{\dot{\sigma}_t}{\sigma_t} - f_t, \qquad \frac{g_t^2}{2\sigma_t^4} = \frac{\dot{\sigma}_t}{\sigma_t^3} - \frac{f_t}{\sigma_t^2}.
$$

Substituting these identities yields

$$
\begin{aligned}
&-\nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big) + \frac{1}{2}g_t^2\Delta p_t(x \mid x_0)\\
&\quad = p_t(x \mid x_0)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_0 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right].
\end{aligned}
$$

This matches (17), so (16) holds exactly. â–¡

8

<!-- page: 9 -->

## 2 Marginalized Forward Process

### 2.1 Marginalized forward path

The marginalized forward process is the unconditional family \((X_t)_{0 \leq t \leq 1}\) with density path

$$
p_t(x) = \int p_t(x \mid x_0)p_0(x_0) \,\mathrm{d}x_0. \tag{18}
$$

Because the conditional kernels are Gaussian, \(p_t\) is a Gaussian mixture induced by the data distribution \(p_0\). In general \(p_t\) is not itself Gaussian unless \(p_0\) is Gaussian.

[FIGURE: Figure 2: Marginalized forward process]

Text in figure:

- \(X_{t_0}\)
- \(X_{t_n}\)
- \(X_{t_{n+1}}\)
- \(X_{t_N}\)
- ODE : \(X_{t_{n+1}} = X_{t_n} + u_{t_n}(X_{t_n}) \cdot (t_{n+1} - t_n)\)
- SDE : \(X_{t_{n+1}} = X_{t_n} + f_{t_n} X_{t_n} \cdot (t_{n+1} - t_n) + g_{t_n} z\)

Figure 2: Marginalized forward process: Create a time grid \(0 = t_0 < \cdots < t_n < t_{n+1} < \cdots < t_N = 1\). The initial clean image \(X_0\) is drawn from the data distribution \(p_0\), and the marginal forward ODE/SDE progressively transform the data distribution to Gaussian noise distribution. Where \(z \sim \mathcal{N}(0, (t_{n+1} - t_n)I)\).

### 2.2 Marginalized ODE that generates the marginalized forward process

**Theorem 2.1** (Marginalized forward ODE). *The marginal path 18 is generated by the ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_t(X_t), \tag{19}
$$

*with velocity field*

$$
u_t(x) := \mathbb{E}[u_t(x \mid X_0) \mid X_t = x] = f_t x - \frac{1}{2}g_t^2 \nabla \log p_t(x). \tag{20}
$$

*or equivalently, and the marginal density path satisfies marginal continuity equation*

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)u_t(x)\big). \tag{21}
$$

*Proof.* Starting from the conditional score form (14),

$$
u_t(x \mid X_0) = f_t x - \frac{1}{2}g_t^2 \nabla \log p_t(x \mid X_0).
$$

Conditioning on \(X_t = x\) yields

$$
\begin{aligned}
u_t(x) &= \mathbb{E}[u_t(x \mid X_0) \mid X_t = x]\\
&= f_t x - \frac{1}{2}g_t^2 \mathbb{E}[\nabla \log p_t(x \mid X_0) \mid X_t = x].
\end{aligned}
$$

9

<!-- page: 10 -->

By Fisher's identity, proved in Appendix G,

$$
\mathbb{E}[\nabla \log p_t(x \mid X_0) \mid X_t = x] = \nabla \log p_t(x),
$$

which gives (20).

We now verify the continuity equation directly by averaging the conditional continuity equations:

$$
\begin{aligned}
\partial_t p_t(x) &= \int \partial_t p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\\
&= -\int \nabla \cdot \big(p_t(x \mid x_0)u_t(x \mid x_0)\big)p_0(x_0)\,\mathrm{d}x_0\\
&= -\nabla \cdot \left(\int p_t(x \mid x_0)u_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\right).
\end{aligned}
$$

By the definition (20),

$$
\int p_t(x \mid x_0)u_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0 = p_t(x)u_t(x).
$$

Therefore (21) holds. â–¡

### 2.3 Marginalized SDE that generates the marginalized forward process

**Theorem 2.2** (Marginalized forward SDE). *The marginal forward process is also generated by the SDE*

$$
\mathrm{d}X_t = f_t X_t \,\mathrm{d}t + g_t \,\mathrm{d}W_t, \qquad X_0 \sim p_0. \tag{22}
$$

*Equivalently, the marginal density path satisfies the marginal Fokkerâ€“Planck equation*

$$
\partial_t p_t(x) = -\nabla \cdot \big(f_t x\, p_t(x)\big) + \frac{1}{2}g_t^2 \Delta p_t(x). \tag{23}
$$

*Proof.* For every fixed \(x_0\), Theorem 1.4 gives

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big) + \frac{1}{2}g_t^2 \Delta p_t(x \mid x_0).
$$

Integrating both sides against \(p_0(x_0)\,\mathrm{d}x_0\) gives

$$
\begin{aligned}
\partial_t p_t(x) &= -\int \nabla \cdot \big(f_t x\, p_t(x \mid x_0)\big)p_0(x_0)\,\mathrm{d}x_0 + \frac{1}{2}g_t^2\int \Delta p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\\
&= -\nabla \cdot \left(f_t x \int p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\right) + \frac{1}{2}g_t^2\Delta\left(\int p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\right)\\
&= -\nabla \cdot \big(f_t x\, p_t(x)\big) + \frac{1}{2}g_t^2\Delta p_t(x).
\end{aligned}
$$

This is exactly (23), the Fokkerâ€“Planck equation of (22). â–¡

*Remark* 2.3 (From here on). After Section 2 we work only with the marginal process \(X_t\), the marginal density path \(p_t\), and their reverse-time counterparts. This is the level at which practical diffusion models are trained and sampled.

10

<!-- page: 11 -->

## 3 Reverse Process and Reverse Dynamics

### 3.1 Definition of the reverse process

**Definition 3.1** (Reverse process). *Given the forward marginal process \((X_t)_{0 \leq t \leq 1}\), the reverse process is*

$$
Y_\tau := X_{1-\tau}, \qquad 0 \leq \tau \leq 1. \tag{24}
$$

*Its density is*

$$
q_\tau(x) := p_{1-\tau}(x). \tag{25}
$$

[FIGURE: Figure 3: (Marginalized) Reverse process]

Text in figure:

- \(X_{t_0}\)
- \(X_{t_{n-1}}\)
- \(X_{t_n}\)
- \(X_{t_N}\)
- Reverse ODE : \(X_{t_{n-1}} = X_{t_n} - \left[f_{t_n} X_{t_n} + \dfrac{g_{t_n}^2}{2\sigma_{t_n}}\epsilon_\theta(X_{t_n}, t_n)\right]\Delta t_n\)
- Reverse SDE : \(X_{t_{n-1}} = X_{t_n} - \left[f_{t_n} X_{t_n} + \dfrac{g_{t_n}^2}{\sigma_{t_n}}\epsilon_\theta(X_{t_n}, t_n)\right]\Delta t_n + g_{t_n} z\)

Figure 3: (Marginalized) Reverse process: Create a time grid \(1 = t_N > \cdots > t_n > t_{n-1} > \cdots > t_0 = 0\). The initial noise \(X_1\) is drawn from the Gaussian distribution \(p_1\), and the marginal reverse ODE/SDE progressively transform the Gaussian distribution to data distribution. Where \(z \sim \mathcal{N}(0, (t_n - t_{n-1})I)\).

### 3.2 Reverse density equation

**Proposition 3.2** (PDE for the reverse density path). *The reverse density \(q_\tau\) satisfies*

$$
\partial_\tau q_\tau(x) = \nabla \cdot \big(f_{1-\tau}x\, q_\tau(x)\big) - \frac{1}{2}g_{1-\tau}^2 \Delta q_\tau(x). \tag{26}
$$

*Proof.* Since \(q_\tau(x) = p_{1-\tau}(x)\),

$$
\partial_\tau q_\tau(x) = -\partial_t p_t(x)\big|_{t=1-\tau}.
$$

Using the forward marginal Fokkerâ€“Planck equation (23),

$$
\partial_t p_t(x) = -\nabla \cdot \big(f_t x\, p_t(x)\big) + \frac{1}{2}g_t^2 \Delta p_t(x),
$$

we obtain

$$
\partial_\tau q_\tau(x) = \nabla \cdot \big(f_{1-\tau}x\, q_\tau(x)\big) - \frac{1}{2}g_{1-\tau}^2 \Delta q_\tau(x). \qquad \square
$$

11

<!-- page: 12 -->

### 3.3 Reverse SDE

The reverse-time diffusion viewpoint used below is classical in stochastic analysis [1] and underlies the modern reverse-SDE formulation of score-based generative modeling [28].

**Theorem 3.3** (Reverse SDE in \(\tau\)). *Define*

$$
b_\tau^{\mathrm{rev}}(x) := -f_{1-\tau}x + g_{1-\tau}^2 \nabla \log q_\tau(x). \tag{27}
$$

*Then the SDE*

$$
\mathrm{d}Y_\tau = b_\tau^{\mathrm{rev}}(Y_\tau)\,\mathrm{d}\tau + g_{1-\tau}\,\mathrm{d}W_\tau^{\mathrm{rev}}, \qquad Y_0 \sim q_0 = p_1, \tag{28}
$$

*has density path \(q_\tau\).*

*Proof.* We claim that \(q_\tau\) satisfies the Fokkerâ€“Planck equation

$$
\partial_\tau q_\tau(x) = -\nabla \cdot \big(b_\tau^{\mathrm{rev}}(x)q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x).
$$

Substitute (27):

$$
\begin{aligned}
&-\nabla \cdot \big(b_\tau^{\mathrm{rev}}(x)q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x)\\
&\quad = -\nabla \cdot \left(\left[-f_{1-\tau}x + g_{1-\tau}^2\nabla \log q_\tau(x)\right]q_\tau(x)\right) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x)\\
&\quad = \nabla \cdot \big(f_{1-\tau}x\, q_\tau(x)\big) - g_{1-\tau}^2\nabla \cdot \big(q_\tau(x)\nabla \log q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x).
\end{aligned}
$$

Since \(q_\tau \nabla \log q_\tau = \nabla q_\tau\), we have

$$
\nabla \cdot \big(q_\tau(x)\nabla \log q_\tau(x)\big) = \Delta q_\tau(x).
$$

Hence

$$
-\nabla \cdot \big(b_\tau^{\mathrm{rev}}(x)q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x) = \nabla \cdot \big(f_{1-\tau}x\, q_\tau(x)\big) - \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x),
$$

which is exactly (26). Therefore \(q_\tau\) satisfies the Fokkerâ€“Planck equation â–¡

**Corollary 3.4** (Reverse SDE written in the original time label). *Rewriting (28) in the original time label \(t\) gives*

$$
\mathrm{d}X_t = \left(f_t X_t - g_t^2 \nabla \log p_t(X_t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0, \qquad X_1 \sim p_1 \tag{29}
$$

*Proof.* Set \(\tau = 1 - t\) and \(Y_\tau = X_t\). Then \(q_\tau = p_t\), and the drift (27) becomes

$$
b_\tau^{\mathrm{rev}}(x) = -f_t x + g_t^2 \nabla \log p_t(x).
$$

Writing the same diffusion in backward \(t\) notation gives (29). â–¡

12

<!-- page: 13 -->

### 3.4 Reverse probability-flow ODE

**Theorem 3.5** (Reverse ODE in \(\tau\)). *The ODE*

$$
\frac{\mathrm{d}Y_\tau}{\mathrm{d}\tau} = -f_{1-\tau}Y_\tau + \frac{1}{2}g_{1-\tau}^2\nabla \log q_\tau(Y_\tau), \qquad Y_0 \sim q_0 = p_1, \tag{30}
$$

*has the same density path \(q_\tau\) as the reverse SDE.*

*Proof.* From the reverse SDE proof,

$$
\partial_\tau q_\tau(x) = -\nabla \cdot \big(b_\tau^{\mathrm{rev}}(x)q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\Delta q_\tau(x),
$$

where \(b_\tau^{\mathrm{rev}}(x) = -f_{1-\tau}x + g_{1-\tau}^2\nabla \log q_\tau(x)\). Since

$$
\Delta q_\tau(x) = \nabla \cdot \big(q_\tau(x)\nabla \log q_\tau(x)\big),
$$

we can rewrite the right-hand side as

$$
\begin{aligned}
\partial_\tau q_\tau(x) &= -\nabla \cdot \big(b_\tau^{\mathrm{rev}}(x)q_\tau(x)\big) + \frac{1}{2}g_{1-\tau}^2\nabla \cdot \big(q_\tau(x)\nabla \log q_\tau(x)\big)\\
&= -\nabla \cdot \left(q_\tau(x)\left[b_\tau^{\mathrm{rev}}(x) - \frac{1}{2}g_{1-\tau}^2\nabla \log q_\tau(x)\right]\right).
\end{aligned}
$$

Substituting the expression for \(b_\tau^{\mathrm{rev}}\) yields

$$
\partial_\tau q_\tau(x) = -\nabla \cdot \left(q_\tau(x)\left[-f_{1-\tau}x + \frac{1}{2}g_{1-\tau}^2\nabla \log q_\tau(x)\right]\right),
$$

which is precisely the continuity equation of (30). â–¡

**Corollary 3.6** (Reverse ODE written in the original time label). *Rewriting (30) in backward \(t\) notation gives*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t - \frac{1}{2}g_t^2\nabla \log p_t(X_t), \qquad t : 1 \to 0, \qquad X_1 \sim p_1 \tag{31}
$$

*Proof.* As before, use \(\tau = 1 - t\), \(Y_\tau = X_t\), and \(q_\tau = p_t\). Since

$$
\frac{\mathrm{d}Y_\tau}{\mathrm{d}\tau} = -\frac{\mathrm{d}X_t}{\mathrm{d}t},
$$

equation (30) becomes

$$
-\frac{\mathrm{d}X_t}{\mathrm{d}t} = -f_t X_t + \frac{1}{2}g_t^2\nabla \log p_t(X_t),
$$

which is equivalent to (31). â–¡

*Remark* 3.7 (Important distinction). The reverse ODE shares the same one-time density path as the reverse process, but it is not the same stochastic process law as the reverse SDE unless the diffusion coefficient vanishes. This deterministic ODE is therefore best understood as a probability-flow ODE for the reverse density path.

13

<!-- page: 14 -->

## 4 Learning the Score for Reverse Sampling

Sections 3 derived the reverse SDE and reverse ODE associated with the forward diffusion. To use these reverse dynamics for generation, we must identify the unknown term in the reverse equations and learn it from data. This section presents that story in a narrative order: we first isolate the unknown quantity in the reverse dynamics; next we introduce a score model and a score-matching objective; then we connect the score to the posterior mean noise in the forward process; after that we reparameterize the score model as a noise predictor and derive the standard denoising loss; finally we write the learned reverse SDE and reverse ODE in both score-model and noise-prediction form.

### 4.1 The unknown part of the reverse ODE and reverse SDE

Recall that the reverse SDE and reverse ODE are

$$
\mathrm{d}X_t = \left(f_t X_t - g_t^2\nabla \log p_t(X_t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0, \tag{32}
$$

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t - \frac{1}{2}g_t^2\nabla \log p_t(X_t), \qquad t : 1 \to 0. \tag{33}
$$

The coefficients \(f_t\) and \(g_t\) are determined by the chosen forward process, so they are known once the noise schedule has been fixed. The only unknown term in both reverse dynamics is therefore the time-dependent score

$$
s_t^*(x) := \nabla \log p_t(x).
$$

Thus the central problem in reverse-time sampling is to estimate the score function along the forward density path.

### 4.2 A neural score model and score matching

A natural strategy is to approximate the score by a neural network

$$
s_\theta(x, t) \approx s_t^*(x) = \nabla \log p_t(x).
$$

This leads to the score-matching objective

$$
\mathcal{L}_{\mathrm{SM}}(\theta) := \frac{1}{2}\int_0^1 \lambda(t)\,\mathbb{E}_{X_t \sim p_t}\left[\|s_\theta(X_t, t) - \nabla \log p_t(X_t)\|_2^2\right]\mathrm{d}t, \tag{34}
$$

where \(\lambda(t) \geq 0\) is a user-chosen weighting function. In principle, minimizing (34) would directly learn the unknown part of the reverse ODE and reverse SDE. In practice, however, the target \(\nabla \log p_t(x)\) is not available in closed form, so we need a tractable reformulation of the same objective.

### 4.3 The score as a conditional expectation of the forward noise

The key observation comes from the forward reparameterization

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I).
$$

It implies that the score can be expressed in terms of a conditional expectation of the Gaussian noise.

14

<!-- page: 15 -->

**Proposition 4.1** (Posterior mean noise identity). *If*

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I),
$$

*then*

$$
\mathbb{E}[\varepsilon \mid X_t = x] = -\sigma_t \nabla \log p_t(x). \tag{35}
$$

*Proof.* From the forward reparameterization,

$$
\varepsilon = \frac{X_t - \alpha_t X_0}{\sigma_t}.
$$

By (8), for every fixed \(x_0\),

$$
\nabla_x \log p_t(x \mid x_0) = -\frac{x - \alpha_t x_0}{\sigma_t^2},
$$

so

$$
-\sigma_t \nabla_x \log p_t(x \mid x_0) = \frac{x - \alpha_t x_0}{\sigma_t}.
$$

Substituting \(x = X_t\) and \(x_0 = X_0\) yields

$$
-\sigma_t \nabla \log p_t(X_t \mid X_0) = \varepsilon.
$$

Now condition on the event \(X_t = x\). After conditioning, the remaining randomness is through the posterior variable \(X_0 \mid X_t = x\) (equivalently, through \(\varepsilon \mid X_t = x\)). Therefore

$$
\mathbb{E}[\varepsilon \mid X_t = x] = -\sigma_t \mathbb{E}[\nabla_x \log p_t(x \mid X_0) \mid X_t = x].
$$

Since the quantity inside the conditional expectation depends on the remaining randomness only through \(X_0\), we may write

$$
\mathbb{E}[\varepsilon \mid X_t = x] = -\sigma_t \mathbb{E}_{X_0 \mid X_t = x}[\nabla_x \log p_t(x \mid X_0)].
$$

Fisher's identity gives

$$
\mathbb{E}_{X_0 \mid X_t = x}[\nabla_x \log p_t(x \mid X_0)] = \nabla \log p_t(x),
$$

which proves (35). â–¡

### 4.4 Reparameterizing the score model as a noise predictor

The previous proposition suggests introducing the *ideal noise predictor*

$$
\epsilon^*(x, t) := -\sigma_t \nabla \log p_t(x) = \mathbb{E}[\varepsilon \mid X_t = x]. \tag{36}
$$

We now reparameterize the score model by

$$
\epsilon_\theta(x, t) := -\sigma_t s_\theta(x, t).
$$

Then

$$
s_\theta(x, t) - \nabla \log p_t(x) = -\frac{1}{\sigma_t}\big(\epsilon_\theta(x, t) - \epsilon^*(x, t)\big),
$$

so

$$
\|s_\theta(x, t) - \nabla \log p_t(x)\|_2^2 = \frac{1}{\sigma_t^2}\,\|\epsilon_\theta(x, t) - \epsilon^*(x, t)\|_2^2.
$$

Therefore the factor \(\sigma_t^{-2}\) can be absorbed into the time weighting. Renaming the resulting weight by \(\omega(t)\), the score-matching objective (34) becomes

$$
\mathcal{L}(\theta) := \frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_t \sim p_t}\left[\|\epsilon_\theta(X_t, t) + \sigma_t \nabla \log p_t(X_t)\|_2^2\right]\mathrm{d}t. \tag{37}
$$

This is still score matching; it is simply written in the equivalent noise-prediction parameterization.

15

<!-- page: 16 -->

**Theorem 4.2** (Score loss and noise-prediction loss). *Let \(\omega(t) \geq 0\) be a weighting function. Then minimizing (37) is equivalent, up to a constant independent of \(\theta\), to minimizing*

$$
\mathcal{L}(\theta) = \frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_0,\varepsilon}\left[\|\epsilon_\theta(\alpha_t X_0 + \sigma_t\varepsilon, t) - \varepsilon\|_2^2\right]\mathrm{d}t + C. \tag{38}
$$

*Proof.* By (36), the objective (37) can be rewritten as

$$
\mathcal{L}(\theta) = \frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_t}\left[\|\epsilon_\theta(X_t, t) - \mathbb{E}[\varepsilon \mid X_t]\|_2^2\right]\mathrm{d}t.
$$

Apply the orthogonality identity from Appendix H with \(Z = X_t\) and \(a(Z) = \epsilon_\theta(X_t, t)\):

$$
\mathbb{E}_{Z,\varepsilon}\|a(Z) - \varepsilon\|_2^2 = \mathbb{E}_Z\|a(Z) - \mathbb{E}[\varepsilon \mid Z]\|_2^2 + \mathbb{E}_{Z,\varepsilon}\|\varepsilon - \mathbb{E}[\varepsilon \mid Z]\|_2^2.
$$

The second term is independent of \(\theta\). Hence minimizing (37) is equivalent to minimizing

$$
\frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_0,\varepsilon}\left[\|\epsilon_\theta(X_t, t) - \varepsilon\|_2^2\right]\mathrm{d}t + C.
$$

Finally, substitute \(X_t = \alpha_t X_0 + \sigma_t \varepsilon\) to obtain (38). â–¡

### 4.5 The learned reverse SDE and reverse ODE

Once the score model has been learned, replacing the marginal score by the learned score model,

$$
\nabla \log p_t(x) \approx s_\theta(x, t),
$$

The reverse SDE and reverse ODE can be written directly in score-model form as

$$
\mathrm{d}X_t = \left(f_t X_t - g_t^2 s_\theta(X_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0,
$$

and

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t - \frac{1}{2}g_t^2 s_\theta(X_t, t), \qquad t : 1 \to 0.
$$

Using the equivalent parameterization

$$
s_\theta(x, t) = -\frac{1}{\sigma_t}\epsilon_\theta(x, t),
$$

turns the reverse SDE (29) into

$$
\mathrm{d}X_t = \left(f_t X_t + \frac{g_t^2}{\sigma_t}\epsilon_\theta(X_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0, \tag{39}
$$

and turns the reverse ODE (31) into

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t + \frac{g_t^2}{2\sigma_t}\epsilon_\theta(X_t, t), \qquad t : 1 \to 0. \tag{40}
$$

16

<!-- page: 17 -->

## 5 Sampling from the Reverse ODE and SDE

### 5.1 Terminal distribution

Diffusion models are designed so that the terminal marginal is approximately Gaussian:

$$
p_1(x) \approx \mathcal{N}(0, \tilde{\sigma}^2 I). \tag{41}
$$

Sampling therefore begins from

$$
X_1 \sim \mathcal{N}(0, \tilde{\sigma}^2 I).
$$

### 5.2 Basic reverse SDE sampler

To sample from the learned reverse SDE (39), choose a decreasing time grid

$$
1 = t_N > t_{N-1} > \cdots > t_1 > t_0 = 0, \qquad \Delta t_n := t_n - t_{n-1} > 0.
$$

The quantity \(\Delta t_n\) is the positive numerical step size. Although the reverse SDE is written with the convention \(t : 1 \to 0\), the differential increment along one numerical step satisfies

$$
\mathrm{d}t = t_{n-1} - t_n = -\Delta t_n < 0.
$$

Consequently, every explicit backward update acquires a minus sign in front of the drift evaluated at the right endpoint \(t_n\).

Initialize

$$
X_{t_N} \sim \mathcal{N}(0, \tilde{\sigma}^2 I).
$$

To connect the discrete update with the continuous reverse SDE, write (39) as

$$
\mathrm{d}X_t = b_\theta(X_t, t)\,\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad b_\theta(x, t) := f_t x + \frac{g_t^2}{\sigma_t}\epsilon_\theta(x, t).
$$

Integrating from \(t_n\) down to \(t_{n-1}\) gives

$$
X_{t_{n-1}} - X_{t_n} = \int_{t_n}^{t_{n-1}} b_\theta(X_s, s)\,\mathrm{d}s + \int_{t_n}^{t_{n-1}} g_s\,\mathrm{d}\bar{W}_s.
$$

Approximating the drift by its value at the right endpoint yields

$$
\int_{t_n}^{t_{n-1}} b_\theta(X_s, s)\,\mathrm{d}s = -b_\theta(X_{t_n}, t_n)\Delta t_n + O(\Delta t_n^2).
$$

For the stochastic term, define the reverse-time Brownian increment

$$
\Delta \bar{W}_n := \int_{t_n}^{t_{n-1}}\mathrm{d}\bar{W}_s.
$$

Since \(\bar{W}_t = W_{1-t}^{\mathrm{rev}}\) and \(W_\tau^{\mathrm{rev}}\) is a standard Brownian motion in the increasing variable \(\tau = 1 - t\), we have

$$
\Delta \bar{W}_n = W_{1-t_{n-1}}^{\mathrm{rev}} - W_{1-t_n}^{\mathrm{rev}} \sim \mathcal{N}(0, \Delta t_n I).
$$

Therefore the stochastic integral is implemented by sampling

$$
\Delta \bar{W}_n = \sqrt{\Delta t_n}\,Z_n, \qquad Z_n \sim \mathcal{N}(0, I),
$$

which is exactly the meaning of the symbol \(\mathrm{d}\bar{W}_t\) in the numerical scheme.

Thus, for \(n = N, N-1, \ldots, 1\), we sample \(Z_n \sim \mathcal{N}(0, I)\) independently and update

$$
X_{t_{n-1}} = X_{t_n} - \left[f_{t_n}X_{t_n} + \frac{g_{t_n}^2}{\sigma_{t_n}}\epsilon_\theta(X_{t_n}, t_n)\right]\Delta t_n + g_{t_n}\sqrt{\Delta t_n}\,Z_n. \tag{42}
$$

Equation (42) is therefore the first-order Eulerâ€“Maruyama discretization of the reverse SDE (39).

17

<!-- page: 18 -->

### 5.3 Basic reverse ODE sampler

The learned reverse ODE (40) can be solved with any numerical ODE solver. The simplest explicit backward-in-time Euler update is

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = h_\theta(X_t, t), \qquad h_\theta(x, t) := f_t x + \frac{g_t^2}{2\sigma_t}\epsilon_\theta(x, t).
$$

Integrating from \(t_n\) down to \(t_{n-1}\) gives

$$
X_{t_{n-1}} - X_{t_n} = \int_{t_n}^{t_{n-1}} h_\theta(X_s, s)\,\mathrm{d}s = -h_\theta(X_{t_n}, t_n)\Delta t_n + O(\Delta t_n^2),
$$

which produces the explicit first-order backward update

$$
X_{t_{n-1}} = X_{t_n} - \left[f_{t_n}X_{t_n} + \frac{g_{t_n}^2}{2\sigma_{t_n}}\epsilon_\theta(X_{t_n}, t_n)\right]\Delta t_n. \tag{43}
$$

A higher-order option is Heun's method:

$$
k_1 = f_{t_n}X_{t_n} + \frac{g_{t_n}^2}{2\sigma_{t_n}}\epsilon_\theta(X_{t_n}, t_n), \tag{44}
$$

$$
\widetilde{X} = X_{t_n} - \Delta t_n k_1, \tag{45}
$$

$$
k_2 = f_{t_{n-1}}\widetilde{X} + \frac{g_{t_{n-1}}^2}{2\sigma_{t_{n-1}}}\epsilon_\theta(\widetilde{X}, t_{n-1}), \tag{46}
$$

followed by

$$
X_{t_{n-1}} = X_{t_n} - \frac{\Delta t_n}{2}(k_1 + k_2). \tag{47}
$$

Because the ODE is deterministic, adaptive high-order solvers such as RK45 are standard choices.

### 5.4 Fast sampling in the style of DPM-Solver

Fast ODE-based samplers of this type were developed systematically in DPM-Solver and DPM-Solver++ [14, 15]; related acceleration strategies include progressive distillation [23].

Define the log-SNR variable

$$
\lambda_t := \log\frac{\alpha_t}{\sigma_t}. \tag{48}
$$

Assume in this subsection that \(\lambda_t\) is monotone in \(t\), so that \(\lambda\) can be used as an alternative time coordinate.

**Proposition 5.1** (Exact integral form of the learned reverse ODE). *Let*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t + \frac{g_t^2}{2\sigma_t}\epsilon_\theta(X_t, t).
$$

*Then for any two times \(s\) and \(t\),*

$$
\frac{X_t}{\alpha_t} = \frac{X_s}{\alpha_s} - \int_{\lambda_s}^{\lambda_t} e^{-\zeta}\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))\,\mathrm{d}\zeta, \tag{49}
$$

*or equivalently*

$$
X_t = \frac{\alpha_t}{\alpha_s}X_s - \alpha_t\int_{\lambda_s}^{\lambda_t} e^{-\zeta}\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))\,\mathrm{d}\zeta. \tag{50}
$$

*Here \(\vartheta(\cdot)\) denotes the inverse of the monotone map \(t \mapsto \lambda_t\).*

18

<!-- page: 19 -->

*Proof.* Define

$$
R_t := \frac{X_t}{\alpha_t}.
$$

Since \(\dot{\alpha}_t = f_t \alpha_t\),

$$
\begin{aligned}
\frac{\mathrm{d}R_t}{\mathrm{d}t} &= \frac{1}{\alpha_t}\left(\frac{\mathrm{d}X_t}{\mathrm{d}t} - f_t X_t\right)\\
&= \frac{1}{\alpha_t}\cdot\frac{g_t^2}{2\sigma_t}\epsilon_\theta(X_t, t).
\end{aligned}
$$

Also,

$$
\dot{\lambda}_t = \frac{\dot{\alpha}_t}{\alpha_t} - \frac{\dot{\sigma}_t}{\sigma_t} = f_t - \frac{\dot{\sigma}_t}{\sigma_t}.
$$

Using (1),

$$
g_t^2 = 2\sigma_t\dot{\sigma}_t - 2f_t\sigma_t^2 = -2\sigma_t^2\dot{\lambda}_t.
$$

Therefore

$$
\frac{\mathrm{d}R_t}{\mathrm{d}t} = -\frac{\sigma_t}{\alpha_t}\dot{\lambda}_t\,\epsilon_\theta(X_t, t) = -e^{-\lambda_t}\dot{\lambda}_t\,\epsilon_\theta(X_t, t).
$$

Since \(\mathrm{d}\lambda_t = \dot{\lambda}_t\,\mathrm{d}t\), this is

$$
\mathrm{d}R_t = -e^{-\lambda_t}\epsilon_\theta(X_t, t)\,\mathrm{d}\lambda_t.
$$

Integrating from \(s\) to \(t\) gives

$$
R_t - R_s = -\int_{\lambda_s}^{\lambda_t} e^{-\zeta}\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))\,\mathrm{d}\zeta,
$$

which is (49). Multiplying by \(\alpha_t\) yields (50). â–¡

**First-order DPM-Solver update.** Suppose \(s > t\) in physical time, so that we move backward from \(s\) to \(t\). Let

$$
h := \lambda_t - \lambda_s.
$$

Approximate the integrand

$$
\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))
$$

in (50) by \(\epsilon_\theta(X_s, s)\). Then

$$
\begin{aligned}
X_t &\approx \frac{\alpha_t}{\alpha_s}X_s - \alpha_t\epsilon_\theta(X_s, s)\int_{\lambda_s}^{\lambda_t} e^{-\zeta}\,\mathrm{d}\zeta\\
&= \frac{\alpha_t}{\alpha_s}X_s - \alpha_t\epsilon_\theta(X_s, s)\big(e^{-\lambda_s} - e^{-\lambda_t}\big).
\end{aligned}
$$

For standard VP-type schedules, \(\lambda_t\) decreases as \(t\) increases, so \(s > t\) implies \(h > 0\). Also,

$$
\alpha_t e^{-\lambda_t} = \alpha_t\frac{\sigma_t}{\alpha_t} = \sigma_t,
$$

and

$$
\alpha_t e^{-\lambda_s} = \alpha_t e^{-\lambda_t}e^{\lambda_t - \lambda_s} = \sigma_t e^h.
$$

Therefore

$$
X_t \approx \frac{\alpha_t}{\alpha_s}X_s - \sigma_t(e^h - 1)\epsilon_\theta(X_s, s). \tag{51}
$$

Higher-order DPM-Solver methods replace the constant approximation of the integrand by linear or quadratic interpolation in \(\lambda\) [14, 15].

19

<!-- page: 20 -->

## 6 Guided Diffusion

Guided diffusion modifies the reverse score so that the generated sample is steered toward a prescribed condition \(c\). This framework includes classifier guidance, classifier-free guidance, and a number of influential text-to-image and image-editing systems [4, 7, 17, 16, 21, 22]. In text-to-image generation, \(c\) is typically a text prompt or its embedding.

### 6.1 Classifier guidance

Classifier guidance was popularized in diffusion-based image synthesis by Dhariwal and Nichol [4].

Classifier guidance requires two trained components:

1. an unconditional diffusion model, trained with the denoising objective from Section 4,

2. a time-dependent classifier \(p_\phi(c \mid x, t)\), trained on noised data.

Let \((X_0, C) \sim p_0(x, c)\), let \(\varepsilon \sim \mathcal{N}(0, I)\), and define

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon.
$$

With \(t\) sampled from a chosen distribution on \([0, 1]\) (typically the uniform distribution), the standard classifier-training objective is

$$
\mathcal{L}_{\mathrm{clf}}(\phi) := \mathbb{E}_{X_0, C, t, \varepsilon}\left[-\log p_\phi(C \mid X_t, t)\right]. \tag{52}
$$

This is simply the cross-entropy loss of the noisy classifier. Indeed, conditioning on \((X_t, t) = (x, t)\) yields

$$
\mathbb{E}_{C \mid X_t = x, t}\left[-\log p_\phi(C \mid X_t, t)\right] = \sum_c p_t(c \mid x)\big(-\log p_\phi(c \mid x, t)\big),
$$

which is the cross-entropy between the true noisy conditional label distribution \(p_t(c \mid x)\) and the classifier prediction \(p_\phi(c \mid x, t)\). Hence, under sufficient model capacity, the pointwise minimizer satisfies

$$
p_\phi(c \mid x, t) = p_t(c \mid x),
$$

so that

$$
\nabla \log p_\phi(c \mid x, t) \approx \nabla \log p_t(c \mid x).
$$

This is precisely the quantity required in the guidance formulas below.

Suppose we want to sample from the conditional distribution \(p_t(x \mid c)\). By Bayes' rule,

$$
\log p_t(x \mid c) = \log p_t(x) + \log p_t(c \mid x) - \log p_t(c),
$$

so differentiating with respect to \(x\) gives

$$
\nabla \log p_t(x \mid c) = \nabla \log p_t(x) + \nabla \log p_t(c \mid x). \tag{53}
$$

In practice one often uses a time-dependent classifier \(p_\phi(c \mid x, t)\) and replaces \(\nabla \log p_t(c \mid x)\) by \(\nabla \log p_\phi(c \mid x, t)\).

With a guidance scale \(\gamma \geq 0\), the guided reverse SDE becomes

$$
\mathrm{d}X_t = \left[f_t X_t - g_t^2\left(\nabla \log p_t(X_t) + \gamma\nabla \log p_\phi(c \mid X_t, t)\right)\right]\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0. \tag{54}
$$

20

<!-- page: 21 -->

The corresponding guided reverse ODE is

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t - \frac{1}{2}g_t^2\left(\nabla \log p_t(X_t) + \gamma\nabla \log p_\phi(c \mid X_t, t)\right), \qquad t : 1 \to 0. \tag{55}
$$

Using the noise predictor \(\epsilon_\theta(x, t) \approx -\sigma_t \nabla \log p_t(x)\), these become

$$
\mathrm{d}X_t = \left[f_t X_t + \frac{g_t^2}{\sigma_t}\epsilon_\theta(X_t, t) - \gamma g_t^2\nabla \log p_\phi(c \mid X_t, t)\right]\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \tag{56}
$$

and

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t + \frac{g_t^2}{2\sigma_t}\epsilon_\theta(X_t, t) - \frac{\gamma}{2}g_t^2\nabla \log p_\phi(c \mid X_t, t). \tag{57}
$$

### 6.2 Classifier-free guidance

Classifier-free guidance was introduced by Ho and Salimans [7].

Classifier-free guidance avoids a separate classifier. Instead, one trains a single network \(\epsilon_\theta(x, t, c)\) with random condition dropout, so that the same network can produce

$$
\epsilon_\theta(x, t, c) \qquad \text{and} \qquad \epsilon_\theta(x, t, \varnothing),
$$

where \(\varnothing\) denotes the null condition.

Let \(P_{\mathrm{drop}} \in [0, 1]\) be the dropout probability, and define a random dropped condition

$$
\widetilde{C} := \begin{cases} C, & \text{with probability } 1 - P_{\mathrm{drop}},\\ \varnothing, & \text{with probability } P_{\mathrm{drop}}.\end{cases}
$$

Classifier-free guidance trains a single denoiser with the mixed objective

$$
\mathcal{L}_{\mathrm{cfg}}(\theta) := \frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_0, C, \varepsilon, \widetilde{C}}\left[\big\|\epsilon_\theta(X_t, t, \widetilde{C}) - \varepsilon\big\|_2^2\right]\mathrm{d}t, \tag{58}
$$

where, as before,

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon.
$$

This is the same denoising loss as in Section 4, but applied to the augmented conditioning variable \(\widetilde{C}\). By the orthogonality identity with

$$
Z = (X_t, \widetilde{C}),
$$

the pointwise minimizer is

$$
\epsilon_\theta^*(x, t, \tilde{c}) = \mathbb{E}_{\varepsilon \mid X_t = x, \widetilde{C} = \tilde{c}}[\varepsilon]. \tag{59}
$$

When \(\tilde{c} = c\) is a genuine condition, this conditional expectation equals the scaled conditional score,

$$
\epsilon_\theta^*(x, t, c) = -\sigma_t \nabla \log p_t(x \mid c),
$$

whereas for the null condition it reduces to the unconditional predictor,

$$
\epsilon_\theta^*(x, t, \varnothing) = -\sigma_t \nabla \log p_t(x).
$$

Thus a single network learns both the conditional and unconditional denoisers needed for classifier-free guidance.

21

<!-- page: 22 -->

The classifier-free guided predictor is

$$
\epsilon_\theta^{\mathrm{cfg}}(x, t, c; s) := \epsilon_\theta(x, t, \varnothing) + s\Big(\epsilon_\theta(x, t, c) - \epsilon_\theta(x, t, \varnothing)\Big), \tag{60}
$$

where \(s \geq 1\) is the guidance scale. When \(s = 1\) this reduces to the ordinary conditional predictor; when \(s > 1\) it extrapolates toward the conditional direction and typically improves condition fidelity at the cost of some diversity.

The classifier-free guided reverse SDE is obtained by replacing \(\epsilon_\theta\) in (39) by \(\epsilon_\theta^{\mathrm{cfg}}\):

$$
\mathrm{d}X_t = \left[f_t X_t + \frac{g_t^2}{\sigma_t}\epsilon_\theta^{\mathrm{cfg}}(X_t, t, c; s)\right]\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t. \tag{61}
$$

Similarly, the classifier-free guided reverse ODE is

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t + \frac{g_t^2}{2\sigma_t}\epsilon_\theta^{\mathrm{cfg}}(X_t, t, c; s). \tag{62}
$$

*Remark* 6.1 (Text-to-image generation). In text-to-image diffusion models, the condition \(c\) is a text prompt encoded into a sequence of text features. Classifier-free guidance is especially widely used because it avoids training a separate image-text classifier while still allowing strong conditional control through the scale \(s\); representative examples include GLIDE, latent diffusion models, and Imagen [17, 21, 22].

*Remark* 6.2 (Two different conditional scores in this tutorial). Two distinct conditional scores appear in this tutorial, and they play different roles.

First, the score

$$
\nabla \log p_t(x \mid x_0)
$$

is the *pathwise conditional score*. Here the conditioning variable is a specific clean sample \(x_0\). This score is used in the conditional forward and reverse ODE/SDE analysis, where one studies the noising and denoising trajectory associated with a single data point. In this setting, \(p_t(x \mid x_0)\) is the conditional Gaussian transition density along the forward diffusion path.

Second, the score

$$
\nabla \log p_t(x \mid c)
$$

is the *guidance conditional score*. Here the conditioning variable is an external condition \(c\), such as a class label or a text prompt. Unlike \(p_t(x \mid x_0)\), the density \(p_t(x \mid c)\) is not a single-sample transition kernel. Rather, it is the conditional *marginal* distribution obtained by averaging over all clean data \(x_0\) compatible with the condition \(c\):

$$
p_t(x \mid c) = \int p_t(x \mid x_0)\,p_0(x_0 \mid c)\,\mathrm{d}x_0.
$$

Accordingly, its score

$$
\nabla \log p_t(x \mid c)
$$

describes how to guide generation toward the conditional data distribution associated with \(c\), rather than how to reverse the noising trajectory of one fixed clean sample.

Thus the two conditionals have different meanings:

- \(p_t(x \mid x_0)\) is a pathwise conditional distribution for a fixed clean sample \(x_0\);
- \(p_t(x \mid c)\) is a conditional marginal distribution obtained after averaging over clean data \(x_0\) under the condition \(c\).

They should therefore be interpreted separately, even though both lead to conditional score functions.

22

<!-- page: 23 -->

## 7 Unifying DDPM, DDIM in the Reverse ODE/SDE Framework

This section makes the correspondence between the continuous reverse ODE/SDE framework and the discrete DDPM/DDIM formulations explicit [6, 25, 28]. The logic is organized in four steps:

1. start from the discrete DDPM forward process, continuize it, and construct the corresponding forward SDE;

2. connect the DDPM training loss with the reverse-SDE training loss;

3. connect DDPM inference with reverse-SDE inference;

4. connect DDIM inference with reverse-ODE inference.

To avoid conflicts with the continuous-time notation used in the earlier sections, we use a separate notation for the discrete chain:

$$
\tilde{x}_0, \tilde{x}_1, \ldots, \tilde{x}_N
$$

for the discrete states, while

$$
X_t, \qquad 0 \leq t \leq 1
$$

continues to denote the continuous-time process from the previous sections.

*Remark* 7.1 (Notation map). The original DDPM paper writes the discrete schedule as \((\beta_k, \alpha_k, \bar{\alpha}_k)\) and the discrete states as \((x_k)_{k=0}^N\). In this section we rename them as

$$
b_k, \qquad a_k := 1 - b_k, \qquad \bar{a}_k := \prod_{i=1}^{k} a_i, \qquad \tilde{x}_k,
$$

so that they do not clash with the continuous-time objects \(\alpha_t, \sigma_t, \beta(t), X_t\) already used in this tutorial.

### 7.1 Continuizing the DDPM forward process and constructing its SDE

Let

$$
0 = t_0 < t_1 < \cdots < t_N = 1
$$

be a time grid. The discrete forward Gaussian chain is

$$
q(\tilde{x}_k \mid \tilde{x}_{k-1}) = \mathcal{N}\left(\tilde{x}_k; \sqrt{a_k}\,\tilde{x}_{k-1}, (1 - a_k)I\right), \qquad k = 1, \ldots, N, \tag{63}
$$

where

$$
b_k \in (0, 1), \qquad a_k := 1 - b_k, \qquad \bar{a}_k := \prod_{i=1}^{k} a_i, \qquad \bar{a}_0 := 1.
$$

**Proposition 7.2** (Closed form of the DDPM forward marginal). *For every \(k \in \{1, \ldots, N\}\),*

$$
q(\tilde{x}_k \mid \tilde{x}_0) = \mathcal{N}\left(\tilde{x}_k; \sqrt{\bar{a}_k}\,\tilde{x}_0, (1 - \bar{a}_k)I\right). \tag{64}
$$

*Equivalently,*

$$
\tilde{x}_k = \sqrt{\bar{a}_k}\,\tilde{x}_0 + \sqrt{1 - \bar{a}_k}\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I). \tag{65}
$$

23

<!-- page: 24 -->

*Proof.* We prove (64) by induction on \(k\).

For \(k = 1\), the statement is exactly the one-step kernel (63), because \(\bar{a}_1 = a_1\).

Now assume that for some \(k - 1 \geq 1\) we have

$$
\tilde{X}_{k-1} = \sqrt{\bar{a}_{k-1}}\,\tilde{X}_0 + \sqrt{1 - \bar{a}_{k-1}}\,\varepsilon_{k-1}', \qquad \varepsilon_{k-1}' \sim \mathcal{N}(0, I),
$$

with \(\varepsilon_{k-1}'\) independent of \(\tilde{X}_0\). The one-step DDPM forward process gives

$$
\tilde{X}_k = \sqrt{a_k}\,\tilde{X}_{k-1} + \sqrt{1 - a_k}\,\varepsilon_k, \qquad \varepsilon_k \sim \mathcal{N}(0, I),
$$

where \(\varepsilon_k\) is independent of \((\tilde{X}_0, \varepsilon_{k-1}')\). Substituting the inductive form of \(\tilde{X}_{k-1}\) yields

$$
\begin{aligned}
\tilde{X}_k &= \sqrt{a_k \bar{a}_{k-1}}\,\tilde{X}_0 + \sqrt{a_k(1 - \bar{a}_{k-1})}\,\varepsilon_{k-1}' + \sqrt{1 - a_k}\,\varepsilon_k\\
&= \sqrt{\bar{a}_k}\,\tilde{X}_0 + \sqrt{a_k(1 - \bar{a}_{k-1})}\,\varepsilon_{k-1}' + \sqrt{1 - a_k}\,\varepsilon_k,
\end{aligned}
$$

because \(\bar{a}_k = a_k \bar{a}_{k-1}\).

The last two terms are independent centered Gaussians. Their sum is therefore Gaussian with covariance

$$
\begin{aligned}
a_k(1 - \bar{a}_{k-1})I &+ (1 - a_k)I\\
&= \big(a_k - a_k\bar{a}_{k-1} + 1 - a_k\big)I\\
&= (1 - \bar{a}_k)I.
\end{aligned}
$$

Hence there exists \(\varepsilon_k' \sim \mathcal{N}(0, I)\) such that

$$
\sqrt{a_k(1 - \bar{a}_{k-1})}\,\varepsilon_{k-1}' + \sqrt{1 - a_k}\,\varepsilon_k = \sqrt{1 - \bar{a}_k}\,\varepsilon_k'.
$$

Therefore

$$
\tilde{X}_k = \sqrt{\bar{a}_k}\,\tilde{X}_0 + \sqrt{1 - \bar{a}_k}\,\varepsilon_k',
$$

which is exactly (64) and (65). The induction is complete. â–¡

Compare this with the continuous Gaussian path from Section 2:

$$
X_t = \alpha_t X_0 + \sigma_t \varepsilon.
$$

The exact correspondence at the grid point \(t_k\) is

$$
X_{t_k} \equiv \tilde{X}_k, \qquad p_{t_k}(x) = q_k(x), \qquad \alpha_{t_k} = \sqrt{\bar{a}_k}, \qquad \sigma_{t_k} = \sqrt{1 - \bar{a}_k}. \tag{66}
$$

At every grid point we therefore have

$$
\alpha_{t_k}^2 + \sigma_{t_k}^2 = \bar{a}_k + (1 - \bar{a}_k) = 1.
$$

This suggests the following continuization of the discrete DDPM forward process.

**Definition 7.3** (Continuized DDPM forward path). *Choose differentiable functions \(\alpha_t, \sigma_t\) on \([0, 1]\) such that*

$$
\alpha_{t_k} = \sqrt{\bar{a}_k}, \qquad \sigma_{t_k} = \sqrt{1 - \bar{a}_k}, \qquad \alpha_t^2 + \sigma_t^2 = 1 \quad \text{for all } t \in [0, 1].
$$

*The associated conditional Gaussian path is*

$$
p_t(x \mid x_0) = \mathcal{N}(x; \alpha_t x_0, \sigma_t^2 I).
$$

*We call this path the* continuized DDPM forward process.

24

<!-- page: 25 -->

**Theorem 7.4** (The continuized DDPM forward process is generated by a VP-SDE). *Let \(p_t(x \mid x_0) = \mathcal{N}(x; \alpha_t x_0, \sigma_t^2 I)\) be the continuized DDPM forward path. Then it is generated by the variance-preserving SDE*

$$
\mathrm{d}X_t = -\frac{1}{2}\beta(t)X_t\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}W_t, \tag{67}
$$

*where*

$$
\beta(t) := -2\frac{\dot{\alpha}_t}{\alpha_t} = g_t^2 \geq 0. \tag{68}
$$

*Proof.* Section 2 proved that any Gaussian path

$$
p_t(x \mid x_0) = \mathcal{N}(x; \alpha_t x_0, \sigma_t^2 I)
$$

is generated by the forward SDE

$$
\mathrm{d}X_t = f_t X_t\,\mathrm{d}t + g_t\,\mathrm{d}W_t,
$$

provided

$$
f_t = \frac{\dot{\alpha}_t}{\alpha_t}, \qquad g_t^2 = \frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 - 2\frac{\dot{\alpha}_t}{\alpha_t}\sigma_t^2.
$$

We now simplify these coefficients under the variance-preserving constraint

$$
\alpha_t^2 + \sigma_t^2 = 1.
$$

Differentiate this identity with respect to \(t\):

$$
\frac{\mathrm{d}}{\mathrm{d}t}(\alpha_t^2 + \sigma_t^2) = 0.
$$

Hence

$$
2\alpha_t\dot{\alpha}_t + \frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 = 0,
$$

so

$$
\frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 = -2\alpha_t\dot{\alpha}_t.
$$

Substituting this into the general formula for \(g_t^2\) gives

$$
\begin{aligned}
g_t^2 &= -2\alpha_t\dot{\alpha}_t - 2\frac{\dot{\alpha}_t}{\alpha_t}\sigma_t^2\\
&= -2\frac{\dot{\alpha}_t}{\alpha_t}(\alpha_t^2 + \sigma_t^2)\\
&= -2\frac{\dot{\alpha}_t}{\alpha_t},
\end{aligned}
$$

because \(\alpha_t^2 + \sigma_t^2 = 1\). Therefore

$$
f_t = \frac{\dot{\alpha}_t}{\alpha_t} = -\frac{1}{2}g_t^2.
$$

Define

$$
\beta(t) := g_t^2.
$$

Then

$$
f_t = -\frac{1}{2}\beta(t), \qquad g_t = \sqrt{\beta(t)},
$$

25

<!-- page: 26 -->

and the general Gaussian-path SDE becomes exactly

$$
\mathrm{d}X_t = -\frac{1}{2}\beta(t)X_t\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}W_t.
$$

Finally, Section 2 already verified that the Gaussian conditional density satisfies the conditional Fokkerâ€“Planck equation for the general coefficients \((f_t, g_t)\). Since in the present variance-preserving case those coefficients reduce to

$$
f_t = -\frac{1}{2}\beta(t), \qquad g_t^2 = \beta(t),
$$

the same verification yields

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \left(-\frac{1}{2}\beta(t)\,x\,p_t(x \mid x_0)\right) + \frac{1}{2}\beta(t)\Delta p_t(x \mid x_0),
$$

which is exactly the conditional Fokkerâ€“Planck equation of (67). Therefore the VP-SDE (67) generates the continuized DDPM forward process. â–¡

For the discrete step \([t_{k-1}, t_k]\), define the integrated noise level

$$
h_k := \int_{t_{k-1}}^{t_k} \beta(s)\,\mathrm{d}s. \tag{69}
$$

Since

$$
\frac{\dot{\alpha}_t}{\alpha_t} = -\frac{1}{2}\beta(t),
$$

integration over \([t_{k-1}, t_k]\) gives

$$
\log \alpha_{t_k} - \log \alpha_{t_{k-1}} = -\frac{1}{2}\int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s = -\frac{h_k}{2},
$$

hence

$$
\frac{\alpha_{t_k}}{\alpha_{t_{k-1}}} = e^{-h_k/2}.
$$

Now compare this continuous one-step signal factor with the DDPM one-step kernel

$$
q(\tilde{x}_k \mid \tilde{x}_{k-1}) = \mathcal{N}\left(\tilde{x}_k; \sqrt{a_k}\,\tilde{x}_{k-1}, (1 - a_k)I\right).
$$

The one-step mean coefficient must match, so

$$
\sqrt{a_k} := \frac{\alpha_{t_k}}{\alpha_{t_{k-1}}} = e^{-h_k/2}.
$$

Squaring both sides yields

$$
a_k = e^{-h_k}, \qquad b_k = 1 - a_k = 1 - e^{-h_k}. \tag{70}
$$

This is the precise bridge between the continuous VP-SDE coefficients and the discrete DDPM schedule.

26

<!-- page: 27 -->

*Remark* 7.5 (Why the map goes through \(h_k\) rather than pointwise \(f_t, g_t\)). The discrete DDPM coefficients \(a_k\) and \(b_k\) do not correspond to the instantaneous values of \(f_t\) and \(g_t\) at a single time. They correspond to the effect of the continuous SDE accumulated over the whole interval \([t_{k-1}, t_k]\). That is why the correct bridge is

$$
h_k = \int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s, \qquad a_k = e^{-h_k}, \qquad b_k = 1 - e^{-h_k},
$$

rather than a direct pointwise identification such as \(a_k = f_{t_k}\) or \(b_k = g_{t_k}^2\).

| Continuous-time notation in this tutorial | Discrete DDPM/DDIM notation |
|---|---|
| \(X_{t_k}\) | \(\tilde{x}_k\) |
| \(\alpha_{t_k}\) | \(\sqrt{\bar{a}_k}\) |
| \(\sigma_{t_k}\) | \(\sqrt{1 - \bar{a}_k}\) |
| \(f_t = -\beta(t)/2\) | one-step attenuation \(\sqrt{a_k} = e^{-h_k/2}\) |
| \(g_t^2 = \beta(t)\) | one-step noise increment \(b_k = 1 - e^{-h_k}\) |
| \(h_k = \int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s\) | \(a_k = e^{-h_k}\) |
| \(\epsilon_\theta(X_{t_k}, t_k)\) | \(\epsilon_\theta(\tilde{x}_k, k)\) |

Throughout this section, we write

$$
\epsilon_\theta(\tilde{x}_k, k) := \epsilon_\theta(\tilde{x}_k, t_k)
$$

for the restriction of the continuous-time noise predictor to the discrete grid. When expectations or conditional laws are involved, we denote by \(\tilde{X}_k\) the discrete random variable at step \(k\) and by \(\tilde{x}_k\) one of its realized values.

### 7.2 DDPM training and its relation to the reverse SDE loss

DDPM training [6] samples

$$
\tilde{X}_0 \sim p_0, \qquad K \sim \mathrm{Unif}\{1, \ldots, N\}, \qquad \varepsilon \sim \mathcal{N}(0, I),
$$

constructs

$$
\tilde{X}_K = \sqrt{\bar{a}_K}\,\tilde{X}_0 + \sqrt{1 - \bar{a}_K}\,\varepsilon,
$$

and minimizes

$$
\mathcal{L}_{\mathrm{DDPM}}(\theta) := \mathbb{E}_{\tilde{X}_0, K, \varepsilon}\left[\big\|\epsilon_\theta(\tilde{X}_K, K) - \varepsilon\big\|_2^2\right]. \tag{71}
$$

**Theorem 7.6** (DDPM training is the reverse-SDE training objective on the time grid). *Let*

$$
q_k(x) := q(\tilde{X}_k = x)
$$

*be the marginal density of the discrete forward chain at step \(k\). Then*

$$
\mathcal{L}_{\mathrm{DDPM}}(\theta) = \mathbb{E}_{\tilde{X}_0, K, \varepsilon}\left[\big\|\epsilon_\theta(\tilde{X}_K, K) + \sqrt{1 - \bar{a}_K}\,\nabla \log q_K(\tilde{X}_K)\big\|_2^2\right] + C, \tag{72}
$$

*where \(C\) is independent of \(\theta\). Under the identification (66), this is exactly the grid-restricted reverse-SDE training objective*

$$
\mathbb{E}_K \mathbb{E}_{X_{t_K} \sim p_{t_K}}\left[\|\epsilon_\theta(X_{t_K}, t_K) + \sigma_{t_K}\nabla \log p_{t_K}(X_{t_K})\|_2^2\right].
$$

27

<!-- page: 28 -->

*Proof.* From (65),

$$
\varepsilon = \frac{\tilde{x}_k - \sqrt{\bar{a}_k}\,\tilde{x}_0}{\sqrt{1 - \bar{a}_k}}.
$$

The conditional forward density is

$$
q(\tilde{x}_k \mid \tilde{x}_0) = \mathcal{N}\left(\tilde{x}_k; \sqrt{\bar{a}_k}\,\tilde{x}_0, (1 - \bar{a}_k)I\right),
$$

so its score is

$$
\nabla \log q(\tilde{x}_k \mid \tilde{x}_0) = -\frac{\tilde{x}_k - \sqrt{\bar{a}_k}\,\tilde{x}_0}{1 - \bar{a}_k}.
$$

Hence

$$
\varepsilon = -\sqrt{1 - \bar{a}_k}\,\nabla \log q(\tilde{x}_k \mid \tilde{x}_0). \tag{73}
$$

Taking conditional expectation given \(\tilde{x}_k\) yields

$$
\mathbb{E}_{\varepsilon \mid \tilde{X}_k = \tilde{x}_k}[\varepsilon] = -\sqrt{1 - \bar{a}_k}\,\mathbb{E}_{\tilde{X}_0 \mid \tilde{X}_k = \tilde{x}_k}[\nabla \log q(\tilde{x}_k \mid \tilde{x}_0)].
$$

By Fisher's identity,

$$
\mathbb{E}_{\tilde{X}_0 \mid \tilde{X}_k = \tilde{x}_k}[\nabla \log q(\tilde{x}_k \mid \tilde{x}_0)] = \nabla \log q_k(\tilde{x}_k),
$$

and therefore

$$
\mathbb{E}_{\varepsilon \mid \tilde{X}_k = \tilde{x}_k}[\varepsilon] = -\sqrt{1 - \bar{a}_k}\,\nabla \log q_k(\tilde{x}_k). \tag{74}
$$

Now apply the orthogonality identity with

$$
Z = \tilde{x}_k, \qquad a(Z) = \epsilon_\theta(\tilde{x}_k, k).
$$

Then

$$
\mathbb{E}_{\tilde{X}_k, \varepsilon}\|\epsilon_\theta(\tilde{X}_k, k) - \varepsilon\|_2^2 = \mathbb{E}_{\tilde{X}_k}\left\|\epsilon_\theta(\tilde{X}_k, k) - \mathbb{E}_{\varepsilon \mid \tilde{X}_k}[\varepsilon]\right\|_2^2 + \mathbb{E}_{\tilde{X}_k, \varepsilon}\left\|\varepsilon - \mathbb{E}_{\varepsilon \mid \tilde{X}_k}[\varepsilon]\right\|_2^2.
$$

The second term is independent of \(\theta\). Substituting (74) gives

$$
\mathbb{E}_{\tilde{X}_k, \varepsilon}\|\epsilon_\theta(\tilde{X}_k, k) - \varepsilon\|_2^2 = \mathbb{E}_{\tilde{X}_k}\left\|\epsilon_\theta(\tilde{X}_k, k) + \sqrt{1 - \bar{a}_k}\,\nabla \log q_k(\tilde{X}_k)\right\|_2^2 + C,
$$

which is exactly (72).

Finally, by (66),

$$
q_k(x) = p_{t_k}(x), \qquad \sqrt{1 - \bar{a}_k} = \sigma_{t_k},
$$

so the discrete target is precisely

$$
-\sigma_{t_k}\nabla \log p_{t_k}(x).
$$

Thus DDPM training learns the same scaled score as the reverse-SDE framework, but only at the discrete times \(t_k\). Since the reverse ODE is obtained from the same scaled score, the same conclusion also applies to the reverse ODE. â–¡

28

<!-- page: 29 -->

### 7.3 DDPM inference and its relation to the reverse SDE

The exact reverse Gaussian posterior of the discrete forward chain, central to DDPM sampling [6, 18], is

$$
q(\tilde{x}_{k-1} \mid \tilde{x}_k, \tilde{x}_0) = \mathcal{N}\left(\tilde{x}_{k-1}; \widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0), \widetilde{b}_k I\right), \tag{75}
$$

where

$$
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) := \frac{\sqrt{\bar{a}_{k-1}}\,b_k}{1 - \bar{a}_k}\tilde{x}_0 + \frac{\sqrt{a_k}(1 - \bar{a}_{k-1})}{1 - \bar{a}_k}\tilde{x}_k, \tag{76}
$$

and

$$
\widetilde{b}_k := \frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}b_k. \tag{77}
$$

To see this directly, fix \(\tilde{x}_k\) and \(\tilde{x}_0\) and regard the posterior as a function of \(\tilde{x}_{k-1}\). By Bayes' rule,

$$
q(\tilde{x}_{k-1} \mid \tilde{x}_k, \tilde{x}_0) \propto q(\tilde{x}_k \mid \tilde{x}_{k-1})\,q(\tilde{x}_{k-1} \mid \tilde{x}_0).
$$

Using the forward kernels,

$$
q(\tilde{x}_k \mid \tilde{x}_{k-1}) \propto \exp\left(-\frac{\|\tilde{x}_k - \sqrt{a_k}\,\tilde{x}_{k-1}\|_2^2}{2b_k}\right),
$$

and

$$
q(\tilde{x}_{k-1} \mid \tilde{x}_0) \propto \exp\left(-\frac{\|\tilde{x}_{k-1} - \sqrt{\bar{a}_{k-1}}\,\tilde{x}_0\|_2^2}{2(1 - \bar{a}_{k-1})}\right).
$$

Therefore

$$
\begin{aligned}
\log q(\tilde{x}_{k-1} \mid \tilde{x}_k, \tilde{x}_0) &= C - \frac{\|\tilde{x}_k - \sqrt{a_k}\,\tilde{x}_{k-1}\|_2^2}{2b_k} - \frac{\|\tilde{x}_{k-1} - \sqrt{\bar{a}_{k-1}}\,\tilde{x}_0\|_2^2}{2(1 - \bar{a}_{k-1})}\\
&= C' - \frac{1}{2}\left(\frac{a_k}{b_k} + \frac{1}{1 - \bar{a}_{k-1}}\right)\|\tilde{x}_{k-1}\|_2^2\\
&\quad + \left(\frac{\sqrt{a_k}}{b_k}\tilde{x}_k + \frac{\sqrt{\bar{a}_{k-1}}}{1 - \bar{a}_{k-1}}\tilde{x}_0\right)^\top \tilde{x}_{k-1},
\end{aligned}
$$

where \(C, C'\) are constants independent of \(\tilde{x}_{k-1}\). Since

$$
\frac{a_k}{b_k} + \frac{1}{1 - \bar{a}_{k-1}} = \frac{a_k(1 - \bar{a}_{k-1}) + b_k}{b_k(1 - \bar{a}_{k-1})} = \frac{1 - \bar{a}_k}{b_k(1 - \bar{a}_{k-1})},
$$

the quadratic coefficient equals \(\widetilde{b}_k^{-1}\) with

$$
\widetilde{b}_k = \frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}b_k.
$$

Completing the square therefore gives a Gaussian posterior with covariance \(\widetilde{b}_k I\) and mean

$$
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) = \widetilde{b}_k\left(\frac{\sqrt{a_k}}{b_k}\tilde{x}_k + \frac{\sqrt{\bar{a}_{k-1}}}{1 - \bar{a}_{k-1}}\tilde{x}_0\right).
$$

Now substitute

$$
\widetilde{b}_k = \frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}b_k.
$$

29

<!-- page: 30 -->

Then

$$
\begin{aligned}
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) &= \frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}b_k\left(\frac{\sqrt{a_k}}{b_k}\tilde{x}_k + \frac{\sqrt{\bar{a}_{k-1}}}{1 - \bar{a}_{k-1}}\tilde{x}_0\right)\\
&= \frac{\sqrt{a_k}(1 - \bar{a}_{k-1})}{1 - \bar{a}_k}\tilde{x}_k + \frac{b_k\sqrt{\bar{a}_{k-1}}}{1 - \bar{a}_k}\tilde{x}_0,
\end{aligned}
$$

which is exactly (76). Using (65),

$$
\tilde{x}_0 = \frac{\tilde{x}_k - \sqrt{1 - \bar{a}_k}\,\varepsilon}{\sqrt{\bar{a}_k}},
$$

so substituting into (76) gives

$$
\begin{aligned}
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) &= \frac{\sqrt{a_k}(1 - \bar{a}_{k-1})}{1 - \bar{a}_k}\tilde{x}_k + \frac{b_k\sqrt{\bar{a}_{k-1}}}{1 - \bar{a}_k}\cdot\frac{\tilde{x}_k - \sqrt{1 - \bar{a}_k}\,\varepsilon}{\sqrt{\bar{a}_k}}\\
&= \frac{\sqrt{a_k}(1 - \bar{a}_{k-1})}{1 - \bar{a}_k}\tilde{x}_k + \frac{b_k}{\sqrt{a_k}(1 - \bar{a}_k)}\tilde{x}_k - \frac{b_k}{\sqrt{a_k}\sqrt{1 - \bar{a}_k}}\varepsilon.
\end{aligned}
$$

Here we used \(\bar{a}_k = a_k\bar{a}_{k-1}\), hence

$$
\frac{\sqrt{\bar{a}_{k-1}}}{\sqrt{\bar{a}_k}} = \frac{1}{\sqrt{a_k}}.
$$

Now combine the two coefficients of \(\tilde{x}_k\):

$$
\begin{aligned}
\frac{\sqrt{a_k}(1 - \bar{a}_{k-1})}{1 - \bar{a}_k} + \frac{b_k}{\sqrt{a_k}(1 - \bar{a}_k)} &= \frac{a_k(1 - \bar{a}_{k-1}) + b_k}{\sqrt{a_k}(1 - \bar{a}_k)}\\
&= \frac{1 - \bar{a}_k}{\sqrt{a_k}(1 - \bar{a}_k)} = \frac{1}{\sqrt{a_k}},
\end{aligned}
$$

because

$$
a_k(1 - \bar{a}_{k-1}) + b_k = a_k - a_k\bar{a}_{k-1} + b_k = a_k + b_k - \bar{a}_k = 1 - \bar{a}_k.
$$

Therefore

$$
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) = \frac{1}{\sqrt{a_k}}\left(\tilde{x}_k - \frac{b_k}{\sqrt{1 - \bar{a}_k}}\varepsilon\right). \tag{78}
$$

DDPM replaces the true noise \(\varepsilon\) in (78) by the learned predictor \(\epsilon_\theta(\tilde{x}_k, k)\) and defines the learned reverse kernel

$$
p_\theta(\tilde{x}_{k-1} \mid \tilde{x}_k) = \mathcal{N}\left(\tilde{x}_{k-1}; \widetilde{\mu}_\theta(\tilde{x}_k, k), \widetilde{b}_k I\right), \tag{79}
$$

with

$$
\widetilde{\mu}_\theta(\tilde{x}_k, k) := \frac{1}{\sqrt{a_k}}\left(\tilde{x}_k - \frac{b_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k)\right). \tag{80}
$$

**Theorem 7.7** (DDPM ancestral sampling and the reverse SDE). *Consider the learned reverse SDE*

$$
\mathrm{d}X_t = \left(f_t X_t + \frac{g_t^2}{\sigma_t}\epsilon_\theta(X_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t.
$$

*DDPM sampling admits two complementary interpretations.*

1. *It is exactly the learned reverse Gaussian chain associated with the discrete forward diffusion (63).*

30

<!-- page: 31 -->

2. *Under the VP correspondence (66) and (70), its conditional mean matches the conditional mean of the first-order backward Eulerâ€“Maruyama discretization of the learned reverse SDE up to \(O(h_k^2)\). Its stochastic term does not coincide exactly with the Eulerâ€“Maruyama stochastic term at finite step size; instead DDPM uses the exact Gaussian posterior variance of the discrete forward diffusion. For interior steps with \(1 - \bar{a}_{k-1} > 0\) fixed, the two variances agree to first order:*

$$
\widetilde{b}_k = h_k + O(h_k^2).
$$

*Proof.* For the first claim, the exact reverse posterior of the discrete forward chain was derived above:

$$
q(\tilde{x}_{k-1} \mid \tilde{x}_k, \tilde{x}_0) = \mathcal{N}\left(\tilde{x}_{k-1}; \widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0), \widetilde{b}_k I\right),
$$

with

$$
\widetilde{\mu}_k(\tilde{x}_k, \tilde{x}_0) = \frac{1}{\sqrt{a_k}}\left(\tilde{x}_k - \frac{b_k}{\sqrt{1 - \bar{a}_k}}\varepsilon\right).
$$

DDPM keeps the same Gaussian form and the same variance \(\widetilde{b}_k I\), but replaces the inaccessible target \(\varepsilon\) by the learned predictor \(\epsilon_\theta(\tilde{x}_k, k)\). Therefore the learned DDPM kernel (79) is exactly the learned reverse Gaussian chain associated with the discrete forward diffusion.

We now compare with the reverse SDE from Section 5. In the variance-preserving case,

$$
f_t = -\frac{1}{2}\beta(t), \qquad g_t^2 = \beta(t), \qquad \sigma_{t_k} = \sqrt{1 - \bar{a}_k}.
$$

Let

$$
h_k := \int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s.
$$

Then by (70),

$$
a_k = e^{-h_k}, \qquad b_k = 1 - e^{-h_k}.
$$

**Step 1: derive the backward Eulerâ€“Maruyama step from the reverse SDE.** In the VP case, the learned reverse SDE is

$$
\mathrm{d}X_t = \left(-\frac{1}{2}\beta(t)X_t + \frac{\beta(t)}{\sigma_t}\epsilon_\theta(X_t, t)\right)\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0.
$$

Integrating from \(t_k\) down to \(t_{k-1}\) gives

$$
\begin{aligned}
X_{t_{k-1}} - X_{t_k} &= \int_{t_k}^{t_{k-1}}\left(-\frac{1}{2}\beta(s)X_s + \frac{\beta(s)}{\sigma_s}\epsilon_\theta(X_s, s)\right)\mathrm{d}s + \int_{t_k}^{t_{k-1}}\sqrt{\beta(s)}\,\mathrm{d}\bar{W}_s\\
&= \frac{1}{2}\int_{t_{k-1}}^{t_k}\beta(s)X_s\,\mathrm{d}s - \int_{t_{k-1}}^{t_k}\frac{\beta(s)}{\sigma_s}\epsilon_\theta(X_s, s)\,\mathrm{d}s + \int_{t_k}^{t_{k-1}}\sqrt{\beta(s)}\,\mathrm{d}\bar{W}_s.
\end{aligned}
$$

For a first-order backward Eulerâ€“Maruyama step, freeze the drift at the right endpoint:

$$
X_s = \tilde{x}_k + O(|s - t_k|), \qquad \epsilon_\theta(X_s, s) = \epsilon_\theta(\tilde{x}_k, k) + O(|s - t_k|), \qquad \sigma_s = \sigma_{t_k} + O(|s - t_k|).
$$

Then

$$
\frac{1}{2}\int_{t_{k-1}}^{t_k}\beta(s)X_s\,\mathrm{d}s = \frac{1}{2}\tilde{x}_k\int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s + O(h_k^2) = \frac{h_k}{2}\tilde{x}_k + O(h_k^2),
$$

and

$$
\int_{t_{k-1}}^{t_k}\frac{\beta(s)}{\sigma_s}\epsilon_\theta(X_s, s)\,\mathrm{d}s = \frac{\epsilon_\theta(\tilde{x}_k, k)}{\sigma_{t_k}}\int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s + O(h_k^2) = \frac{h_k}{\sigma_{t_k}}\epsilon_\theta(\tilde{x}_k, k) + O(h_k^2).
$$

31

<!-- page: 32 -->

Since \(\sigma_{t_k} = \sqrt{1 - \bar{a}_k}\), this term is

$$
\frac{h_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k) + O(h_k^2).
$$

For the stochastic term, define

$$
\eta_k := \int_{t_k}^{t_{k-1}}\sqrt{\beta(s)}\,\mathrm{d}\bar{W}_s.
$$

Recall from Appendix B that \(\bar{W}_t = W_{1-t}^{\mathrm{rev}}\) is the backward-\(t\) representation of the standard Brownian motion \(W_\tau^{\mathrm{rev}}\) in the increasing reverse-time variable \(\tau = 1 - t\). Therefore

$$
\eta_k = \int_{1-t_k}^{1-t_{k-1}}\sqrt{\beta(1-\tau)}\,\mathrm{d}W_\tau^{\mathrm{rev}}.
$$

Since the integrand is deterministic, \(\eta_k\) is a centered Gaussian random vector. Appendix C proves this deterministic-integrand case in detail from the definition of the ItĂ´ integral. More explicitly,

$$
\mathbb{E}_{W^{\mathrm{rev}}}[\eta_k] = 0.
$$

Moreover, ItĂ´ isometry gives

$$
\mathbb{E}_{W^{\mathrm{rev}}}[\eta_k\eta_k^\top] = \left(\int_{1-t_k}^{1-t_{k-1}}\beta(1-\tau)\,\mathrm{d}\tau\right)I = \left(\int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s\right)I = h_k I.
$$

Hence

$$
\eta_k \sim \mathcal{N}(0, h_k I).
$$

Therefore there exists \(z_k \sim \mathcal{N}(0, I)\) such that

$$
\eta_k = \sqrt{h_k}\,z_k, \qquad z_k \sim \mathcal{N}(0, I).
$$

Therefore

$$
X_{t_{k-1}} = X_{t_k} + \frac{h_k}{2}X_{t_k} - \frac{h_k}{\sigma_{t_k}}\epsilon_\theta(X_{t_k}, t_k) + \sqrt{h_k}\,z_k + O(h_k^2).
$$

Replacing \(X_{t_k}\) by \(\tilde{x}_k\) and \(\sigma_{t_k}\) by \(\sqrt{1 - \bar{a}_k}\) yields

$$
\tilde{x}_{k-1}^{\mathrm{SDE}} = \tilde{x}_k + \frac{h_k}{2}\tilde{x}_k - \frac{h_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k) + \sqrt{h_k}\,z_k + O(h_k^2), \tag{81}
$$

where \(z_k \sim \mathcal{N}(0, I)\).

Equation (81) is the first-order backward Eulerâ€“Maruyama step associated with the learned reverse SDE.

**Step 2: expand the DDPM ancestral mean.** On the other hand, the DDPM ancestral mean (80) satisfies

$$
\begin{aligned}
\widetilde{\mu}_\theta(\tilde{x}_k, k) &= \frac{1}{\sqrt{a_k}}\left(\tilde{x}_k - \frac{b_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k)\right)\\
&= \frac{1}{\sqrt{a_k}}\tilde{x}_k - \frac{1}{\sqrt{a_k}}\frac{b_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k).
\end{aligned}
$$

We now expand the two coefficients separately.

32

<!-- page: 33 -->

First, since \(a_k = e^{-h_k}\), we have

$$
\frac{1}{\sqrt{a_k}} = e^{h_k/2} = 1 + \frac{h_k}{2} + \frac{h_k^2}{8} + O(h_k^3) = 1 + \frac{h_k}{2} + O(h_k^2).
$$

Therefore

$$
\frac{1}{\sqrt{a_k}}\tilde{x}_k = \left(1 + \frac{h_k}{2} + O(h_k^2)\right)\tilde{x}_k. \tag{A}
$$

Second, since \(b_k = 1 - e^{-h_k}\),

$$
b_k = 1 - \left(1 - h_k + \frac{h_k^2}{2} + O(h_k^3)\right) = h_k - \frac{h_k^2}{2} + O(h_k^3) = h_k + O(h_k^2).
$$

Hence

$$
\frac{1}{\sqrt{a_k}}b_k = \left(1 + \frac{h_k}{2} + O(h_k^2)\right)\left(h_k + O(h_k^2)\right).
$$

Expanding this product term by term gives

$$
\begin{aligned}
\frac{1}{\sqrt{a_k}}b_k &= h_k + 1\cdot O(h_k^2) + \frac{h_k}{2}\cdot h_k + \frac{h_k}{2}\cdot O(h_k^2) + O(h_k^2)\cdot h_k + O(h_k^2)\cdot O(h_k^2)\\
&= h_k + O(h_k^2) + \frac{h_k^2}{2} + O(h_k^3) + O(h_k^3) + O(h_k^4)\\
&= h_k + O(h_k^2).
\end{aligned}
$$

Therefore

$$
\frac{1}{\sqrt{a_k}}\frac{b_k}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k) = \left(h_k + O(h_k^2)\right)\frac{1}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k). \tag{B}
$$

Substituting (A) and (B) back into \(\widetilde{\mu}_\theta(\tilde{x}_k, k)\) yields

$$
\widetilde{\mu}_\theta(\tilde{x}_k, k) = \left(1 + \frac{h_k}{2} + O(h_k^2)\right)\tilde{x}_k - \left(h_k + O(h_k^2)\right)\frac{1}{\sqrt{1 - \bar{a}_k}}\epsilon_\theta(\tilde{x}_k, k).
$$

Hence the DDPM ancestral mean admits the first-order expansion displayed above.

Therefore the DDPM conditional mean matches the conditional mean of the reverse-SDE step (81) to first order in \(h_k\).

**Step 3: compare the stochastic terms.** The backward Eulerâ€“Maruyama step (81) uses the Gaussian increment

$$
\eta_k^{\mathrm{EM}} := \sqrt{h_k}\,z_k, \qquad \eta_k^{\mathrm{EM}} \sim \mathcal{N}(0, h_k I).
$$

By contrast, the DDPM ancestral step uses

$$
\eta_k^{\mathrm{DDPM}} := \sqrt{\widetilde{b}_k}\,z_k, \qquad \eta_k^{\mathrm{DDPM}} \sim \mathcal{N}(0, \widetilde{b}_k I),
$$

where

$$
\widetilde{b}_k = \frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}\,b_k
$$

is the exact Gaussian posterior variance of the discrete forward diffusion.

33

<!-- page: 34 -->

In general, \(\widetilde{b}_k\) is *not* equal to \(h_k\), so the DDPM stochastic term is not exactly the same as the Eulerâ€“Maruyama stochastic term. Indeed, using (70) and \(\bar{a}_k = a_k\bar{a}_{k-1} = e^{-h_k}\bar{a}_{k-1}\), we obtain

$$
\widetilde{b}_k = \frac{1 - \bar{a}_{k-1}}{1 - e^{-h_k}\bar{a}_{k-1}}\left(1 - e^{-h_k}\right). \tag{82}
$$

This formula already shows that exact equality with \(h_k\) fails in general. For example, at the final denoising step \(k = 1\) we have \(\bar{a}_0 = 1\), hence

$$
\widetilde{b}_1 = \frac{1 - \bar{a}_0}{1 - \bar{a}_1}\,b_1 = 0,
$$

whereas

$$
h_1 = \int_{t_0}^{t_1}\beta(s)\,\mathrm{d}s > 0
$$

whenever \(\beta\) is not identically zero on \([t_0, t_1]\). Therefore the DDPM stochastic term does not coincide exactly with the Eulerâ€“Maruyama stochastic term at finite step size.

Nevertheless, away from this degenerate endpoint, the two variances agree to first order. Assume that \(1 - \bar{a}_{k-1} > 0\) is fixed. Since

$$
e^{-h_k} = 1 - h_k + O(h_k^2),
$$

we have

$$
b_k = 1 - e^{-h_k} = h_k + O(h_k^2).
$$

Also,

$$
\begin{aligned}
1 - \bar{a}_k &= 1 - \bar{a}_{k-1}e^{-h_k}\\
&= 1 - \bar{a}_{k-1}\big(1 - h_k + O(h_k^2)\big)\\
&= (1 - \bar{a}_{k-1}) + \bar{a}_{k-1}h_k + O(h_k^2).
\end{aligned}
$$

Hence

$$
\begin{aligned}
\frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k} &= \frac{1 - \bar{a}_{k-1}}{(1 - \bar{a}_{k-1}) + \bar{a}_{k-1}h_k + O(h_k^2)}\\
&= \frac{1}{1 + \frac{\bar{a}_{k-1}}{1 - \bar{a}_{k-1}}h_k + O(h_k^2)}\\
&= 1 + O(h_k),
\end{aligned}
$$

where the last step uses the Taylor expansion \((1 + u)^{-1} = 1 - u + O(u^2)\) as \(u \to 0\). Multiplying by \(b_k = h_k + O(h_k^2)\) gives

$$
\widetilde{b}_k = (1 + O(h_k))\left(h_k + O(h_k^2)\right) = h_k + O(h_k^2).
$$

Consequently

$$
\sqrt{\widetilde{b}_k} = \sqrt{h_k}\sqrt{1 + O(h_k)} = \sqrt{h_k}\left(1 + O(h_k)\right),
$$

so the DDPM stochastic term agrees with the Eulerâ€“Maruyama stochastic term to first order on interior steps.

We conclude that DDPM sampling should be interpreted in two layers:

- exactly, it is the learned reverse Gaussian chain of the discrete forward diffusion;

34

<!-- page: 35 -->

- asymptotically, under the VP correspondence and for small step size, it is a first-order discrete approximation to the continuous reverse SDE.

â–¡

The ancestral DDPM sampling algorithm is

1. Sample \(\tilde{x}_N \sim \mathcal{N}(0, I)\).

2. For \(k = N, N-1, \ldots, 1\), sample \(z_k \sim \mathcal{N}(0, I)\) and set

$$
\tilde{x}_{k-1} = \widetilde{\mu}_\theta(\tilde{x}_k, k) + \sqrt{\widetilde{b}_k}\,z_k. \tag{83}
$$

3. Output \(\tilde{x}_0\).

### 7.4 DDIM inference and its relation to the reverse ODE

DDIM [25] uses the same trained noise predictor as DDPM, but changes the reverse sampler. Define the predicted clean sample

$$
\widehat{\tilde{x}}_0(\tilde{x}_k, k) := \frac{\tilde{x}_k - \sqrt{1 - \bar{a}_k}\,\epsilon_\theta(\tilde{x}_k, k)}{\sqrt{\bar{a}_k}}. \tag{84}
$$

The deterministic DDIM update is

$$
\tilde{x}_{k-1} = \sqrt{\bar{a}_{k-1}}\,\widehat{\tilde{x}}_0(\tilde{x}_k, k) + \sqrt{1 - \bar{a}_{k-1}}\,\epsilon_\theta(\tilde{x}_k, k). \tag{85}
$$

More generally, DDIM introduces a stochasticity parameter \(\eta \in [0, 1]\) and uses

$$
\tilde{x}_{k-1} = \sqrt{\bar{a}_{k-1}}\,\widehat{\tilde{x}}_0(\tilde{x}_k, k) + \sqrt{1 - \bar{a}_{k-1} - \widehat{s}_k^2}\,\epsilon_\theta(\tilde{x}_k, k) + \widehat{s}_k z_k, \tag{86}
$$

where \(z_k \sim \mathcal{N}(0, I)\) and

$$
\widehat{s}_k := \eta\sqrt{\frac{1 - \bar{a}_{k-1}}{1 - \bar{a}_k}\left(1 - \frac{\bar{a}_k}{\bar{a}_{k-1}}\right)}. \tag{87}
$$

**Theorem 7.8** (Deterministic DDIM is a discrete reverse-ODE sampler). *When \(\eta = 0\), the DDIM update (85) is exactly the first-order one-step discretization of the learned reverse ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = f_t X_t + \frac{g_t^2}{2\sigma_t}\epsilon_\theta(X_t, t)
$$

*obtained by freezing \(\epsilon_\theta\) on the interval \([t_{k-1}, t_k]\).*

*Proof.* Section 5 showed that the learned reverse ODE has the exact variation-of-constants formula

$$
X_t = \frac{\alpha_t}{\alpha_s}X_s - \alpha_t\int_{\lambda_s}^{\lambda_t}e^{-\zeta}\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))\,\mathrm{d}\zeta.
$$

Apply this with \(s = t_k\) and \(t = t_{k-1}\). Then

$$
X_{t_{k-1}} = \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}X_{t_k} - \alpha_{t_{k-1}}\int_{\lambda_{t_k}}^{\lambda_{t_{k-1}}}e^{-\zeta}\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta))\,\mathrm{d}\zeta.
$$

35

<!-- page: 36 -->

Now freeze the integrand on the interval \([t_{k-1}, t_k]\):

$$
\epsilon_\theta(X_{\vartheta(\zeta)}, \vartheta(\zeta)) \approx \epsilon_\theta(\tilde{x}_k, k).
$$

Then

$$
\begin{aligned}
\tilde{x}_{k-1} &= \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\tilde{x}_k - \alpha_{t_{k-1}}\epsilon_\theta(\tilde{x}_k, k)\int_{\lambda_{t_k}}^{\lambda_{t_{k-1}}}e^{-\zeta}\,\mathrm{d}\zeta\\
&= \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\tilde{x}_k - \alpha_{t_{k-1}}\epsilon_\theta(\tilde{x}_k, k)\left[-e^{-\zeta}\right]_{\lambda_{t_k}}^{\lambda_{t_{k-1}}}\\
&= \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\tilde{x}_k - \alpha_{t_{k-1}}\epsilon_\theta(\tilde{x}_k, k)\left(e^{-\lambda_{t_k}} - e^{-\lambda_{t_{k-1}}}\right).
\end{aligned}
$$

Because

$$
\Delta\lambda_k := \lambda_{t_{k-1}} - \lambda_{t_k},
$$

we have

$$
e^{-\lambda_{t_k}} = e^{-\lambda_{t_{k-1}}}e^{\Delta\lambda_k},
$$

so

$$
e^{-\lambda_{t_k}} - e^{-\lambda_{t_{k-1}}} = e^{-\lambda_{t_{k-1}}}\left(e^{\Delta\lambda_k} - 1\right).
$$

Since

$$
e^{-\lambda_{t_{k-1}}} = \frac{\sigma_{t_{k-1}}}{\alpha_{t_{k-1}}},
$$

the coefficient of \(\epsilon_\theta\) becomes

$$
\alpha_{t_{k-1}}\left(e^{-\lambda_{t_k}} - e^{-\lambda_{t_{k-1}}}\right) = \alpha_{t_{k-1}}e^{-\lambda_{t_{k-1}}}\left(e^{\Delta\lambda_k} - 1\right) = \sigma_{t_{k-1}}\left(e^{\Delta\lambda_k} - 1\right).
$$

Hence

$$
\tilde{x}_{k-1} = \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\tilde{x}_k - \sigma_{t_{k-1}}(e^{\Delta\lambda_k} - 1)\epsilon_\theta(\tilde{x}_k, k), \tag{88}
$$

Using

$$
e^{\Delta\lambda_k} = \frac{\alpha_{t_{k-1}}\sigma_{t_k}}{\alpha_{t_k}\sigma_{t_{k-1}}},
$$

the coefficient of \(\epsilon_\theta\) becomes

$$
-\sigma_{t_{k-1}}(e^{\Delta\lambda_k} - 1) = \sigma_{t_{k-1}} - \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\sigma_{t_k}.
$$

Therefore (88) is equivalent to

$$
\tilde{x}_{k-1} = \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\tilde{x}_k + \left(\sigma_{t_{k-1}} - \frac{\alpha_{t_{k-1}}}{\alpha_{t_k}}\sigma_{t_k}\right)\epsilon_\theta(\tilde{x}_k, k). \tag{89}
$$

Now substitute the discrete-continuous identification

$$
\alpha_{t_k} = \sqrt{\bar{a}_k}, \qquad \sigma_{t_k} = \sqrt{1 - \bar{a}_k},
$$

to get

$$
\tilde{x}_{k-1} = \sqrt{\frac{\bar{a}_{k-1}}{\bar{a}_k}}\,\tilde{x}_k + \left(\sqrt{1 - \bar{a}_{k-1}} - \sqrt{\frac{\bar{a}_{k-1}}{\bar{a}_k}}\sqrt{1 - \bar{a}_k}\right)\epsilon_\theta(\tilde{x}_k, k).
$$

36

<!-- page: 37 -->

On the other hand, by the definition (84),

$$
\begin{aligned}
\sqrt{\bar{a}_{k-1}}\,\widehat{\tilde{x}}_0(\tilde{x}_k, k) + \sqrt{1 - \bar{a}_{k-1}}\,\epsilon_\theta(\tilde{x}_k, k) &= \sqrt{\bar{a}_{k-1}}\frac{\tilde{x}_k - \sqrt{1 - \bar{a}_k}\,\epsilon_\theta(\tilde{x}_k, k)}{\sqrt{\bar{a}_k}} + \sqrt{1 - \bar{a}_{k-1}}\,\epsilon_\theta(\tilde{x}_k, k)\\
&= \sqrt{\frac{\bar{a}_{k-1}}{\bar{a}_k}}\,\tilde{x}_k + \left(\sqrt{1 - \bar{a}_{k-1}} - \sqrt{\frac{\bar{a}_{k-1}}{\bar{a}_k}}\sqrt{1 - \bar{a}_k}\right)\epsilon_\theta(\tilde{x}_k, k).
\end{aligned}
$$

The coefficient of \(\tilde{x}_k\) and the coefficient of \(\epsilon_\theta(\tilde{x}_k, k)\) agree term by term, so the two updates are identical. Therefore

$$
\tilde{x}_{k-1} = \sqrt{\bar{a}_{k-1}}\,\widehat{\tilde{x}}_0(\tilde{x}_k, k) + \sqrt{1 - \bar{a}_{k-1}}\,\epsilon_\theta(\tilde{x}_k, k),
$$

which is precisely the deterministic DDIM update (85). Thus deterministic DDIM is the discrete reverse-ODE sampler corresponding to the learned probability-flow ODE. â–¡

When \(\eta > 0\), the additional term \(\widehat{s}_k z_k\) in (86) reintroduces stochasticity. So DDIM interpolates between deterministic reverse-ODE sampling (\(\eta = 0\)) and a stochastic reverse-diffusion-style sampler (\(\eta > 0\)).

37

<!-- page: 38 -->

## 8 Comparison with Flow Matching and Score-Based SDEs

This section places the reverse ODE/SDE framework developed in this tutorial in the context of two closely related viewpoints: flow matching [13] and score-based generative modeling through SDEs [28]. The three frameworks are closely connected, but they differ in what is taken as the primary object, which time direction is emphasized, and what quantity is learned by the neural network.

### 8.1 Flow models, flow matching, diffusion models, and score matching

A *flow model* is a deterministic generative model defined by an ODE

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = v_t(X_t),
$$

where \(v_t : \mathbb{R}^d \to \mathbb{R}^d\) is a time-dependent velocity field. If the corresponding density path is \(p_t\), then the velocity field must satisfy the continuity equation

$$
\partial_t p_t(x) = -\nabla \cdot (p_t(x)v_t(x)).
$$

Given a target density path \(p_t\) and a target velocity field \(v_t^*\) that generates it, the standard flow-matching objective is

$$
\mathcal{L}_{\mathrm{FM}}(\theta) := \int_0^1 \mathbb{E}_{X_t \sim p_t}\left[\|v_\theta(X_t, t) - v_t^*(X_t)\|_2^2\right]\mathrm{d}t. \tag{90}
$$

Thus flow matching learns a velocity field directly.

A *diffusion model* is a stochastic generative model defined by an SDE

$$
\mathrm{d}X_t = b_t(X_t)\,\mathrm{d}t + g_t\,\mathrm{d}W_t,
$$

where the drift transports mass and the Brownian term injects randomness continuously in time. In score-based diffusion modeling, the key quantity is the score

$$
s_t^*(x) := \nabla \log p_t(x).
$$

A score model \(s_\theta(x, t)\) can be trained by score matching, for example through the objective

$$
\mathcal{L}_{\mathrm{SM}}(\theta) := \frac{1}{2}\int_0^1 \lambda(t)\,\mathbb{E}_{X_t \sim p_t}\left[\|s_\theta(X_t, t) - \nabla \log p_t(X_t)\|_2^2\right]\mathrm{d}t, \tag{91}
$$

or equivalently, in the Gaussian diffusion setting of this tutorial, through the reparameterized noise-prediction loss (37)â€“(38). Thus score matching learns the score directly, while the reverse drift is then obtained from that score.

### 8.2 Comparison with *Flow Matching for Generative Modeling*

In this subsection and the next, we temporarily switch to the generative-time convention used in [13, 28]. Thus \(t : 0 \to 1\) is the sampling clock, \(X_0 \sim p_0\) denotes a noise sample, and \(X_1 \sim p_1 = p_{\mathrm{data}}\) denotes a data sample. This is opposite to the convention used in the main body of the tutorial. To avoid notational conflict, we now introduce a new pair of schedules, again denoted by \(\alpha_t\) and \(\sigma_t\), local to Sections 8.2 and 8.3. We assume

$$
\alpha_0 = 0, \quad \alpha_1 = 1, \quad \sigma_0 = 1, \quad \sigma_1 = 0, \qquad \alpha_t \geq 0, \ \sigma_t \geq 0 \text{ for all } t \in [0, 1],
$$

38

<!-- page: 39 -->

Typically, \(\alpha_t\) increases while \(\sigma_t\) decreases, so that the path begins with Gaussian noise and ends at clean data. Conceptually, this is the key difference from our earlier ODE framework: in the main body we first constructed a data-to-noise forward process and then derived a reverse ODE for sampling, whereas flow matching specifies the sampling ODE directly in the forward generative time direction.

**Conditional generative Gaussian path.** Fix a target data point \(x_1\). The conditional generative path is

$$
p_t(x \mid x_1) := \mathcal{N}(x \mid \alpha_t x_1, \sigma_t^2 I). \tag{92}
$$

At \(t = 0\), this distribution is approximately Gaussian noise; at \(t = 1\), it collapses to the clean data point \(x_1\).

**Conditional generative ODE.**

**Theorem 8.1** (Conditional generative ODE). *The conditional path (92) is generated by the ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_t(X_t \mid x_1), \tag{93}
$$

*where*

$$
u_t(x \mid x_1) := \left(\dot{\alpha}_t - \frac{\dot{\sigma}_t}{\sigma_t}\alpha_t\right)x_1 + \frac{\dot{\sigma}_t}{\sigma_t}x. \tag{94}
$$

*Equivalently, the conditional density satisfies*

$$
\partial_t p_t(x \mid x_1) = -\nabla \cdot \big(p_t(x \mid x_1)u_t(x \mid x_1)\big). \tag{95}
$$

*Proof.* Fix \(x_1\) and write

$$
r_t(x) := x - \alpha_t x_1.
$$

From the reparameterization

$$
X_t = \alpha_t x_1 + \sigma_t \varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I),
$$

we obtain

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = \dot{\alpha}_t x_1 + \dot{\sigma}_t \varepsilon = \dot{\alpha}_t x_1 + \dot{\sigma}_t\frac{X_t - \alpha_t x_1}{\sigma_t},
$$

which simplifies to (94). Thus (93) indeed generates the conditional Gaussian path.

We now verify the continuity equation (95) explicitly. Since

$$
p_t(x \mid x_1) = \frac{1}{(2\pi\sigma_t^2)^{d/2}}\exp\left(-\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right),
$$

we have

$$
\log p_t(x \mid x_1) = -\frac{d}{2}\log(2\pi\sigma_t^2) - \frac{\|r_t(x)\|_2^2}{2\sigma_t^2}.
$$

Because

$$
\partial_t r_t(x) = -\dot{\alpha}_t x_1, \qquad \partial_t\|r_t(x)\|_2^2 = -2\dot{\alpha}_t r_t(x)^\top x_1,
$$

39

<!-- page: 40 -->

it follows that

$$
\begin{aligned}
\partial_t \log p_t(x \mid x_1) &= -d\frac{\dot{\sigma}_t}{\sigma_t} - \partial_t\left(\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right)\\
&= -d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2.
\end{aligned}
$$

Therefore

$$
\partial_t p_t(x \mid x_1) = p_t(x \mid x_1)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right]. \tag{96}
$$

Next, by (106),

$$
\nabla p_t(x \mid x_1) = p_t(x \mid x_1)\nabla \log p_t(x \mid x_1) = -p_t(x \mid x_1)\frac{r_t(x)}{\sigma_t^2}.
$$

Also,

$$
u_t(x \mid x_1) = \dot{\alpha}_t x_1 + \frac{\dot{\sigma}_t}{\sigma_t}r_t(x),
$$

so

$$
u_t(x \mid x_1)^\top \nabla p_t(x \mid x_1) = -p_t(x \mid x_1)\left[\frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right].
$$

Moreover,

$$
\nabla \cdot u_t(x \mid x_1) = \frac{\dot{\sigma}_t}{\sigma_t}\nabla \cdot r_t(x) = d\frac{\dot{\sigma}_t}{\sigma_t},
$$

because \(r_t(x) = x - \alpha_t x_1\) and \(\nabla \cdot x = d\). Hence

$$
\begin{aligned}
\nabla \cdot \big(p_t(x \mid x_1)u_t(x \mid x_1)\big) &= u_t(x \mid x_1)^\top \nabla p_t(x \mid x_1) + p_t(x \mid x_1)\nabla \cdot u_t(x \mid x_1)\\
&= p_t(x \mid x_1)\left[-\frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 - \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2 + d\frac{\dot{\sigma}_t}{\sigma_t}\right].
\end{aligned}
$$

Therefore

$$
-\nabla \cdot \big(p_t(x \mid x_1)u_t(x \mid x_1)\big) = p_t(x \mid x_1)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right],
$$

which agrees exactly with (96). This proves (95). â–¡

**Marginal generative ODE.** Marginalizing (92) over the data distribution \(p_1\) gives the noise-to-data density path

$$
p_t(x) := \int_{\mathbb{R}^d} p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1. \tag{97}
$$

Define the marginal generative velocity by

$$
u_t^*(x) := \mathbb{E}[u_t(x \mid X_1) \mid X_t = x]. \tag{98}
$$

**Proposition 8.2** (Marginal generative ODE). *The marginal density path (97) satisfies*

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)u_t^*(x)\big). \tag{99}
$$

*Hence the ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_t^*(X_t), \qquad X_0 \sim p_0, \tag{100}
$$

*transports noise to data in forward time \(t : 0 \to 1\).*

40

<!-- page: 41 -->

*Proof.* Differentiate under the integral sign:

$$
\partial_t p_t(x) = \int \partial_t p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1.
$$

Using (95),

$$
\partial_t p_t(x) = -\int \nabla \cdot \big(p_t(x \mid x_1)u_t(x \mid x_1)\big)p_1(x_1)\,\mathrm{d}x_1.
$$

Since the divergence acts on \(x\), it may be moved outside the integral:

$$
\partial_t p_t(x) = -\nabla \cdot \left(\int p_t(x \mid x_1)u_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1\right).
$$

We now identify the vector field inside the divergence. By Bayes' rule,

$$
\int p_t(x \mid x_1)u_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1 = p_t(x)\int u_t(x \mid x_1)p(x_1 \mid X_t = x)\,\mathrm{d}x_1 = p_t(x)\,u_t^*(x).
$$

Substituting this identity into the previous display yields

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)u_t^*(x)\big),
$$

which is exactly (99). This is the continuity equation associated with the ODE (100). â–¡

At this point there is no reverse ODE: (100) itself already runs from noise to data, so it is the sampling dynamics.

**Marginal flow matching.** If the marginal target velocity \(u_t^*(x)\) were directly available, one could train a generative flow model \(u_\theta(x, t)\) with

$$
\mathcal{L}_{\mathrm{FM}}(\theta) := \frac{1}{2}\int_0^1 \mathbb{E}_{X_t \sim p_t}\left[\|u_\theta(X_t, t) - u_t^*(X_t)\|_2^2\right]\mathrm{d}t. \tag{101}
$$

**Conditional flow matching.** As emphasized in [13], the marginal velocity is typically intractable. The conditional-flow-matching surrogate is

$$
\mathcal{L}_{\mathrm{CFM}}(\theta) := \frac{1}{2}\int_0^1 \mathbb{E}_{X_1,\,X_t \sim p_t(\cdot \mid X_1)}\left[\|u_\theta(X_t, t) - u_t(X_t \mid X_1)\|_2^2\right]\mathrm{d}t. \tag{102}
$$

**Theorem 8.3** (Conditional flow matching is a proxy for marginal flow matching). *The objectives (101) and (102) differ only by a constant independent of \(\theta\). Equivalently,*

$$
\mathcal{L}_{\mathrm{CFM}}(\theta) = \mathcal{L}_{\mathrm{FM}}(\theta) + C.
$$

*Proof.* Fix \(t\) and define

$$
Z := X_t, \qquad \eta := u_t(X_t \mid X_1), \qquad a(Z) := u_\theta(X_t, t).
$$

By (98),

$$
\mathbb{E}[\eta \mid Z] = u_t^*(Z).
$$

Applying the orthogonality identity from Appendix H gives

$$
\mathbb{E}\|a(Z) - \eta\|_2^2 = \mathbb{E}\|a(Z) - \mathbb{E}[\eta \mid Z]\|_2^2 + \mathbb{E}\|\eta - \mathbb{E}[\eta \mid Z]\|_2^2.
$$

Hence

$$
\mathbb{E}\|u_\theta(X_t, t) - u_t(X_t \mid X_1)\|_2^2 = \mathbb{E}\|u_\theta(X_t, t) - u_t^*(X_t)\|_2^2 + C_t,
$$

where \(C_t\) does not depend on \(\theta\). Integrating over \(t\) yields the result. â–¡

41

<!-- page: 42 -->

**Learned generative ODE.** After training, the generative ODE is simply

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_\theta(X_t, t), \qquad X_0 \sim p_0. \tag{103}
$$

This is the exact forward generative viewpoint of [13]: one directly learns a noise-to-data ODE, and the forward ODE itself performs sampling.

### 8.3 Comparison with *Score-Based Generative Modeling through Stochastic Differential Equations*

We keep the same generative-time notation and the same local schedules \(\alpha_t, \sigma_t\) as in Section 8.2: \(X_0 \sim p_0\) is noise, \(X_1 \sim p_1\) is data, and the density path runs in forward time \(t : 0 \to 1\). For the SDE formulation, define the local generative-time coefficients

$$
f_t := \frac{\dot{\alpha}_t}{\alpha_t}, \qquad g_t^2 := -\frac{\mathrm{d}}{\mathrm{d}t}\sigma_t^2 + 2\frac{\dot{\alpha}_t}{\alpha_t}\sigma_t^2, \tag{104}
$$

and assume \(g_t^2 \geq 0\). This is the generative-time analogue of (1). The conceptual difference from the main body is again the same: Sections 2â€“5 start from a noising SDE and derive reverse-time sampling dynamics, whereas the score-based SDE viewpoint below can be written directly as a forward noise-to-data generative SDE.

**Conditional generative Gaussian path.** Fix a target data point \(x_1\). As in (92), consider

$$
p_t(x \mid x_1) := \mathcal{N}(x \mid \alpha_t x_1, \sigma_t^2 I). \tag{105}
$$

Its conditional score is

$$
\nabla \log p_t(x \mid x_1) = -\frac{x - \alpha_t x_1}{\sigma_t^2}. \tag{106}
$$

**Conditional generative SDE.**

**Theorem 8.4** (Conditional generative SDE). *For every fixed \(x_1\), the conditional path (105) is generated by the SDE*

$$
\mathrm{d}X_t = \left(f_t X_t + g_t^2 \nabla \log p_t(X_t \mid x_1)\right)\mathrm{d}t + g_t\,\mathrm{d}W_t, \tag{107}
$$

*with initial law \(X_0 \sim p_0(\cdot \mid x_1)\).*

*Proof.* Write

$$
r_t(x) := x - \alpha_t x_1.
$$

Since

$$
p_t(x \mid x_1) = \frac{1}{(2\pi\sigma_t^2)^{d/2}}\exp\left(-\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right),
$$

$$
\log p_t(x \mid x_1) = -\frac{d}{2}\log(2\pi\sigma_t^2) - \frac{\|r_t(x)\|_2^2}{2\sigma_t^2}.
$$

Because

$$
\partial_t r_t(x) = -\dot{\alpha}_t x_1, \qquad \partial_t\|r_t(x)\|_2^2 = -2\dot{\alpha}_t r_t(x)^\top x_1,
$$

42

<!-- page: 43 -->

we obtain

$$
\begin{aligned}
\partial_t \log p_t(x \mid x_1) &= -d\frac{\dot{\sigma}_t}{\sigma_t} - \partial_t\left(\frac{\|r_t(x)\|_2^2}{2\sigma_t^2}\right)\\
&= -d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2.
\end{aligned}
$$

Hence

$$
\partial_t p_t(x \mid x_1) = p_t(x \mid x_1)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right]. \tag{108}
$$

Next,

$$
\nabla \log p_t(x \mid x_1) = -\frac{r_t(x)}{\sigma_t^2}, \qquad \nabla p_t(x \mid x_1) = -p_t(x \mid x_1)\frac{r_t(x)}{\sigma_t^2}.
$$

Differentiating once more yields

$$
\Delta p_t(x \mid x_1) = p_t(x \mid x_1)\left(\frac{\|r_t(x)\|_2^2}{\sigma_t^4} - \frac{d}{\sigma_t^2}\right),
$$

and

$$
-\nabla \cdot \big(f_t x\, p_t(x \mid x_1)\big) = p_t(x \mid x_1)\left[-f_t d + f_t\frac{x^\top r_t(x)}{\sigma_t^2}\right].
$$

Because \(p_t(x \mid x_1)\nabla \log p_t(x \mid x_1) = \nabla p_t(x \mid x_1)\), the Fokkerâ€“Planck equation of (107) becomes

$$
\partial_t p_t(x \mid x_1) = -\nabla \cdot \big(f_t x\, p_t(x \mid x_1)\big) - \frac{1}{2}g_t^2\Delta p_t(x \mid x_1).
$$

Substituting the previous expressions, the right-hand side of Fokkerâ€“Planck equation becomes

$$
p_t(x \mid x_1)\left[-f_t d + f_t\frac{x^\top r_t(x)}{\sigma_t^2} - \frac{g_t^2}{2}\left(\frac{\|r_t(x)\|_2^2}{\sigma_t^4} - \frac{d}{\sigma_t^2}\right)\right].
$$

Now use \(x = r_t(x) + \alpha_t x_1\) together with

$$
\frac{g_t^2}{2\sigma_t^2} = -\frac{\dot{\sigma}_t}{\sigma_t} + f_t,
$$

which follows from (104). Then the right-hand side simplifies to

$$
p_t(x \mid x_1)\left[-d\frac{\dot{\sigma}_t}{\sigma_t} + \frac{\dot{\alpha}_t}{\sigma_t^2}r_t(x)^\top x_1 + \frac{\dot{\sigma}_t}{\sigma_t^3}\|r_t(x)\|_2^2\right],
$$

which agrees with (108). Therefore the density path of (107) is precisely (105). â–¡

**Marginal generative SDE.** Marginalizing over \(x_1 \sim p_1\) gives

$$
p_t(x) = \int_{\mathbb{R}^d} p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1.
$$

Define the marginal score by

$$
s_t^*(x) := \nabla \log p_t(x). \tag{109}
$$

43

<!-- page: 44 -->

**Proposition 8.5** (Marginal generative SDE). *The marginal density path \(p_t\) is generated by*

$$
\mathrm{d}X_t = \left(f_t X_t + g_t^2 \nabla \log p_t(X_t)\right)\mathrm{d}t + g_t\,\mathrm{d}W_t, \qquad X_0 \sim p_0. \tag{110}
$$

*Proof.* For every fixed \(x_1\), the conditional Fokkerâ€“Planck equation of (107) is

$$
\partial_t p_t(x \mid x_1) = -\nabla \cdot \left(\big[f_t x + g_t^2 \nabla \log p_t(x \mid x_1)\big]p_t(x \mid x_1)\right) + \frac{1}{2}g_t^2\Delta p_t(x \mid x_1).
$$

Integrating both sides against \(p_1(x_1)\,\mathrm{d}x_1\) gives

$$
\begin{aligned}
\partial_t p_t(x) = &-\int \nabla \cdot \left(\big[f_t x + g_t^2 \nabla \log p_t(x \mid x_1)\big]p_t(x \mid x_1)\right)p_1(x_1)\,\mathrm{d}x_1\\
&+ \frac{1}{2}g_t^2\int \Delta p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1.
\end{aligned}
$$

Since the differential operators act on \(x\), we may move them outside the integral:

$$
\begin{aligned}
\partial_t p_t(x) = &-\nabla \cdot \left(\int \big[f_t x + g_t^2 \nabla \log p_t(x \mid x_1)\big]p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1\right)\\
&+ \frac{1}{2}g_t^2\Delta\left(\int p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1\right).
\end{aligned}
$$

Using (97), this becomes

$$
\begin{aligned}
\partial_t p_t(x) = &-\nabla \cdot \left(f_t x\, p_t(x) + g_t^2\int p_t(x \mid x_1)\nabla \log p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1\right)\\
&+ \frac{1}{2}g_t^2\Delta p_t(x).
\end{aligned}
$$

Now

$$
p_t(x \mid x_1)\nabla \log p_t(x \mid x_1) = \nabla p_t(x \mid x_1),
$$

so

$$
\int p_t(x \mid x_1)\nabla \log p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1 = \int \nabla p_t(x \mid x_1)p_1(x_1)\,\mathrm{d}x_1 = \nabla p_t(x).
$$

Equivalently, by Fisher's identity,

$$
\nabla p_t(x) = p_t(x)\nabla \log p_t(x).
$$

Substituting this back gives

$$
\partial_t p_t(x) = -\nabla \cdot \left(\big[f_t x + g_t^2 \nabla \log p_t(x)\big]p_t(x)\right) + \frac{1}{2}g_t^2\Delta p_t(x).
$$

This is exactly the Fokkerâ€“Planck equation of (110), so the SDE (110) generates the marginal density path. â–¡

Again, there is no separate reverse SDE: (110) itself already runs from noise to data.

**Marginal score matching.** If the marginal score \(s_t^*(x) = \nabla \log p_t(x)\) were directly available, one could train a score model \(s_\theta(x, t)\) by

$$
\mathcal{L}_{\mathrm{SM}}(\theta) := \frac{1}{2}\int_0^1 \lambda(t)\,\mathbb{E}_{X_t \sim p_t}\left[\|s_\theta(X_t, t) - \nabla \log p_t(X_t)\|_2^2\right]\mathrm{d}t. \tag{111}
$$

44

<!-- page: 45 -->

**Conditional score matching.** Since the marginal score is typically intractable, one may instead use the conditional objective

$$
\mathcal{L}_{\mathrm{CSM}}(\theta) := \frac{1}{2}\int_0^1 \lambda(t)\,\mathbb{E}_{X_1,\,X_t \sim p_t(\cdot \mid X_1)}\left[\|s_\theta(X_t, t) - \nabla \log p_t(X_t \mid X_1)\|_2^2\right]\mathrm{d}t. \tag{112}
$$

This is the conditional score-matching counterpart of conditional flow matching.

**Theorem 8.6** (Conditional score matching is a proxy for marginal score matching). *The objectives (111) and (112) differ only by a constant independent of \(\theta\). Equivalently,*

$$
\mathcal{L}_{\mathrm{CSM}}(\theta) = \mathcal{L}_{\mathrm{SM}}(\theta) + C.
$$

*Proof.* Fix \(t\) and define

$$
Z := X_t, \qquad \eta := \nabla \log p_t(X_t \mid X_1), \qquad a(Z) := s_\theta(X_t, t).
$$

By Fisher's identity,

$$
\mathbb{E}[\eta \mid Z] = \nabla \log p_t(Z).
$$

Applying the orthogonality identity from Appendix H gives

$$
\mathbb{E}\|a(Z) - \eta\|_2^2 = \mathbb{E}\|a(Z) - \mathbb{E}[\eta \mid Z]\|_2^2 + \mathbb{E}\|\eta - \mathbb{E}[\eta \mid Z]\|_2^2.
$$

Hence

$$
\mathbb{E}\|s_\theta(X_t, t) - \nabla \log p_t(X_t \mid X_1)\|_2^2 = \mathbb{E}\|s_\theta(X_t, t) - \nabla \log p_t(X_t)\|_2^2 + C_t,
$$

where \(C_t\) does not depend on \(\theta\). Integrating over \(t\) yields the result. â–¡

**Conditional denoising score matching.** Using (106) and the conditional reparameterization

$$
X_t = \alpha_t X_1 + \sigma_t\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I),
$$

we have

$$
\nabla \log p_t(X_t \mid X_1) = -\frac{\varepsilon}{\sigma_t}.
$$

Therefore the conditional score-matching loss (112) can be reparameterized into the denoising form. Define

$$
\epsilon_\theta(x, t) := -\sigma_t s_\theta(x, t).
$$

Then (112) is equivalent, after absorbing the factor \(\sigma_t^{-2}\) into the time weight, to

$$
\mathcal{L}_{\mathrm{DSM}}(\theta) := \frac{1}{2}\int_0^1 \omega(t)\,\mathbb{E}_{X_1,\varepsilon}\left[\|\epsilon_\theta(\alpha_t X_1 + \sigma_t\varepsilon, t) - \varepsilon\|_2^2\right]\mathrm{d}t. \tag{113}
$$

This is precisely the denoising-score-matching route that leads to the score-based SDE framework.

**Learned generative SDE.** Once the score has been learned, the forward generative SDE is

$$
\mathrm{d}X_t = \left(f_t X_t + g_t^2 s_\theta(X_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}W_t, \qquad X_0 \sim p_0, \tag{114}
$$

or, equivalently, in noise-prediction form,

$$
\mathrm{d}X_t = \left(f_t X_t - \frac{g_t^2}{\sigma_t}\epsilon_\theta(X_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}W_t, \qquad X_0 \sim p_0. \tag{115}
$$

This is the exact forward generative viewpoint of [28]: one directly learns a noise-to-data SDE, and the forward SDE itself performs sampling.

45

<!-- page: 46 -->

## 9 Diffusion Language Models in Continuous Embedding Space

Diffusion language models face a structural challenge that image diffusion models do not: language is discrete, while the reverse ODE/SDE framework developed in this tutorial is continuous. A common solution is to embed tokens into a continuous space, run diffusion on those embeddings, and only at the end project the denoised embeddings back to vocabulary items. This idea underlies Diffusion-LM [12], self-conditioned embedding diffusion [29], and conditional generation models such as DiffuSeq [5]. In this section we follow the prompt-response formulation summarized in Figures 4 and 5: the prompt embedding remains clean and acts as a condition, while only the response embedding is noised and denoised.

### 9.1 Prompt-Response Formulation

Let the prompt and response tokens be

$$
\{p, w\} = \{p_1, \ldots, p_n, w_1, \ldots, w_L\}, \qquad p_j, w_i \in \mathcal{V},
$$

where \(\mathcal{V}\) is the vocabulary. Let

$$
E \in \mathbb{R}^{d \times |\mathcal{V}|}
$$

be a *frozen* embedding table, and let \(e(v) \in \mathbb{R}^d\) denote the column of \(E\) associated with token \(v\). We split the clean sequence embedding into a prompt part and a response part:

$$
c_0 := E[\mathrm{onehot}(p_1), \ldots, \mathrm{onehot}(p_n)] \in \mathbb{R}^{d \times n}, \tag{116}
$$

$$
x_0 := E[\mathrm{onehot}(w_1), \ldots, \mathrm{onehot}(w_L)] \in \mathbb{R}^{d \times L}. \tag{117}
$$

The prompt embedding \(c_0\) is kept fixed during both training and inference. Diffusion is applied only to the response block:

$$
x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1 - \bar{\alpha}_t}\,\varepsilon, \qquad \varepsilon \sim \mathcal{N}(0, I), \tag{118}
$$

where \(\bar{\alpha}_t\) decreases from \(\bar{\alpha}_0 = 1\) to \(\bar{\alpha}_1 = 0\). A simple schedule often used in practice is

$$
\bar{\alpha}_t = 1 - \sqrt{t}, \qquad t \in [0, 1]. \tag{119}
$$

Thus the model sees the mixed state \(\{c_0, x_t\}\): the prompt side stays clean, while the response side gradually transitions from clean embeddings to Gaussian noise.

### 9.2 Training Objective

The denoiser predicts the clean response embedding from the noisy response and the clean prompt:

$$
\hat{x}_0 = f_\theta(c_0, x_t, t) \in \mathbb{R}^{d \times L}. \tag{120}
$$

To map this continuous prediction back toward the vocabulary, one forms rounding logits

$$
\hat{l} = E^\top \hat{x}_0 \in \mathbb{R}^{|\mathcal{V}| \times L}. \tag{121}
$$

The training loss in this formulation has two terms. The first is the clean-embedding regression loss

$$
\mathcal{L}_{x_0}(\theta) := \mathbb{E}_{x_0, t, \varepsilon}\left[\|\hat{x}_0 - x_0\|_2^2\right], \tag{122}
$$

46

<!-- page: 47 -->

[FIGURE: Figure 4: Training pipeline for a prompt-conditioned diffusion language model in continuous embedding space.]

Text in figure:

- Rounding logits \(\hat{l}\)
- \(\hat{l} = E^T \cdot \hat{x}_0\)
- Predicted \(\hat{x}_0\)
- \(f_\theta(c_0, x_t, t)\)
- \(\{c_0, x_t\}\)
- \(x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1 - \bar{\alpha}_t}\epsilon\)
- Clean token embedding \(\{c_0, x_0\}\)
- Tokenizer&Embed Table
- Prompt p + Response w
- How to make diffusion great again?
- Combine it with RL algorithm.

Figure 4: Training pipeline for a prompt-conditioned diffusion language model in continuous embedding space. Only the response embedding \(x_0\) is noised; the prompt embedding \(c_0\) remains fixed.

and the second is the rounding loss

$$
\mathcal{L}_{\mathrm{round}}(\theta) := \mathbb{E}_{w, t, \varepsilon}\left[\frac{1}{L}\sum_{i=1}^{L}\mathrm{CE}\big(\hat{l}_i, \mathrm{onehot}(w_i)\big)\right]. \tag{123}
$$

The total training objective is

$$
\mathcal{L}_{\mathrm{total}}(\theta) := \lambda_{x_0}\mathcal{L}_{x_0}(\theta) + \lambda_{\mathrm{round}}\mathcal{L}_{\mathrm{round}}(\theta), \tag{124}
$$

where \(\lambda_{x_0}\) and \(\lambda_{\mathrm{round}}\) balance continuous denoising and discrete token recovery.

This choice is natural for language. The \(x_0\) loss encourages the denoiser to land on the clean response embedding manifold, while the rounding loss makes the projected logits agree with the target tokens. In contrast to image diffusion, where continuous outputs are already valid samples, language requires this extra discrete-alignment term because the final generation must return vocabulary items rather than arbitrary vectors.

47

<!-- page: 48 -->

**Algorithm 1: Training a Prompt-Conditioned Diffusion Language Model**

1. Sample a prompt-response pair \(\{p, w\}\) from the training corpus.

2. Compute the clean prompt embedding \(c_0\) by (116) and the clean response embedding \(x_0\) by (117).

3. Sample a diffusion time \(t \sim \mathrm{Uniform}(0, 1)\) and Gaussian noise \(\varepsilon \sim \mathcal{N}(0, I)\).

4. Construct the noisy response embedding

$$
x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1 - \bar{\alpha}_t}\,\varepsilon.
$$

5. Predict the clean response embedding

$$
\hat{x}_0 = f_\theta(c_0, x_t, t).
$$

6. Form rounding logits

$$
\hat{l} = E^\top \hat{x}_0.
$$

7. Compute the losses (122) and (123), then update \(\theta\) using (124).

### 9.3 Inference by DDIM-Stochastic Rollout

At inference time, the prompt remains fixed and only the response is generated. Given a prompt

$$
p = \{p_1, \ldots, p_n\},
$$

one first computes the prompt embedding \(c_0\). If the total sequence length is fixed to \(T\), then the response length is set to

$$
L = T - n.
$$

The initial response embedding is sampled from Gaussian noise:

$$
x_1 \sim \mathcal{N}(0, \lambda_E^2 I), \tag{125}
$$

where \(\lambda_E\) is the root-mean-square scale of the embedding table. One then chooses a reverse grid

$$
1 = t_1 > t_2 > \cdots > t_K = \mathrm{EPS}, \qquad s_i := t_{i+1}.
$$

At each step, the denoiser predicts a clean response embedding and then uses a DDIM-style stochastic update.

The basic per-step quantities are:

$$
\hat{x}_0^{(i)} = f_\theta(c_0, x_{t_i}, t_i), \tag{126}
$$

$$
\epsilon_{\mathrm{pred}}^{(i)} := \frac{x_{t_i} - \sqrt{\bar{\alpha}_{t_i}}\hat{x}_0^{(i)}}{\sqrt{1 - \bar{\alpha}_{t_i}}}, \tag{127}
$$

$$
\sigma_i := \eta\sqrt{\frac{1 - \bar{\alpha}_{s_i}}{1 - \bar{\alpha}_{t_i}}}\sqrt{1 - \frac{\bar{\alpha}_{t_i}}{\bar{\alpha}_{s_i}}}, \tag{128}
$$

$$
\mu^{(i)} := \sqrt{\bar{\alpha}_{s_i}}\,\hat{x}_0^{(i)} + \sqrt{1 - \bar{\alpha}_{s_i} - \sigma_i^2}\,\epsilon_{\mathrm{pred}}^{(i)}, \tag{129}
$$

$$
x_{s_i} = \mu^{(i)} + \sigma_i\xi_i, \qquad \xi_i \sim \mathcal{N}(0, I). \tag{130}
$$

Here \(\eta \geq 0\) controls the amount of randomness: \(\eta = 0\) gives the deterministic DDIM limit, while \(\eta > 0\) yields a stochastic rollout.

48

<!-- page: 49 -->

[FIGURE: Figure 5: Inference pipeline for a diffusion language model.]

Text in figure:

- \(1 = t_1 > \ldots > t_K = \mathrm{EPS}\)
- Combine it with RL algorithm.
- Decode
- Rounding logits \(\hat{l}\)
- \(\hat{l} = E^T \cdot \hat{x}_0\)
- Clean prompt+predicted clean response \(\{c_0, \hat{x}_0\}\)
- \(f_\theta(c_0, x_{t_K}, t_K)\)
- Clean prompt+Noisy response \(\{c_0, x_{t_K}\}\)
- DDIM-Stochastic Sample
- Clean prompt+Noisy response \(\{c_0, x_{t_2}\}\)
- DDIM-Stochastic Sample
- Clean prompt+ Pure gaussian noise \(\{c_0, x_{t_1}\}\)
- \(\sim \mathcal{N}(0, \lambda_E^2 I)\)
- Tokenizer&Embed Table
- Prompt p
- How to make diffusion great again?

Figure 5: Inference pipeline for a diffusion language model. The prompt embedding remains fixed, while the response embedding is iteratively denoised from Gaussian noise to discrete tokens.

**Algorithm 2: DDIM-Stochastic Inference for Prompt-Conditioned Text Generation**

1. Given a prompt \(p = \{p_1, \ldots, p_n\}\), compute its clean embedding \(c_0\) by (116).

2. Fix a total sequence length \(T\) and set the response length to \(L = T - n\).

3. Sample the initial noisy response embedding \(x_1 \sim \mathcal{N}(0, \lambda_E^2 I)\).

4. Choose a reverse grid \(1 = t_1 > \cdots > t_K = \mathrm{EPS}\) and set \(s_i = t_{i+1}\).

5. For \(i = 1, \ldots, K - 1\):

   a. predict \(\hat{x}_0^{(i)}\) using (126);

   b. compute \(\epsilon_{\mathrm{pred}}^{(i)}\) by (127);

   c. compute \(\sigma_i\) and \(\mu^{(i)}\) by (128)â€“(129);

   d. sample \(x_{s_i}\) by (130).

6. Compute the final clean response embedding

$$
\hat{x}_0 = f_\theta(c_0, x_{\mathrm{EPS}}, \mathrm{EPS}).
$$

7. Decode the response by rounding logits (121), and return the generated tokens \(\hat{w}\).

### 9.4 Connection to the Reverse ODE/SDE Framework

The connection with the main body of this tutorial is now transparent. The response embedding \(x_t\) is simply a continuous state variable conditioned on the fixed prompt embedding \(c_0\). Therefore the

49

<!-- page: 50 -->

reverse-time theory of Sections 3â€“5 applies verbatim to the conditional density

$$
p_t(x_t \mid c_0).
$$

If we write

$$
\alpha_t := \sqrt{\bar{\alpha}_t}, \qquad \sigma_t := \sqrt{1 - \bar{\alpha}_t},
$$

and define \(f_t\) and \(g_t\) from \(\alpha_t\) and \(\sigma_t\) exactly as in the Setup section, then the forward perturbation (118) has exactly the same Gaussian form as the forward processes studied earlier:

$$
x_t = \alpha_t x_0 + \sigma_t \varepsilon.
$$

Consequently, the reverse SDE is

$$
\mathrm{d}x_t = \left(f_t x_t - g_t^2 \nabla_{x_t}\log p_t(x_t \mid c_0)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0, \tag{131}
$$

and the reverse probability-flow ODE is

$$
\frac{\mathrm{d}x_t}{\mathrm{d}t} = f_t x_t - \frac{1}{2}g_t^2 \nabla_{x_t}\log p_t(x_t \mid c_0). \tag{132}
$$

In many diffusion language models, the network predicts \(x_0\) rather than \(\varepsilon\). However, the two parameterizations are equivalent under the Gaussian forward process:

$$
\epsilon_\theta(c_0, x_t, t) := \frac{x_t - \sqrt{\bar{\alpha}_t}\,\hat{x}_0}{\sqrt{1 - \bar{\alpha}_t}}, \qquad \hat{x}_0 = f_\theta(c_0, x_t, t). \tag{133}
$$

This induced noise predictor determines an induced score model

$$
s_\theta(c_0, x_t, t) := -\frac{1}{\sqrt{1 - \bar{\alpha}_t}}\,\epsilon_\theta(c_0, x_t, t). \tag{134}
$$

Therefore the learned reverse SDE can be written as

$$
\mathrm{d}x_t = \left(f_t x_t - g_t^2 s_\theta(c_0, x_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \tag{135}
$$

or equivalently in noise-prediction form,

$$
\mathrm{d}x_t = \left(f_t x_t + \frac{g_t^2}{\sqrt{1 - \bar{\alpha}_t}}\,\epsilon_\theta(c_0, x_t, t)\right)\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t. \tag{136}
$$

The corresponding reverse ODE is

$$
\frac{\mathrm{d}x_t}{\mathrm{d}t} = f_t x_t + \frac{g_t^2}{2\sqrt{1 - \bar{\alpha}_t}}\,\epsilon_\theta(c_0, x_t, t). \tag{137}
$$

This perspective explains the inference formulas above. The DDIM-stochastic rollout is simply a discrete sampler built from the same reverse-time objects:

- when \(\eta = 0\), the update becomes deterministic and is best viewed as an ODE-like sampler;

- when \(\eta > 0\), extra Gaussian noise is injected and the rollout becomes SDE-like.

50

<!-- page: 51 -->

### 9.5 A Brief Note on Discrete Diffusion LLMs

Not all diffusion language models work in a continuous embedding space. A different line of work studies *discrete* diffusion language models, where the state at every time step is still a token sequence rather than a real-valued embedding sequence. A standard construction is to define a categorical forward corruption process that gradually replaces clean tokens by a special absorbing symbol such as \(\langle\mathrm{MASK}\rangle\), or more generally applies a discrete transition matrix over the vocabulary [2]. The reverse model then predicts the previous-token distribution \(p_\theta(x_{t-1} \mid x_t, c)\) and generation proceeds by iterative parallel unmasking and refinement.

The high-level intuition is still diffusion-like: one starts from a heavily corrupted sequence and repeatedly denoises it. However, the mathematical objects are different from those in the present tutorial. In discrete diffusion, the forward and reverse dynamics are Markov chains on a finite state space, or in the continuous-time limit Markov jump processes, rather than ODEs or SDEs on \(\mathbb{R}^d\). Accordingly, the central quantities are transition matrices and categorical posterior distributions, not vector fields, Brownian noise, or score functions \(\nabla \log p_t(x)\).

For this reason, discrete diffusion LLMs are *not* our main concern in this tutorial. Our focus is the continuous reverse ODE/SDE framework, where the state variable lives in a Euclidean space and the learned object is a score, noise predictor, or induced reverse vector field. Discrete diffusion is an important parallel direction for language modeling, especially for \(\langle\mathrm{MASK}\rangle\)-prediction style generation, but it requires a different probabilistic formalism from the one developed here.

51

<!-- page: 52 -->

## A Differential Operators

This appendix records the basic differential operators used throughout the tutorial.

Let

$$
x = (x_1, \ldots, x_d) \in \mathbb{R}^d.
$$

**Definition A.1** (Gradient). *If \(f : \mathbb{R}^d \to \mathbb{R}\) is a scalar-valued differentiable function, its gradient is the vector field*

$$
\nabla f(x) := \left(\frac{\partial f}{\partial x_1}(x), \ldots, \frac{\partial f}{\partial x_d}(x)\right)^\top.
$$

Thus the gradient maps a scalar function to a vector field.

**Definition A.2** (Divergence). *If \(v : \mathbb{R}^d \to \mathbb{R}^d\) is a differentiable vector field with components*

$$
v(x) = \big(v_1(x), \ldots, v_d(x)\big)^\top,
$$

*its divergence is the scalar function*

$$
\nabla \cdot v(x) := \sum_{i=1}^{d}\frac{\partial v_i}{\partial x_i}(x).
$$

Thus the divergence maps a vector field to a scalar function.

**Definition A.3** (Laplacian). *If \(f : \mathbb{R}^d \to \mathbb{R}\) is twice differentiable, its Laplacian is*

$$
\Delta f(x) := \nabla \cdot (\nabla f(x)) = \sum_{i=1}^{d}\frac{\partial^2 f}{\partial x_i^2}(x).
$$

Thus the Laplacian maps a scalar function to a scalar function.

For completeness, if \(v : \mathbb{R}^d \to \mathbb{R}^d\) is a differentiable vector field, then \(\nabla v(x)\) denotes its Jacobian matrix,

$$
\nabla v(x) := \left(\frac{\partial v_i}{\partial x_j}(x)\right)_{i,j=1}^{d}.
$$

This notation should not be confused with the divergence \(\nabla \cdot v(x)\), which is the trace of this Jacobian matrix.

## B Brownian Motion in Forward and Reverse Time

This appendix clarifies the three noise symbols that appear in the main text:

$$
W_t, \qquad W_\tau^{\mathrm{rev}}, \qquad \bar{W}_t.
$$

They are related, but they play different conceptual roles. The main source of confusion is that standard Brownian motion is defined with respect to an increasing time parameter, whereas the reverse SDE is often rewritten in the original label \(t\) with the convention \(t : 1 \to 0\).

52

<!-- page: 53 -->

**Forward Brownian motion**

The forward diffusion is written in the increasing time variable \(t \in [0, 1]\) as

$$
\mathrm{d}X_t = b_t(X_t)\,\mathrm{d}t + g_t\,\mathrm{d}W_t.
$$

For the Brownian motion itself, the most natural filtration is the Brownian filtration

$$
\mathcal{F}_t^W := \sigma(W_s : 0 \leq s \leq t),
$$

or an augmentation of it. The forward process \(X_t\) has its own natural filtration

$$
\mathcal{F}_t^X := \sigma(X_s : 0 \leq s \leq t).
$$

In a strong-solution setting one usually works with a filtration \((\mathcal{F}_t)_{0 \leq t \leq 1}\) large enough that both \(X_t\) and \(W_t\) are adapted, for example

$$
\mathcal{F}_t^X \subseteq \mathcal{F}_t \supseteq \mathcal{F}_t^W.
$$

For the definition of Brownian motion, however, it is conceptually cleaner to refer to \(\mathcal{F}_t^W\) rather than to \(\mathcal{F}_t^X\).

By definition, \(W_t\) is a standard Brownian motion if:

1. \(W_0 = 0\) almost surely;

2. for every \(0 \leq s < t \leq 1\), the increment \(W_t - W_s\) is Gaussian with mean 0 and covariance \((t - s)I\);

3. for every \(0 \leq s < t \leq 1\), the increment \(W_t - W_s\) is independent of \(\mathcal{F}_s^W\).

Thus \(W_t\) is a forward-time noise process. It is attached to the forward SDE and to the forward filtration.

**Reverse process and reverse-time filtration**

The reverse process is defined by

$$
Y_\tau := X_{1-\tau}, \qquad 0 \leq \tau \leq 1.
$$

The reverse process has its own natural filtration

$$
\mathcal{G}_\tau^Y := \sigma(Y_s : 0 \leq s \leq \tau) = \sigma(X_{1-s} : 0 \leq s \leq \tau).
$$

This filtration grows as \(\tau\) increases from 0 to 1. Therefore \(\tau\) is the natural forward time variable for the reverse process.

The reverse Brownian motion \(W_\tau^{\mathrm{rev}}\) also has its own Brownian filtration

$$
\mathcal{G}_\tau^{W^{\mathrm{rev}}} := \sigma(W_\rho^{\mathrm{rev}} : 0 \leq \rho \leq \tau).
$$

These two filtrations play different roles:

- \(\mathcal{G}_\tau^Y\) records the reverse-time information carried by the reverse process;

- \(\mathcal{G}_\tau^{W^{\mathrm{rev}}}\) is the natural filtration of the reverse Brownian driver itself.

53

<!-- page: 54 -->

For a rigorous reverse SDE, one works on a filtration large enough to support both objects.

The relationship with the forward filtration is as follows. The forward Brownian filtration

$$
\mathcal{F}_t^W = \sigma(W_s : 0 \leq s \leq t)
$$

and the reverse Brownian filtration

$$
\mathcal{G}_\tau^{W^{\mathrm{rev}}} = \sigma(W_\rho^{\mathrm{rev}} : 0 \leq \rho \leq \tau)
$$

play analogous roles, but they are attached to different Brownian motions and different time directions. Likewise, the forward process filtration

$$
\mathcal{F}_t^X = \sigma(X_s : 0 \leq s \leq t)
$$

and the reverse process filtration

$$
\mathcal{G}_\tau^Y = \sigma(Y_s : 0 \leq s \leq \tau)
$$

describe information revealed along the forward and reverse evolutions, respectively. In general these forward and reverse filtrations should not be identified with one another, and there is typically no simple inclusion relation between them. They are different increasing families of sigma-algebras adapted to different time parameterizations.

When the reverse diffusion theorem is stated in the variable \(\tau\), the reverse SDE has the form

$$
\mathrm{d}Y_\tau = b_\tau^{\mathrm{rev}}(Y_\tau)\,\mathrm{d}\tau + g_{1-\tau}\,\mathrm{d}W_\tau^{\mathrm{rev}},
$$

where \(W_\tau^{\mathrm{rev}}\) is a standard Brownian motion with respect to its Brownian filtration \(\mathcal{G}_\tau^{W^{\mathrm{rev}}}\), or with respect to an augmented filtration that also makes \(Y_\tau\) adapted. Concretely, this means:

1. \(W_0^{\mathrm{rev}} = 0\) almost surely;

2. for every \(0 \leq \rho < \tau \leq 1\),

$$
W_\tau^{\mathrm{rev}} - W_\rho^{\mathrm{rev}} \sim \mathcal{N}(0, (\tau - \rho)I);
$$

3. for every \(0 \leq \rho < \tau \leq 1\), the increment \(W_\tau^{\mathrm{rev}} - W_\rho^{\mathrm{rev}}\) is independent of the past Brownian filtration \(\mathcal{G}_\rho^{W^{\mathrm{rev}}}\).

The crucial point is that \(W_\tau^{\mathrm{rev}}\) is the Brownian driver of the reverse diffusion. It is not the same symbol as the forward Brownian motion \(W_t\), because it is attached to a different Brownian filtration and a different stochastic evolution. At the same time, the reverse SDE itself is naturally interpreted relative to the reverse-process filtration \(\mathcal{G}_\tau^Y\), because that filtration records the information carried by the reversed trajectory.

**Backward-\(t\) notation and the definition of \(\bar{W}_t\)**

The same reverse diffusion may be rewritten in the original time label \(t\) by setting

$$
t = 1 - \tau.
$$

Because the reverse process is still the same stochastic process viewed under a different clock, it is natural to define

$$
\bar{W}_t := W_{1-t}^{\mathrm{rev}}, \qquad t : 1 \to 0.
$$

54

<!-- page: 55 -->

With this notation, the reverse SDE written in the original label becomes

$$
\mathrm{d}X_t = \big(b_t(X_t) - g_t^2 \nabla \log p_t(X_t)\big)\,\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \qquad t : 1 \to 0.
$$

The notation \(\bar{W}_t\) emphasizes that this is the same reverse-time noise as \(W_\tau^{\mathrm{rev}}\), but expressed in the backward label \(t\). The symbol \(\bar{W}_t\) should therefore be interpreted as a *reverse-time noise driver*. It is not introduced as a new forward-time Brownian motion in the increasing variable \(t\).

The corresponding backward-\(t\) filtration is obtained by relabeling the reverse-time filtration:

$$
\bar{\mathcal{G}}_t^X := \mathcal{G}_{1-t}^Y = \sigma(X_s : t \leq s \leq 1).
$$

Likewise, the Brownian filtration of the reverse noise may be rewritten as

$$
\bar{\mathcal{G}}_t^{\bar{W}} := \mathcal{G}_{1-t}^{W^{\mathrm{rev}}} = \sigma(\bar{W}_s : t \leq s \leq 1).
$$

The family \(\bar{\mathcal{G}}_t^X\) is decreasing when \(t\) is read in the ordinary increasing direction, but it is increasing when the reverse SDE is read in its natural orientation \(t : 1 \to 0\). The same is true for \(\bar{\mathcal{G}}_t^{\bar{W}}\). Thus \(\bar{W}_t\) is the backward-\(t\) representation of the reverse Brownian driver, while \(\bar{\mathcal{G}}_t^X\) records the backward-time information of the reverse process itself.

**Which symbols are standard Brownian motions?**

The correct classification is:

- \(W_t\) is a standard Brownian motion in the increasing forward time variable \(t \in [0, 1]\), naturally associated with the filtration \(\mathcal{F}_t^W\).

- \(W_\tau^{\mathrm{rev}}\) is a standard Brownian motion in the increasing reverse-time variable \(\tau \in [0, 1]\), naturally associated with the filtration \(\mathcal{G}_\tau^{W^{\mathrm{rev}}}\).

- \(\bar{W}_t\) is the same reverse-time noise as \(W_\tau^{\mathrm{rev}}\), rewritten in the label \(t = 1 - \tau\). It is naturally associated with the relabeled Brownian filtration \(\bar{\mathcal{G}}_t^{\bar{W}}\) and is not, by itself, introduced as a standard Brownian motion in increasing \(t\).

Indeed,

$$
\bar{W}_1 = W_0^{\mathrm{rev}} = 0, \qquad \bar{W}_0 = W_1^{\mathrm{rev}}.
$$

So \(\bar{W}_t\) starts at zero when the parameter is read from \(t = 1\) down to \(t = 0\), exactly as the backward formulation of the reverse SDE requires.

**Summary**

The three symbols may be summarized as follows:

$$
\begin{aligned}
\text{forward SDE in } t : \quad &\mathrm{d}X_t = b_t(X_t)\,\mathrm{d}t + g_t\,\mathrm{d}W_t,\\
\text{reverse SDE in } \tau : \quad &\mathrm{d}Y_\tau = b_\tau^{\mathrm{rev}}(Y_\tau)\,\mathrm{d}\tau + g_{1-\tau}\,\mathrm{d}W_\tau^{\mathrm{rev}},\\
\text{same reverse SDE in } t : \quad &\mathrm{d}X_t = \big(b_t(X_t) - g_t^2\nabla \log p_t(X_t)\big)\,\mathrm{d}t + g_t\,\mathrm{d}\bar{W}_t, \quad t : 1 \to 0,\\
&\bar{W}_t = W_{1-t}^{\mathrm{rev}}.
\end{aligned}
$$

This is the precise sense in which \(W_\tau^{\mathrm{rev}}\) and \(\bar{W}_t\) represent the same reverse-time noise under two different clocks.

55

<!-- page: 56 -->

## C Deterministic ItĂ´ Integrals and ItĂ´ Isometry

This appendix explains the stochastic-integral step used in Section 7 when comparing DDPM sampling with the reverse SDE. The key object there is an integral of the form

$$
\eta := \int_a^b \phi(\tau)\,\mathrm{d}W_\tau,
$$

where \(W_\tau\) is a standard Brownian motion and \(\phi\) is a deterministic scalar function. The conclusion used in the main text is that \(\eta\) is Gaussian with mean zero and variance

$$
\mathbb{E}_W[\eta^2] = \int_a^b \phi(\tau)^2\,\mathrm{d}\tau.
$$

In the vector-valued case relevant to diffusion models, the same statement holds componentwise, yielding covariance

$$
\mathbb{E}_W[\eta\eta^\top] = \left(\int_a^b \phi(\tau)^2\,\mathrm{d}\tau\right)I.
$$

**What does \(\mathbb{E}_W[\eta]\) mean?**

Some readers may be unfamiliar with notation such as \(\mathbb{E}_W[\eta]\). The meaning is simple: it denotes expectation with respect to the randomness of the Brownian motion \(W\).

Formally, let \((\Omega, \mathcal{F}, \mathbb{P})\) be the underlying probability space, and let

$$
W_\tau = W_\tau(\omega), \qquad \omega \in \Omega,
$$

be a Brownian motion on that space. Then the stochastic integral

$$
\eta = \int_a^b \phi(\tau)\,\mathrm{d}W_\tau
$$

is itself a random variable on \(\Omega\), that is,

$$
\eta = \eta(\omega).
$$

Therefore

$$
\mathbb{E}_W[\eta]
$$

simply means

$$
\mathbb{E}[\eta] = \int_\Omega \eta(\omega)\,\mathrm{d}\mathbb{P}(\omega),
$$

with the subscript \(W\) added only to remind the reader that the randomness comes from the Brownian path \(W\). In the present appendix, there is no additional source of randomness, so

$$
\mathbb{E}_W[\eta] = \mathbb{E}[\eta].
$$

Likewise,

$$
\mathbb{E}_W[\eta^2] = \mathbb{E}[\eta^2], \qquad \mathbb{E}_W[\eta\eta^\top] = \mathbb{E}[\eta\eta^\top].
$$

We keep the subscript \(W\) only as a bookkeeping device indicating that the expectation is taken over Brownian trajectories.

56

<!-- page: 57 -->

**Step 1: the case of a step-function integrand**

Suppose first that

$$
\phi(\tau) = \sum_{j=0}^{m-1} c_j \mathbf{1}_{(u_j, u_{j+1}]}(\tau), \qquad a = u_0 < u_1 < \cdots < u_m = b,
$$

where each \(c_j \in \mathbb{R}\) is deterministic. By definition of the ItĂ´ integral for step functions,

$$
\int_a^b \phi(\tau)\,\mathrm{d}W_\tau := \sum_{j=0}^{m-1} c_j\big(W_{u_{j+1}} - W_{u_j}\big).
$$

Each increment

$$
W_{u_{j+1}} - W_{u_j}
$$

is Gaussian with mean zero and variance \(u_{j+1} - u_j\), and the increments over disjoint intervals are independent. Therefore the random variable

$$
\eta := \sum_{j=0}^{m-1} c_j\big(W_{u_{j+1}} - W_{u_j}\big)
$$

is a linear combination of independent Gaussian random variables, hence itself Gaussian.

Its mean is

$$
\mathbb{E}_W[\eta] = \sum_{j=0}^{m-1} c_j\,\mathbb{E}_W[W_{u_{j+1}} - W_{u_j}] = 0.
$$

Its variance is

$$
\begin{aligned}
\mathbb{E}_W[\eta^2] &= \mathbb{E}_W\left[\left(\sum_{j=0}^{m-1}c_j(W_{u_{j+1}} - W_{u_j})\right)^2\right]\\
&= \sum_{j=0}^{m-1}c_j^2\,\mathbb{E}_W[(W_{u_{j+1}} - W_{u_j})^2] + 2\sum_{0 \leq i < j \leq m-1}c_i c_j\,\mathbb{E}_W[(W_{u_{i+1}} - W_{u_i})(W_{u_{j+1}} - W_{u_j})].
\end{aligned}
$$

The cross terms vanish because disjoint Brownian increments are independent and centered:

$$
\mathbb{E}_W[(W_{u_{i+1}} - W_{u_i})(W_{u_{j+1}} - W_{u_j})] = \mathbb{E}_W[W_{u_{i+1}} - W_{u_i}]\,\mathbb{E}_W[W_{u_{j+1}} - W_{u_j}] = 0 \qquad (i \neq j).
$$

Hence

$$
\begin{aligned}
\mathbb{E}_W[\eta^2] &= \sum_{j=0}^{m-1}c_j^2\,\mathbb{E}_W[(W_{u_{j+1}} - W_{u_j})^2]\\
&= \sum_{j=0}^{m-1}c_j^2\,(u_{j+1} - u_j).
\end{aligned}
$$

But this sum is exactly

$$
\int_a^b \phi(\tau)^2\,\mathrm{d}\tau.
$$

Therefore, for step-function integrands,

$$
\boxed{\int_a^b \phi(\tau)\,\mathrm{d}W_\tau \sim \mathcal{N}\left(0, \int_a^b \phi(\tau)^2\,\mathrm{d}\tau\right).}
$$

This identity is the deterministic step-function case of ItĂ´ isometry.

57

<!-- page: 58 -->

**Step 2: extension to general deterministic integrands**

Now let \(\phi \in L^2([a, b])\) be any deterministic square-integrable function. By the standard construction of the ItĂ´ integral, there exists a sequence of step functions \(\phi_n\) such that

$$
\int_a^b |\phi_n(\tau) - \phi(\tau)|^2\,\mathrm{d}\tau \to 0.
$$

For each \(n\), define

$$
\eta_n := \int_a^b \phi_n(\tau)\,\mathrm{d}W_\tau.
$$

From Step 1,

$$
\mathbb{E}_W[\eta_n] = 0, \qquad \mathbb{E}_W[\eta_n^2] = \int_a^b \phi_n(\tau)^2\,\mathrm{d}\tau.
$$

Moreover,

$$
\eta_n - \eta_m = \int_a^b \big(\phi_n(\tau) - \phi_m(\tau)\big)\,\mathrm{d}W_\tau,
$$

so Step 1 again gives

$$
\mathbb{E}_W[(\eta_n - \eta_m)^2] = \int_a^b |\phi_n(\tau) - \phi_m(\tau)|^2\,\mathrm{d}\tau.
$$

Since \((\phi_n)\) is Cauchy in \(L^2([a, b])\), the sequence \((\eta_n)\) is Cauchy in \(L^2(\Omega)\) and therefore converges in \(L^2\) to a limit, which is by definition

$$
\eta := \int_a^b \phi(\tau)\,\mathrm{d}W_\tau.
$$

We now justify the mean and variance formulas carefully.

First, \(L^2\) convergence implies \(L^1\) convergence by Cauchyâ€“Schwarz:

$$
\mathbb{E}_W[|\eta_n - \eta|] \leq \big(\mathbb{E}_W[(\eta_n - \eta)^2]\big)^{1/2} \to 0.
$$

Therefore

$$
\mathbb{E}_W[\eta] = \mathbb{E}_W[\eta_n] + \mathbb{E}_W[\eta - \eta_n].
$$

Taking absolute values and using \(\mathbb{E}_W[\eta_n] = 0\) for every \(n\),

$$
|\mathbb{E}_W[\eta]| \leq |\mathbb{E}_W[\eta_n]| + \mathbb{E}_W[|\eta - \eta_n|] = \mathbb{E}_W[|\eta - \eta_n|].
$$

Letting \(n \to \infty\) gives

$$
\mathbb{E}_W[\eta] = 0.
$$

Next, to compute the second moment, write

$$
\eta^2 - \eta_n^2 = (\eta - \eta_n)(\eta + \eta_n).
$$

Hence

$$
\big|\mathbb{E}_W[\eta^2] - \mathbb{E}_W[\eta_n^2]\big| \leq \mathbb{E}_W[|\eta - \eta_n|\,|\eta + \eta_n|].
$$

By Cauchyâ€“Schwarz,

$$
\mathbb{E}_W[|\eta - \eta_n|\,|\eta + \eta_n|] \leq \big(\mathbb{E}_W[(\eta - \eta_n)^2]\big)^{1/2}\big(\mathbb{E}_W[(\eta + \eta_n)^2]\big)^{1/2}.
$$

58

<!-- page: 59 -->

The first factor tends to zero because \(\eta_n \to \eta\) in \(L^2\). The second factor remains bounded because

$$
\mathbb{E}_W[(\eta + \eta_n)^2] \leq 2\mathbb{E}_W[\eta^2] + 2\mathbb{E}_W[\eta_n^2],
$$

and both terms on the right are finite. Therefore

$$
\mathbb{E}_W[\eta_n^2] \to \mathbb{E}_W[\eta^2].
$$

Since

$$
\mathbb{E}_W[\eta_n^2] = \int_a^b \phi_n(\tau)^2\,\mathrm{d}\tau
$$

and \(\phi_n \to \phi\) in \(L^2([a, b])\), we also have

$$
\int_a^b \phi_n(\tau)^2\,\mathrm{d}\tau \to \int_a^b \phi(\tau)^2\,\mathrm{d}\tau.
$$

Consequently,

$$
\mathbb{E}_W[\eta^2] = \int_a^b \phi(\tau)^2\,\mathrm{d}\tau.
$$

This identity is the deterministic-integrand form of ItĂ´ isometry:

$$
\boxed{\mathbb{E}_W\left[\left(\int_a^b \phi(\tau)\,\mathrm{d}W_\tau\right)^2\right] = \int_a^b \phi(\tau)^2\,\mathrm{d}\tau.}
$$

Because each \(\eta_n\) is Gaussian and the sequence converges in \(L^2\), the limit \(\eta\) is also Gaussian with the same limiting mean and variance. Therefore

$$
\boxed{\int_a^b \phi(\tau)\,\mathrm{d}W_\tau \sim \mathcal{N}\left(0, \int_a^b \phi(\tau)^2\,\mathrm{d}\tau\right)}
$$

for every deterministic \(\phi \in L^2([a, b])\).

**Step 3: the vector-valued case**

In diffusion models, the Brownian motion is \(d\)-dimensional:

$$
W_\tau = (W_\tau^{(1)}, \ldots, W_\tau^{(d)})^\top.
$$

If \(\phi\) is a deterministic scalar function, define

$$
\eta := \int_a^b \phi(\tau)\,\mathrm{d}W_\tau = \left(\int_a^b \phi(\tau)\,\mathrm{d}W_\tau^{(1)}, \ldots, \int_a^b \phi(\tau)\,\mathrm{d}W_\tau^{(d)}\right)^\top.
$$

Each component is Gaussian with mean zero and variance \(\int_a^b \phi(\tau)^2\,\mathrm{d}\tau\). Since the Brownian components are independent, the components of \(\eta\) are independent as well. Consequently,

$$
\eta \sim \mathcal{N}\left(0, \left(\int_a^b \phi(\tau)^2\,\mathrm{d}\tau\right)I\right).
$$

Equivalently,

$$
\mathbb{E}_W[\eta] = 0,
$$

and

$$
\mathbb{E}_W[\eta\eta^\top] = \left(\int_a^b \phi(\tau)^2\,\mathrm{d}\tau\right)I.
$$

59

<!-- page: 60 -->

**Step 4: application to the DDPM/reverse-SDE comparison**

In Section 7, the stochastic term is

$$
\eta_k := \int_{1-t_k}^{1-t_{k-1}}\sqrt{\beta(1-\tau)}\,\mathrm{d}W_\tau^{\mathrm{rev}}.
$$

Here the deterministic integrand is

$$
\phi(\tau) := \sqrt{\beta(1-\tau)}.
$$

Applying the vector-valued result above gives

$$
\mathbb{E}_{W^{\mathrm{rev}}}[\eta_k] = 0
$$

and

$$
\mathbb{E}_{W^{\mathrm{rev}}}[\eta_k\eta_k^\top] = \left(\int_{1-t_k}^{1-t_{k-1}}\beta(1-\tau)\,\mathrm{d}\tau\right)I.
$$

Now make the change of variables

$$
s = 1 - \tau, \qquad \mathrm{d}s = -\,\mathrm{d}\tau.
$$

When \(\tau = 1 - t_k\), we have \(s = t_k\), and when \(\tau = 1 - t_{k-1}\), we have \(s = t_{k-1}\). Therefore

$$
\begin{aligned}
\int_{1-t_k}^{1-t_{k-1}}\beta(1-\tau)\,\mathrm{d}\tau &= \int_{s=t_k}^{s=t_{k-1}}\beta(s)(-\,\mathrm{d}s)\\
&= \int_{t_{k-1}}^{t_k}\beta(s)\,\mathrm{d}s\\
&= h_k.
\end{aligned}
$$

Hence

$$
\mathbb{E}_{W^{\mathrm{rev}}}[\eta_k\eta_k^\top] = h_k I.
$$

Since \(\eta_k\) is Gaussian and centered, this proves

$$
\boxed{\eta_k \sim \mathcal{N}(0, h_k I).}
$$

Therefore one may write

$$
\eta_k = \sqrt{h_k}\,z_k, \qquad z_k \sim \mathcal{N}(0, I),
$$

which is exactly the stochastic increment used in the backward Eulerâ€“Maruyama step of the reverse SDE.

## D Continuity Equation

**Theorem D.1** (Continuity equation). *Let \(X_t\) satisfy the deterministic ODE*

$$
\frac{\mathrm{d}X_t}{\mathrm{d}t} = u_t(X_t),
$$

*and let \(p_t\) denote the density of \(X_t\). Then*

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)u_t(x)\big). \tag{138}
$$

60

<!-- page: 61 -->

*Proof.* Let \(\varphi : \mathbb{R}^d \to \mathbb{R}\) be a smooth compactly supported test function. Since \(\mathrm{d}X_t/\mathrm{d}t = u_t(X_t)\),

$$
\frac{\mathrm{d}}{\mathrm{d}t}\varphi(X_t) = \nabla\varphi(X_t)^\top u_t(X_t).
$$

Taking expectations,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}_{X_t}[\varphi(X_t)] = \mathbb{E}_{X_t}[\nabla\varphi(X_t)^\top u_t(X_t)].
$$

Writing the expectation in terms of the density \(p_t\),

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int \varphi(x)p_t(x)\,\mathrm{d}x = \int \nabla\varphi(x)^\top u_t(x)p_t(x)\,\mathrm{d}x.
$$

Integrating by parts gives

$$
\int \nabla\varphi(x)^\top u_t(x)p_t(x)\,\mathrm{d}x = -\int \varphi(x)\nabla \cdot \big(u_t(x)p_t(x)\big)\,\mathrm{d}x.
$$

Therefore

$$
\int \varphi(x)\partial_t p_t(x)\,\mathrm{d}x = -\int \varphi(x)\nabla \cdot \big(u_t(x)p_t(x)\big)\,\mathrm{d}x.
$$

Since this holds for every test function \(\varphi\), (138) follows. â–¡

## E Fokkerâ€“Planck Equation

**Theorem E.1** (Fokkerâ€“Planck equation). *Let \(X_t\) satisfy the ItĂ´ SDE*

$$
\mathrm{d}X_t = b_t(X_t)\,\mathrm{d}t + g_t\,\mathrm{d}W_t, \tag{139}
$$

*where \(b_t : \mathbb{R}^d \to \mathbb{R}^d\) and \(g_t\) is scalar. Let \(p_t\) be the density of \(X_t\). Then*

$$
\partial_t p_t(x) = -\nabla \cdot \big(b_t(x)p_t(x)\big) + \frac{1}{2}g_t^2\Delta p_t(x). \tag{140}
$$

*Proof.* Let \(\varphi : \mathbb{R}^d \to \mathbb{R}\) be a smooth compactly supported test function. By ItĂ´'s formula,

$$
\mathrm{d}\varphi(X_t) = \nabla\varphi(X_t)^\top \mathrm{d}X_t + \frac{1}{2}\mathrm{tr}\big(g_t^2 I \nabla^2\varphi(X_t)\big)\,\mathrm{d}t.
$$

Substituting (139),

$$
\mathrm{d}\varphi(X_t) = \nabla\varphi(X_t)^\top b_t(X_t)\,\mathrm{d}t + g_t\nabla\varphi(X_t)^\top\,\mathrm{d}W_t + \frac{1}{2}g_t^2\Delta\varphi(X_t)\,\mathrm{d}t.
$$

Taking expectation removes the martingale term:

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}_{X_t}[\varphi(X_t)] = \mathbb{E}_{X_t}[\nabla\varphi(X_t)^\top b_t(X_t)] + \frac{1}{2}g_t^2\mathbb{E}_{X_t}[\Delta\varphi(X_t)].
$$

Writing the expectations using the density,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int \varphi(x)p_t(x)\,\mathrm{d}x = \int \nabla\varphi(x)^\top b_t(x)p_t(x)\,\mathrm{d}x + \frac{1}{2}g_t^2\int \Delta\varphi(x)p_t(x)\,\mathrm{d}x.
$$

Integrating by parts,

$$
\int \nabla\varphi(x)^\top b_t(x)p_t(x)\,\mathrm{d}x = -\int \varphi(x)\nabla \cdot \big(b_t(x)p_t(x)\big)\,\mathrm{d}x,
$$

61

<!-- page: 62 -->

and

$$
\int \Delta\varphi(x)p_t(x)\,\mathrm{d}x = \int \varphi(x)\Delta p_t(x)\,\mathrm{d}x.
$$

Therefore

$$
\int \varphi(x)\partial_t p_t(x)\,\mathrm{d}x = \int \varphi(x)\left[-\nabla \cdot \big(b_t(x)p_t(x)\big) + \frac{1}{2}g_t^2\Delta p_t(x)\right]\mathrm{d}x.
$$

Since this holds for every test function \(\varphi\), (140) follows. â–¡

## F Conditional-to-Marginal Averaging Lemmas

**Lemma F.1** (Averaging continuity equations). *Suppose that for each fixed \(x_0\), a conditional density \(p_t(x \mid x_0)\) satisfies*

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \big(p_t(x \mid x_0)v_t(x \mid x_0)\big).
$$

*Let*

$$
p_t(x) = \int p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0.
$$

*Then the marginal density satisfies*

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)\bar{v}_t(x)\big),
$$

*where*

$$
\bar{v}_t(x) := \mathbb{E}_{X_0 \mid X_t = x}[v_t(x \mid X_0)]. \tag{141}
$$

*Proof.* Differentiate under the integral sign:

$$
\partial_t p_t(x) = \int \partial_t p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0.
$$

Substitute the conditional continuity equation:

$$
\partial_t p_t(x) = -\int \nabla \cdot \big(p_t(x \mid x_0)v_t(x \mid x_0)\big)p_0(x_0)\,\mathrm{d}x_0.
$$

Since the divergence acts only on \(x\), it can be moved outside the integral:

$$
\partial_t p_t(x) = -\nabla \cdot \left(\int p_t(x \mid x_0)v_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\right).
$$

Define

$$
\bar{v}_t(x) := \frac{\int p_t(x \mid x_0)v_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0}{p_t(x)}.
$$

By Bayes' rule, this is exactly (141). Hence

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)\bar{v}_t(x)\big). \qquad \square
$$

**Lemma F.2** (Averaging Fokkerâ€“Planck equations). *Suppose that for each fixed \(x_0\), a conditional density \(p_t(x \mid x_0)\) satisfies*

$$
\partial_t p_t(x \mid x_0) = -\nabla \cdot \big(p_t(x \mid x_0)b_t(x \mid x_0)\big) + \frac{1}{2}g_t^2\Delta p_t(x \mid x_0).
$$

*Then the marginal density*

$$
p_t(x) = \int p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0
$$

62

<!-- page: 63 -->

*satisfies*

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)\bar{b}_t(x)\big) + \frac{1}{2}g_t^2\Delta p_t(x),
$$

*where*

$$
\bar{b}_t(x) := \mathbb{E}_{X_0 \mid X_t = x}[b_t(x \mid X_0)]. \tag{142}
$$

*Proof.* Differentiate under the integral sign:

$$
\partial_t p_t(x) = \int \partial_t p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0.
$$

Substitute the conditional Fokkerâ€“Planck equation:

$$
\begin{aligned}
\partial_t p_t(x) = &-\int \nabla \cdot \big(p_t(x \mid x_0)b_t(x \mid x_0)\big)p_0(x_0)\,\mathrm{d}x_0\\
&+ \frac{1}{2}g_t^2\int \Delta p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0.
\end{aligned}
$$

Move derivatives outside the integrals:

$$
\partial_t p_t(x) = -\nabla \cdot \left(\int p_t(x \mid x_0)b_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0\right) + \frac{1}{2}g_t^2\Delta p_t(x).
$$

Define

$$
\bar{b}_t(x) := \frac{\int p_t(x \mid x_0)b_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0}{p_t(x)}.
$$

By Bayes' rule this is (142), so

$$
\partial_t p_t(x) = -\nabla \cdot \big(p_t(x)\bar{b}_t(x)\big) + \frac{1}{2}g_t^2\Delta p_t(x). \qquad \square
$$

## G Fisher's Identity

**Theorem G.1** (Fisher's identity). *If*

$$
p_t(x) = \int p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0,
$$

*then*

$$
\nabla \log p_t(x) = \mathbb{E}[\nabla \log p_t(x \mid X_0) \mid X_t = x]. \tag{143}
$$

*Proof.* Differentiate the marginal density:

$$
\nabla p_t(x) = \int \nabla p_t(x \mid x_0)p_0(x_0)\,\mathrm{d}x_0.
$$

Divide by \(p_t(x)\):

$$
\nabla \log p_t(x) = \int \frac{\nabla p_t(x \mid x_0)}{p_t(x)}p_0(x_0)\,\mathrm{d}x_0.
$$

Multiply and divide by \(p_t(x \mid x_0)\) inside the integral:

$$
\nabla \log p_t(x) = \int \frac{\nabla p_t(x \mid x_0)}{p_t(x \mid x_0)}\frac{p_t(x \mid x_0)p_0(x_0)}{p_t(x)}\,\mathrm{d}x_0.
$$

The first factor is \(\nabla \log p_t(x \mid x_0)\). The second factor is \(p(x_0 \mid X_t = x)\) by Bayes' rule. Hence

$$
\nabla \log p_t(x) = \int \nabla \log p_t(x \mid x_0)\,p(x_0 \mid X_t = x)\,\mathrm{d}x_0,
$$

which is (143). â–¡

63

<!-- page: 64 -->

## H Orthogonality Identity Used in the Denoising Loss

**Theorem H.1** (Orthogonality identity). *Let \(Z\) and \(\varepsilon\) be square-integrable random variables, and let \(a(Z)\) be any square-integrable function of \(Z\). Then*

$$
\mathbb{E}_{Z,\varepsilon}\|a(Z) - \varepsilon\|_2^2 = \mathbb{E}_Z\|a(Z) - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon]\|_2^2 + \mathbb{E}_{Z,\varepsilon}\|\varepsilon - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon]\|_2^2. \tag{144}
$$

*Proof.* Write

$$
a(Z) - \varepsilon = \big(a(Z) - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon]\big) + \big(\mathbb{E}_{\varepsilon \mid Z}[\varepsilon] - \varepsilon\big).
$$

Let

$$
A := a(Z) - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon], \qquad B := \mathbb{E}_{\varepsilon \mid Z}[\varepsilon] - \varepsilon.
$$

Then

$$
\|A + B\|_2^2 = \|A\|_2^2 + 2A^\top B + \|B\|_2^2.
$$

Taking expectation,

$$
\mathbb{E}_{Z,\varepsilon}\|A + B\|_2^2 = \mathbb{E}_{Z,\varepsilon}\|A\|_2^2 + 2\mathbb{E}_{Z,\varepsilon}[A^\top B] + \mathbb{E}_{Z,\varepsilon}\|B\|_2^2.
$$

Now \(A\) is measurable with respect to \(Z\), and

$$
\mathbb{E}_{\varepsilon \mid Z}[B] = \mathbb{E}_{\varepsilon \mid Z}[\mathbb{E}_{\varepsilon \mid Z}[\varepsilon] - \varepsilon] = \mathbb{E}_{\varepsilon \mid Z}[\varepsilon] - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon] = 0.
$$

Therefore

$$
\mathbb{E}_{Z,\varepsilon}[A^\top B] = \mathbb{E}_Z\left[\mathbb{E}_{\varepsilon \mid Z}[A^\top B]\right] = \mathbb{E}_Z\left[A^\top \mathbb{E}_{\varepsilon \mid Z}[B]\right] = 0.
$$

Hence

$$
\mathbb{E}_{Z,\varepsilon}\|a(Z) - \varepsilon\|_2^2 = \mathbb{E}_Z\|a(Z) - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon]\|_2^2 + \mathbb{E}_{Z,\varepsilon}\|\varepsilon - \mathbb{E}_{\varepsilon \mid Z}[\varepsilon]\|_2^2. \qquad \square
$$

64

<!-- page: 65 -->

## References

[1] Brian D. O. Anderson. Reverse-time diffusion equation models. *Stochastic Processes and their Applications*, 12(3):313â€“326, 1982.

[2] Jacob Austin, Daniel D. Johnson, Jonathan Ho, Daniel Tarlow, and Rianne van den Berg. Structured denoising diffusion models in discrete state-spaces. In *Advances in Neural Information Processing Systems*, 2021.

[3] Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, and David Duvenaud. Neural ordinary differential equations. In *Advances in Neural Information Processing Systems*, 2018.

[4] Prafulla Dhariwal and Alexander Nichol. Diffusion models beat GANs on image synthesis. In *Advances in Neural Information Processing Systems*, 2021.

[5] Shansan Gong, Mukai Li, Jiangtao Feng, Zhiyong Wu, and Lingpeng Kong. DiffuSeq: Sequence to sequence text generation with diffusion models. In *International Conference on Learning Representations*, 2023.

[6] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In *Advances in Neural Information Processing Systems*, 2020.

[7] Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance. *arXiv preprint arXiv:2207.12598*, 2022.

[8] Peter Holderrieth and Ezra Erives. An introduction to flow matching and diffusion models. arXiv preprint arXiv:2506.02070, 2025.

[9] Aapo HyvĂ¤rinen. Estimation of non-normalized statistical models by score matching. *Journal of Machine Learning Research*, 6:695â€“709, 2005.

[10] Tero Karras, Miika Aittala, Timo Aila, and Samuli Laine. Elucidating the design space of diffusion-based generative models. In *Advances in Neural Information Processing Systems*, 2022.

[11] Diederik P. Kingma, Tim Salimans, Ben Poole, and Jonathan Ho. Variational diffusion models. In *Advances in Neural Information Processing Systems*, 2021.

[12] Xiang Lisa Li, John Thickstun, Ishaan Gulrajani, Percy Liang, and Tatsunori B. Hashimoto. Diffusion-LM improves controllable text generation. In *Advances in Neural Information Processing Systems*, 2022.

[13] Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. In *International Conference on Learning Representations*, 2023.

[14] Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, and Jun Zhu. DPM-Solver: A fast ODE solver for diffusion probabilistic model sampling in around 10 steps. In *Advances in Neural Information Processing Systems*, 2022.

[15] Cheng Lu, Yuhao Zhou, Fan Bao, Jianfei Chen, Chongxuan Li, and Jun Zhu. DPM-Solver++: Fast solver for guided sampling of diffusion probabilistic models. *arXiv preprint arXiv:2211.01095*, 2022.

65

<!-- page: 66 -->

[16] Chenlin Meng, Yutong He, Yang Song, Jiaming Song, Jiajun Wu, Jun-Yan Zhu, and Stefano Ermon. SDEdit: Guided image synthesis and editing with stochastic differential equations. *arXiv preprint arXiv:2108.01073*, 2021.

[17] Alex Nichol, Prafulla Dhariwal, Aditya Ramesh, Pranav Shyam, Pamela Mishkin, Bob McGrew, Ilya Sutskever, and Mark Chen. GLIDE: Towards photorealistic image generation and editing with text-guided diffusion models. *arXiv preprint arXiv:2112.10741*, 2021.

[18] Alexander Quinn Nichol and Prafulla Dhariwal. Improved denoising diffusion probabilistic models. In *International Conference on Machine Learning*, 2021.

[19] Bernt Ă˜ksendal. *Stochastic Differential Equations: An Introduction with Applications*. Springer, 6th edition, 2003.

[20] Hannes Risken. *The Fokkerâ€“Planck Equation: Methods of Solution and Applications*. Springer, 2nd edition, 1996.

[21] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and BjĂ¶rn Ommer. High-resolution image synthesis with latent diffusion models. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 2022.

[22] Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho, David J Fleet, and Mohammad Norouzi. Photorealistic text-to-image diffusion models with deep language understanding. In *Advances in Neural Information Processing Systems*, 2022.

[23] Tim Salimans and Jonathan Ho. Progressive distillation for fast sampling of diffusion models. In *International Conference on Learning Representations*, 2022.

[24] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsupervised learning using nonequilibrium thermodynamics. In *Proceedings of the 32nd International Conference on Machine Learning*, 2015.

[25] Jiaming Song, Chenlin Meng, and Stefano Ermon. Denoising diffusion implicit models. In *International Conference on Learning Representations*, 2021.

[26] Yang Song and Stefano Ermon. Generative modeling by estimating gradients of the data distribution. In *Advances in Neural Information Processing Systems*, 2019.

[27] Yang Song and Stefano Ermon. Improved techniques for training score-based generative models. In *Advances in Neural Information Processing Systems*, 2020.

[28] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. In *International Conference on Learning Representations*, 2021.

[29] Robin Strudel, Corentin Tallec, Florent AltchĂ©, Yilun Du, Yaroslav Ganin, Arthur Mensch, Will Grathwohl, Nikolay Savinov, Sander Dieleman, Laurent Sifre, and RĂ©mi Leblond. Self-conditioned embedding diffusion for text generation. *arXiv preprint arXiv:2211.04236*, 2022.

[30] Pascal Vincent. A connection between score matching and denoising autoencoders. *Neural Computation*, 23(7):1661â€“1674, 2011.

66
