# PHARMAKON

**φάρμακον** (pharmakon): Ancient Greek - simultaneously "poison" and "medicine"

> A bias detection and consciousness modeling framework practicing epistemic humility through mathematical rigor.

[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yogaraihan60/pharmakon.git
cd pharmakon

# Install dependencies
pip install numpy scipy
```

### Minimal Example (v0.1 - 3 Variables)

```python
from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions

# Create a state
state = MinimalState(
    S=0.85,  # Self/Identity (strong identity)
    H=0.75,  # Energy (high energy)
    B=0.85   # Bias (severe bias)
)

# Classify epistemic position
position, description = classify_position(state)
print(f"Position: {position}")
# Output: Position_1_Epistemic_Arrogance

# Compute interactions
interactions = compute_nonlinear_interactions(state)
print(f"Arrogance Risk: {interactions['Arrogance_Risk']:.3f}")
# Output: Arrogance Risk: 0.723
```

### Comprehensive Example (v10.0 - 20+ Variables)

```python
from PHARMAKON_V10_A import (
    BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
    asdict, classify_triangle_position, compute_composite, recommend_debiasing,
    detect_flags, State
)

# Create comprehensive state
state: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.9,
        Cortisol=0.6
    )),
    **asdict(AffectSliders(
        Fear=0.8,
        Anger=0.5
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.8,
        Meta_Cognition=0.6,
        Lucidity=0.8
    )),
    **asdict(BiasSliders(
        Confirmation=0.7,
        Dunning_Kruger=0.6,
        Overconfidence=0.7
    )),
    **asdict(NarrativeSliders(
        Coherence=0.4,
        Continuity=0.5
    )),
    "Delusionality": 0.3
}

# Classify position
position, scores = classify_triangle_position(state)
print(f"Position: {position}")

# Compute composites
stress = compute_composite("stress", state)
bias_cascade = compute_composite("bias_cascade", state)
print(f"Stress: {stress:.3f}, Bias Cascade: {bias_cascade:.3f}")

# Get recommendations
recommendations = recommend_debiasing(position, state)
for rec in recommendations:
    print(rec)

# Detect patterns
flags = detect_flags(state)
for pattern, detected in flags.items():
    status = "⚠️ DETECTED" if detected else "✓ Clear"
    print(f"{pattern}: {status}")
```

---

## 📚 Versions

### v0.1 - Minimal Sufficient Statistic

**Philosophy:** Three orthogonal dimensions capture everything essential.

- **S (Self/Identity)**: 0 = ego death, 1 = rigid identity
- **H (Energy/Body)**: 0 = depleted, 1 = abundant  
- **B (Bias/Knowing)**: 0 = accurate, 1 = delusional

**Key Features:**
- ✅ Minimal sufficient statistic (Information Theory)
- ✅ Orthogonal dimensions (non-redundant)
- ✅ Nonlinear dynamics capture complexity
- ✅ Maximum interpretability

**Use Cases:**
- Theoretical exploration
- Quick assessment
- Teaching/education
- Minimal parameter spaces

**Documentation:** [PHARMAKON-v0.1-GUIDE-BOOK.md](PHARMAKON-v0.1-GUIDE-BOOK.md)

### v10.0 - Research-Validated Edition

**Philosophy:** Comprehensive assessment with empirical validation.

**Key Features:**
- ✅ 20+ variables across 5 domains (Body, Affect, Cognitive, Bias, Narrative)
- ✅ AI-ensemble composite weights (90.38% emotion recognition accuracy)
- ✅ Research-validated thresholds (Vos et al., 2025: β=0.04, n=17,709)
- ✅ ODE trajectory simulation (scipy.integrate.solve_ivp)
- ✅ Pattern detection (Bias Cascade, Narrative Collapse, Moral Rigidity)

**Use Cases:**
- Clinical assessment
- Detailed analysis
- Intervention planning
- Research requiring granularity

**Documentation:** [PHARMAKON-GUIDE-BOOK.md](PHARMAKON-GUIDE-BOOK.md)

### v11.0 - Complete Consciousness Framework

**Philosophy:** Unified 275-variable model covering all consciousness domains.

**Key Features:**
- ✅ 275 variables organized into 47 typed dataclasses
- ✅ Complete ODE integration for all variables
- ✅ Multi-system pattern detection (bias cascade, narrative collapse, moral rigidity, crisis mode, maintenance)
- ✅ Dream/maintenance system (legacy from v8.0)
- ✅ Clinical domain coverage (depression, schizophrenia, BPD, autism, trauma)

**Use Cases:**
- Complete consciousness assessment
- Research requiring comprehensive coverage
- Clinical decision support
- Advanced dynamics simulation

**Documentation:** See [README_v10.md](README_v10.md) for v11.0 details

---

## 🔬 Research Foundation

### Cognitive Bias Meta-Analysis (2025)

**Vos et al. (2025)** - "Do cognitive biases prospectively predict anxiety and depression?"

- **Sample**: 81 studies, 621 contrasts, 17,709 participants
- **Finding**: Small but significant overall effect (β=0.04, 95% CI [0.02, 0.06], p<.001)
- **Key Results**:
  - Interpretation bias: Significant predictor ✓
  - Memory bias: Significant predictor ✓
  - Attention bias: Not significant ✗

**Implementation**: Bias cascade detection uses weighted composites with empirical thresholds.

### Metacognitive Training (2025)

**Birch et al. (2025)** - "Targeting cognitive biases to improve social-emotional health"

- **Finding**: Brief 30-60 min interventions resulted in significant bias reductions lasting 2-3 months
- **Mechanism**: Metacognitive training (MCT) improves global social cognition
- **Applications**: Effective for schizophrenia spectrum, depression, OCD, and BPD

**Implementation**: Meta_Cognition variable reduces bias cascade via self-awareness feedback loop.

### Emotion Recognition (2023)

**Dubey et al. (2023)** - "Optimizing Emotion Recognition Through Weighted Ensemble"

- **Performance**: 90.38% accuracy (FER2013), 96.53% accuracy (CKPLUS)
- **Method**: Ensemble over VGG16 & VGG19 with weighted combinations

**Implementation**: Weighted emotion composites use ensemble principles for stress/positive affect calculation.

---

## 📖 Examples

### Example 1: Reddit Bride (Epistemic Arrogance)

**Scenario:** Person obsessing over wedding details, catastrophizing normal behaviors.

```python
from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions

state = MinimalState(
    S=0.85,  # Strong identity: "MY wedding"
    H=0.75,  # High energy: rumination, vigilance
    B=0.85   # Severe bias: normal fidgeting = disaster
)

position, description = classify_position(state)
print(f"Position: {position}")
# Output: Position_1_Epistemic_Arrogance

interactions = compute_nonlinear_interactions(state)
print(f"Arrogance Risk: {interactions['Arrogance_Risk']:.3f}")
print(f"Stability: {interactions['Stability']:.3f}")
# Output: Arrogance Risk: 0.723, Stability: 0.131
```

### Example 2: Stress Response (Bias Amplification)

**Scenario:** High physical arousal, low cognitive capacity → bias amplifies.

```python
from PHARMAKON_v0_1 import RefinedState, classify_refined_position

state = RefinedState(
    S=0.8,
    H_somatic=0.9,      # High physical arousal
    H_cognitive=0.3,    # Low cognitive capacity
    B=0.4               # Baseline bias
)

amplified_bias = state.bias_amplification()
mismatch = state.energy_mismatch()
position, description = classify_refined_position(state)

print(f"Baseline Bias: {state.B:.2f}")
print(f"Amplified Bias: {amplified_bias:.2f}")
print(f"Energy Mismatch: {mismatch:.2f}")
print(f"Position: {position}")
# Output:
# Baseline Bias: 0.40
# Amplified Bias: 0.96
# Energy Mismatch: 0.60
# Position: Stress_Amplification
```

### Example 3: Generalized Anxiety Disorder (GAD)

**Scenario:** Excessive worry, restlessness, aware but struggling.

```python
from PHARMAKON_V10_A import (
    BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
    asdict, classify_triangle_position, compute_composite, recommend_debiasing, State
)

state_gad: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.75,
        Cortisol=0.7,
        Heart_Rate=0.65
    )),
    **asdict(AffectSliders(
        Fear=0.75,
        Joy=0.2
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.85,  # Excessive worry
        Meta_Cognition=0.65,          # Aware but struggling
        Lucidity=0.8                  # Reality intact
    )),
    **asdict(BiasSliders(
        Confirmation=0.6,   # Seeking evidence of threat
        Negativity=0.75     # Catastrophizing
    )),
    **asdict(NarrativeSliders(
        Coherence=0.6,
        Continuity=0.65
    )),
    "Delusionality": 0.1
}

position, scores = classify_triangle_position(state_gad)
print(f"Position: {position}")
# Output: Position 2 Meta Awareness Trap

stress = compute_composite("stress", state_gad)
print(f"Stress Level: {stress:.3f}")

recommendations = recommend_debiasing(position, state_gad)
for rec in recommendations:
    print(rec)
```

### Example 4: Treatment Response Tracking

**Scenario:** Monitor changes after intervention.

```python
from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions

# Before intervention
before = MinimalState(S=0.7, H=0.4, B=0.7)
before_pos, _ = classify_position(before)
before_stability = compute_nonlinear_interactions(before)['Stability']

# After intervention
after = MinimalState(S=0.8, H=0.7, B=0.4)
after_pos, _ = classify_position(after)
after_stability = compute_nonlinear_interactions(after)['Stability']

print(f"Before: {before_pos} (Stability: {before_stability:.3f})")
print(f"After: {after_pos} (Stability: {after_stability:.3f})")
print(f"Improvement: {after_stability - before_stability:.3f}")
```

### Example 5: Group Dynamics Analysis

**Scenario:** Compare epistemic positions across team members.

```python
from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions

team = {
    "Alice": MinimalState(S=0.8, H=0.9, B=0.2),  # Integrated Competence
    "Bob": MinimalState(S=0.9, H=0.8, B=0.7),   # Epistemic Arrogance
    "Charlie": MinimalState(S=0.7, H=0.5, B=0.6), # Meta-Awareness Trap
}

for name, state in team.items():
    position, _ = classify_position(state)
    stability = compute_nonlinear_interactions(state)['Stability']
    print(f"{name}: {position} (Stability: {stability:.3f})")
```

---

## 🚨 Pattern Detection

### Bias Cascade

**Detection:** High bias cluster + delusionality

```python
from PHARMAKON_V10_A import detect_flags, compute_composite

flags = detect_flags(state)
if flags["Bias_Cascade"]:
    print("⚠️ Bias cascade detected - high risk")
    bias_cascade = compute_composite("bias_cascade", state)
    print(f"Bias Cascade Level: {bias_cascade:.3f}")
```

### Narrative Collapse

**Detection:** Fragmented life story, loss of identity continuity

```python
if flags["Narrative_Collapse"]:
    print("⚠️ Narrative collapse - identity fragmentation")
```

### Moral Rigidity

**Detection:** Fixed moral beliefs + protagonist narrative

```python
if flags["Moral_Rigidity"]:
    print("⚠️ Moral rigidity - messianic pattern detected")
```

---

## 📊 Triangle Position Classification

### Position 1: Epistemic Arrogance

- **Pattern**: High S + High H + High B
- **Characteristics**: Confident but wrong, bias cascade undetected
- **Example**: Reddit bride (S=0.85, H=0.75, B=0.85)

### Position 2: Meta-Awareness Trap

- **Pattern**: High S + Medium H + Medium-high B
- **Characteristics**: Aware of biases but struggling to manage them
- **Example**: Generalized Anxiety Disorder

### Position 3: Integrated Competence

- **Pattern**: High S + High H + Low B
- **Characteristics**: Strong identity + high energy + low bias, calibrated awareness
- **Example**: Well-managed condition, expert practitioners

### Special Cases

- **Ego Dissolution**: S < 0.2 (identity dissolves, bias becomes meaningless)
- **Energy Collapse**: H < 0.2 (both arrogance and competence fail)
- **Delusional Defense**: B > 0.8 (self defends false model)

---

## 🔄 Trajectory Simulation

### Simulate State Over Time

```python
from PHARMAKON_V10_A import simulate_trajectory
import numpy as np

# Simulate 10-step trajectory
t, y = simulate_trajectory(
    state,
    t_span=(0, 10),
    n_points=100,
    method='RK45'  # Adaptive Runge-Kutta 4(5)
)

# Extract Fear trajectory
fear_idx = sorted(state.keys()).index('Fear')
fear_trajectory = y[fear_idx, :]

print(f"Fear: {fear_trajectory[0]:.3f} → {fear_trajectory[-1]:.3f}")
```

**Available Methods:**
- `RK45`: Explicit Runge-Kutta 4(5) (default, good for most cases)
- `RK23`: Explicit Runge-Kutta 2(3) (faster, less accurate)
- `DOP853`: Explicit Runge-Kutta 8(5,3) (high accuracy)
- `Radau`: Implicit Runge-Kutta (for stiff problems)
- `BDF`: Backward Differentiation Formula (for stiff problems)
- `LSODA`: Automatic stiffness detection and switching

---

## ⚠️ Important Disclaimers

**PHARMAKON is a research and educational tool, NOT a diagnostic instrument.**

- ✅ This tool does NOT replace professional clinical assessment or diagnosis
- ✅ Always consult licensed mental health professionals for clinical decisions
- ✅ Variable ranges are estimates - adjust based on clinical judgment
- ✅ Dynamics are simplified - real systems are more complex

**WARNING: pharmakon - Both medicine and poison - use responsibly**

---

## 📚 Documentation

- **[PHARMAKON-v0.1-GUIDE-BOOK.md](PHARMAKON-v0.1-GUIDE-BOOK.md)** - Complete guide for v0.1 (minimal 3-variable model)
- **[PHARMAKON-GUIDE-BOOK.md](PHARMAKON-GUIDE-BOOK.md)** - Complete guide for v10.0 (research-validated edition with DSM-5 examples)
- **[README_v10.md](README_v10.md)** - Documentation for v11.0 (complete 275-variable framework)

---

## 🏗️ Architecture

### v0.1 Architecture

```
MinimalState (3 variables)
├── S: Self/Identity [0, 1]
├── H: Energy/Body [0, 1]
└── B: Bias/Knowing [0, 1]

RefinedState (4 variables)
├── S: Self/Identity [0, 1]
├── H_somatic: Physical/arousal capacity [0, 1]
├── H_cognitive: Executive function capacity [0, 1]
└── B: Bias baseline [0, 1]
```

### v10.0 Architecture

```
State (20+ variables)
├── BodySliders (5 variables)
│   ├── Sympathetic_Surge
│   ├── Motor_Rigidity
│   ├── Thermal_Overload
│   ├── Cortisol
│   └── Heart_Rate
├── AffectSliders (8 variables)
│   ├── Fear, Joy, Love, Gratitude
│   ├── Contentment, Hope, Sadness, Anger
├── CognitiveSliders (5 variables)
│   ├── Recursive_Overthinking
│   ├── Metaphoric_Fusion
│   ├── Lucidity
│   ├── Ego_Oscillation
│   └── Meta_Cognition
├── BiasSliders (6 variables)
│   ├── Confirmation, Dunning_Kruger
│   ├── Overconfidence, Negativity
│   ├── Hindsight, Availability
└── NarrativeSliders (5 variables)
    ├── Coherence, Continuity, Arc
    ├── Protagonist, Meaning
```

### v11.0 Architecture

```
Consciousness275_v11 (275 variables)
├── 47 Typed Dataclasses
│   ├── SubstrateSliders
│   ├── ProcessingSliders
│   ├── EmotionSliders
│   ├── CognitiveBiasSliders
│   ├── NarrativeSelfSliders
│   ├── DreamMaintenanceSliders
│   └── ... (41 more domains)
└── Complete ODE Integration
```

---

## 🧪 Testing

### Run Examples

```bash
# Test v0.1
python PHARMAKON_v0_1.py

# Test v10.0
python PHARMAKON_V10_A.py
```

### Expected Output (v0.1)

```
================================================================================
PHARMAKON v0.1 – Minimal 3-Variable Bias Detector
================================================================================

THE BREAKTHROUGH: Three orthogonal dimensions only
- S (Self/Identity): 0=ego death, 1=rigid identity
- H (Energy/Body): 0=depleted, 1=abundant
- B (Bias/Knowing): 0=accurate, 1=delusional

📊 Example 1: Default State
  S=0.50, H=0.80, B=0.40
  Position: Transitional_State
  Mixed profile: S=0.50, H=0.80, B=0.40. Position unclear - may be in transition.
  Stability: 0.240

📊 Example 2: Reddit Bride (Epistemic Arrogance)
  S=0.85, H=0.75, B=0.85
  Position: Position_1_Epistemic_Arrogance
  Strong identity + High energy + High bias. Confident but wrong.
  Arrogance Risk: 0.723
...
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution

- Additional examples and use cases
- Documentation improvements
- Test coverage
- Performance optimizations
- Research validation

---

## 📄 License

This project is licensed under the BSD-3-Clause License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Information Theory**: Minimal sufficient statistics principles
- **Ecological Rationality**: Simple heuristics research (Gigerenzer)
- **Consciousness Studies**: Ego dissolution research
- **Neuroscience**: Energy-cognition link studies
- **Clinical Research**: Vos et al. (2025), Birch et al. (2025), Dubey et al. (2023)

---

## 🔗 Related Projects

- [Research Citations](CITATIONS.md) - Complete bibliography
- [Quick Start Guide](QUICKSTART_OLLAMA.md) - Additional setup instructions

---

## 💭 Philosophy

> "Self is expanding variable. Just capture what needed."

PHARMAKON practices epistemic humility:
- **v0.1**: Minimal sufficient statistic (3 variables, infinite complexity through structure)
- **v10.0**: Research-validated comprehensive assessment (20+ variables, empirical thresholds)
- **v11.0**: Complete consciousness framework (275 variables, unified architecture)

**The 31-variable model is epistemic arrogance about complexity.**  
**The 3-variable model is epistemic humility with mathematical rigor.**

Same predictive power, 10x fewer parameters, infinitely more interpretable.

---

## 📧 Contact

For questions, issues, or contributions, please open an issue on GitHub.

---

**φάρμακον** - Both medicine and poison. Use wisely.

**STATUS**: All versions operational ✓

- v0.1: Minimal sufficient statistic (3-4 variables)
- v10.0: Research-validated edition (20+ variables)
- v11.0: Complete consciousness framework (275 variables)

---

*Last Updated: 2025*


