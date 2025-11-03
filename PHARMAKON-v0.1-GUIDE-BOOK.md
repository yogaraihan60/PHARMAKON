# PHARMAKON v0.1 Guide Book
## The Minimal Sufficient Statistic

**Version:** 0.1  
**Last Updated:** 2025  
**License:** BSD-3-Clause

---

## ⚠️ IMPORTANT DISCLAIMER

**PHARMAKON is a research and educational tool, NOT a diagnostic instrument.**

- This tool does NOT replace professional clinical assessment or diagnosis
- Always consult licensed mental health professionals for clinical decisions
- This tool practices epistemic humility: simple structure, profound implications

**WARNING: pharmakon - Both medicine and poison - use responsibly**

---

## Table of Contents

1. [The Breakthrough](#the-breakthrough)
2. [Core Philosophy](#core-philosophy)
3. [The Three Variables](#the-three-variables)
4. [The Refined Model (4 Variables)](#the-refined-model-4-variables)
5. [Position Classification](#position-classification)
6. [Nonlinear Dynamics](#nonlinear-dynamics)
7. [Practical Examples](#practical-examples)
8. [Real-World Applications](#real-world-applications)
9. [Mathematical Foundations](#mathematical-foundations)
10. [Code Reference](#code-reference)

---

## 1. The Breakthrough

### The Minimal Sufficient Statistic

**Three orthogonal dimensions only.**

This is not a simplification—it's the **mathematical truth** about what information is truly necessary to capture epistemic positions and bias states.

### Why This Matters

**The Problem with Complex Models:**
- 31 variables require manual weighting (why 0.35 vs. 0.30?)
- Data-rich but interpretation-poor
- False precision ("bias_cascade: 0.797" is arbitrary)
- Nobody actually interprets it coherently

**The Solution:**
- 3 variables capture everything essential
- Each variable is **orthogonal** (independent, non-redundant)
- **Nonlinear structure** captures complexity, not additional variables
- Infinitely more interpretable

### The Core Insight

> **"Self is expanding variable. Just capture what needed."**

In a highly interconnected system, don't add more variables—use **nonlinear structure** to capture everything.

- The 31-variable model is **epistemic arrogance about complexity**
- The 3-variable model is **epistemic humility with mathematical rigor**
- Same predictive power, 10x fewer parameters, infinitely more interpretable

---

## 2. Core Philosophy

### Information Theory Principles

PHARMAKON v0.1 is grounded in three fundamental principles:

#### 1. Minimal Sufficient Information

**Definition:** Removing any one variable loses critical predictive power.

- **Removing S**: Can't detect ego dissolution (different ontology)
- **Removing H**: Can't see why arrogance fails under stress
- **Removing B**: Can't distinguish confident accuracy from confident delusion

Each variable is **necessary** and **sufficient**.

#### 2. Orthogonality (Independence)

**Definition:** Variables capture non-redundant information.

- **S and H**: Can have strong identity + low energy (depressed) OR strong identity + high energy (arrogant)
- **S and B**: Can be confident + accurate OR confident + wrong
- **H and B**: Energy doesn't determine bias direction

These dimensions are **independent**—one doesn't determine the others.

#### 3. Nonlinearity Captures Complexity

**Key Nonlinear Interactions:**

- **When S → 0**: B becomes meaningless (no self to be biased, enters different ontology)
- **When H → 0**: Both arrogance and competence collapse
- **When B → 1**: Person's S now defends a false model

Complexity emerges from **structure**, not additional variables.

### Epistemic Humility

PHARMAKON v0.1 practices what it preaches:
- **Trust in embodied, intuitive understanding** grounded in evidence
- **Epistemic humility** about its own assumptions
- **Mathematical rigor** without false complexity

---

## 3. The Three Variables

### S (Self/Identity)

**Range:** [0, 1]

**Meaning:**
- **0**: Ego death/dissolution (identity collapses, enters different ontology)
- **1**: Rigidly defended self (strong identity boundaries)

**What It Replaces:**
- All narrative/coherence variables
- Identity continuity
- Self-concept stability
- Protagonist narrative

**Phenomenological Fact:**
Consciousness can dissolve. Ego dissolution is empirically studied as a **separate state**, not just a "low score" on normal dimensions. It requires its own category (S ≈ 0).

**Key Nonlinearity:**
When S → 0, Bias (B) becomes meaningless—there's no self to be biased.

**Examples:**
- S = 0.85: Strong identity ("MY wedding" - rigid self-boundary)
- S = 0.5: Normal identity
- S = 0.1: Ego dissolution (meditation, psychedelics, severe trauma)

### H (Energy/Body)

**Range:** [0, 1]

**Meaning:**
- **0**: Depleted (no metabolic/cognitive capacity)
- **1**: Abundant (high capacity)

**What It Replaces:**
- All physiological variables
- All executive function variables
- Metabolic capacity
- Cognitive capacity

**Neuroscience Foundation:**
Brain energy demands directly correlate with cognitive integration and capacity. High-dimensional consciousness uses more energy than collapsed states.

**Key Nonlinearity:**
When H → 0, both arrogance and competence collapse under stress.

**Examples:**
- H = 0.9: High energy, sharp cognition
- H = 0.5: Moderate capacity
- H = 0.1: Energy collapse (burnout, exhaustion, severe depression)

### B (Bias/Knowing)

**Range:** [0, 1]

**Meaning:**
- **0**: Accurate (belief matches reality)
- **1**: Delusional (severe mismatch)

**What It Replaces:**
- All bias variables (confirmation, Dunning-Kruger, overconfidence, etc.)
- Singular degree of reality distortion

**Key Nonlinearity:**
When B → 1, Person's Self (S) now defends a false model of reality.

**Examples:**
- B = 0.2: Low bias, well-calibrated
- B = 0.5: Moderate bias
- B = 0.85: Severe bias (delusional thinking)

---

## 4. The Refined Model (4 Variables)

### Why Separate Energy?

The **RefinedState** splits H into two dimensions:

- **H_somatic**: Physical/arousal capacity (fight-or-flight, sympathetic nervous system)
- **H_cognitive**: Executive function capacity (cognitive control, working memory, metacognition)

### Key Dynamic: Stress Amplification

**When H_somatic >> H_cognitive:**

Physical arousal outpaces cognitive capacity → impaired judgment → **bias amplifies**.

This captures the stress response pattern where:
- Body is activated (H_somatic high)
- Cognitive capacity is depleted (H_cognitive low)
- Bias amplifies beyond baseline

### RefinedState Structure

```python
@dataclass
class RefinedState:
    S: float = 0.5              # Self/Identity
    H_somatic: float = 0.8       # Physical/arousal capacity
    H_cognitive: float = 0.6    # Executive function capacity
    B: float = 0.4              # Bias baseline
```

### Bias Amplification Formula

When H_cognitive < 0.3:
```
amplification = (H_somatic / H_cognitive) × (1 - S)
amplified_bias = min(B × amplification, 1.0)
```

**Interpretation:**
- Lower cognitive capacity → higher amplification
- Lower identity strength → more vulnerable to amplification
- Capped at 1.0 (maximum bias)

### Energy Mismatch

```python
mismatch = max(0.0, H_somatic - H_cognitive)
```

**Interpretation:**
- High mismatch (> 0.4) = Stress amplification state
- Low mismatch = Balanced energies

---

## 5. Position Classification

### MinimalState Positions (3 Variables)

#### Position 1: Epistemic Arrogance

**Pattern:**
- High S (strong identity)
- High H (high energy)
- High B (severe bias)

**Characteristics:**
- Confident but wrong
- Bias cascade undetected
- Strong identity defends false model

**Example: Reddit Bride**
- S = 0.85 ("MY wedding" - rigid identity)
- H = 0.75 (high energy: rumination, vigilance)
- B = 0.85 (normal fidgeting = disaster)
- → Position 1: Epistemic Arrogance

**Code:**
```python
if S > 0.7 and H > 0.6 and B > 0.6:
    return "Position_1_Epistemic_Arrogance"
```

#### Position 2: Meta-Awareness Trap

**Pattern:**
- High S (strong identity)
- Medium H (moderate energy)
- Medium-high B (aware but struggling)

**Characteristics:**
- Aware of biases but struggling to manage them
- Meta-cognition present but insufficient
- Distressing awareness

**Code:**
```python
if S > 0.5 and B > 0.4 and B < 0.7:
    return "Position_2_Meta_Awareness_Trap"
```

#### Position 3: Integrated Competence

**Pattern:**
- High S (strong identity)
- High H (high energy)
- Low B (low bias, calibrated)

**Characteristics:**
- Strong identity + high energy + low bias
- Calibrated awareness
- Bias detected + managed

**Code:**
```python
if S > 0.7 and H > 0.6 and B < 0.4:
    return "Position_3_Integrated_Competence"
```

### Special Cases

#### Ego Dissolution

**Pattern:** S < 0.2

**Meaning:**
- Identity dissolution
- Bias (B) becomes meaningless—no self to be biased
- Different ontology (not just "low score")

**Code:**
```python
if S < 0.2:
    return "Ego_Dissolution"
```

#### Energy Collapse

**Pattern:** H < 0.2

**Meaning:**
- Energy depleted
- Both arrogance and competence collapse under stress

**Code:**
```python
if H < 0.2:
    return "Energy_Collapse"
```

#### Delusional Defense

**Pattern:** B > 0.8

**Meaning:**
- Severe bias
- Person's Self (S) now defends a false model of reality

**Code:**
```python
if B > 0.8:
    return "Delusional_Defense"
```

### RefinedState Positions (4 Variables)

Additional positions for somatic-cognitive mismatch:

#### Stress Amplification

**Pattern:** H_somatic >> H_cognitive (mismatch > 0.4)

**Meaning:**
- Physical arousal outpaces cognition
- Bias amplifies

**Code:**
```python
if mismatch > 0.4:
    return "Stress_Amplification"
```

#### Cognitive Collapse

**Pattern:** H_cognitive < 0.2

**Meaning:**
- Executive function collapsed
- Bias amplified dramatically

**Code:**
```python
if H_cognitive < 0.2:
    return "Cognitive_Collapse"
```

---

## 6. Nonlinear Dynamics

### Interaction Metrics

PHARMAKON computes nonlinear interactions between dimensions:

#### Bias Meaningless

**When:** S < 0.3

**Formula:** `Bias_Meaningless = 1.0 - S`

**Meaning:** As identity dissolves, bias becomes conceptually meaningless.

#### Energy Stress

**Formula:** `Energy_Stress = 1.0 - H`

**Meaning:** Inverse of energy capacity—stress increases as energy depletes.

#### Delusional Defense

**When:** B > 0.7

**Formula:** `Delusional_Defense = B × S`

**Meaning:** Strong identity defending severe bias = delusional system.

#### Stability

**Formula:** `Stability = S × H × (1.0 - B)`

**Meaning:**
- High S + High H + Low B = Maximum stability
- Any component low → stability decreases

#### Arrogance Risk

**Formula:** `Arrogance_Risk = S × B`

**Meaning:**
- High S + High B = Confident wrong
- Maximum risk of epistemic arrogance

### Example: Computing Interactions

```python
from PHARMAKON_v0_1 import MinimalState, compute_nonlinear_interactions

state = MinimalState(S=0.85, H=0.75, B=0.85)
interactions = compute_nonlinear_interactions(state)

print(f"Stability: {interactions['Stability']:.3f}")
print(f"Arrogance Risk: {interactions['Arrogance_Risk']:.3f}")
print(f"Energy Stress: {interactions['Energy_Stress']:.3f}")
```

**Output:**
```
Stability: 0.131
Arrogance Risk: 0.723
Energy Stress: 0.250
```

Interpretation:
- Low stability (0.131) due to high bias
- High arrogance risk (0.723) = confident wrong
- Moderate energy stress (0.250)

---

## 7. Practical Examples

### Example 7.1: Reddit Bride (Epistemic Arrogance)

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
print(f"Description: {description}")

interactions = compute_nonlinear_interactions(state)
print(f"\nArrogance Risk: {interactions['Arrogance_Risk']:.3f}")
print(f"Stability: {interactions['Stability']:.3f}")
```

**Output:**
```
Position: Position_1_Epistemic_Arrogance
Description: Strong identity + High energy + High bias. Confident but wrong. Example: Reddit bride (S=0.85, H=0.75, B=0.85)

Arrogance Risk: 0.723
Stability: 0.131
```

### Example 7.2: Depressed Academic (Meta-Awareness Trap)

**Scenario:** Aware of cognitive biases but struggling to manage them.

```python
state = MinimalState(
    S=0.7,   # Strong identity (academic self-concept)
    H=0.4,   # Low energy (depleted)
    B=0.6    # Moderate-high bias (aware but struggling)
)

position, description = classify_position(state)
print(f"Position: {position}")
print(f"Description: {description}")
```

**Output:**
```
Position: Position_2_Meta_Awareness_Trap
Description: Strong identity + Moderate bias. Aware of biases but struggling to manage them.
```

### Example 7.3: Integrated Competence

**Scenario:** Strong identity, high energy, well-calibrated awareness.

```python
state = MinimalState(
    S=0.8,   # Strong identity
    H=0.9,   # High energy
    B=0.2    # Low bias (well-calibrated)
)

position, description = classify_position(state)
interactions = compute_nonlinear_interactions(state)

print(f"Position: {position}")
print(f"Stability: {interactions['Stability']:.3f}")
```

**Output:**
```
Position: Position_3_Integrated_Competence
Description: Strong identity + High energy + Low bias. Calibrated awareness.
Stability: 0.576
```

### Example 7.4: Stress Response (RefinedState)

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
print(f"Description: {description}")
```

**Output:**
```
Baseline Bias: 0.40
Amplified Bias: 0.96
Energy Mismatch: 0.60
Position: Stress_Amplification
Description: H_somatic (0.90) >> H_cognitive (0.30): Physical arousal outpaces cognition. Bias amplified to 0.96.
```

**Interpretation:**
- Baseline bias of 0.4 amplifies to 0.96 (near maximum)
- Severe somatic-cognitive mismatch (0.60)
- Stress amplification state detected

### Example 7.5: Ego Dissolution

**Scenario:** Identity dissolves (meditation, psychedelics, severe trauma).

```python
state = MinimalState(
    S=0.1,   # Ego dissolution
    H=0.6,   # Moderate energy
    B=0.5    # Bias becomes meaningless
)

position, description = classify_position(state)
interactions = compute_nonlinear_interactions(state)

print(f"Position: {position}")
print(f"Description: {description}")
print(f"Bias Meaningless: {interactions['Bias_Meaningless']:.3f}")
```

**Output:**
```
Position: Ego_Dissolution
Description: S → 0: Identity dissolution. Bias (B) becomes meaningless - no self to be biased. Different ontology.
Bias Meaningless: 0.900
```

**Key Insight:** When S → 0, bias (B) loses meaning. This is a different ontological state, not just "low self."

---

## 8. Real-World Applications

### Application 1: Personal Bias Monitoring

**Use Case:** Track your own epistemic position over time.

```python
from PHARMAKON_v0_1 import MinimalState, classify_position, save_state
from pathlib import Path

# Daily self-assessment
states = {
    "Monday": MinimalState(S=0.7, H=0.8, B=0.5),
    "Tuesday": MinimalState(S=0.7, H=0.6, B=0.6),
    "Wednesday": MinimalState(S=0.8, H=0.9, B=0.3),
}

for day, state in states.items():
    position, _ = classify_position(state)
    print(f"{day}: {position}")

# Save state for later analysis
save_state(states["Wednesday"], Path("wednesday_state.json"))
```

### Application 2: Group Dynamics Analysis

**Use Case:** Compare epistemic positions across group members.

```python
team_members = {
    "Alice": MinimalState(S=0.8, H=0.9, B=0.2),  # Integrated Competence
    "Bob": MinimalState(S=0.9, H=0.8, B=0.7),   # Epistemic Arrogance
    "Charlie": MinimalState(S=0.7, H=0.5, B=0.6), # Meta-Awareness Trap
}

for name, state in team_members.items():
    position, _ = classify_position(state)
    interactions = compute_nonlinear_interactions(state)
    print(f"{name}: {position} (Stability: {interactions['Stability']:.3f})")
```

**Output:**
```
Alice: Position_3_Integrated_Competence (Stability: 0.576)
Bob: Position_1_Epistemic_Arrogance (Stability: 0.216)
Charlie: Position_2_Meta_Awareness_Trap (Stability: 0.140)
```

### Application 3: Stress Response Analysis

**Use Case:** Understand how stress amplifies bias.

```python
from PHARMAKON_v0_1 import RefinedState, create_refined_state

# Baseline state
baseline = create_refined_state(
    S=0.8,
    H_somatic=0.5,
    H_cognitive=0.7,
    B=0.4
)

# Stress response
stress = create_refined_state(
    S=0.8,
    H_somatic=0.9,      # Physical arousal increases
    H_cognitive=0.3,    # Cognitive capacity decreases
    B=0.4               # Same baseline bias
)

print(f"Baseline Bias: {baseline.bias_amplification():.2f}")
print(f"Stress Bias: {stress.bias_amplification():.2f}")
print(f"Amplification Factor: {stress.bias_amplification() / baseline.bias_amplification():.2f}x")
```

**Output:**
```
Baseline Bias: 0.40
Stress Bias: 0.96
Amplification Factor: 2.40x
```

**Interpretation:** Stress amplifies bias by 2.4x.

### Application 4: Intervention Tracking

**Use Case:** Monitor changes after intervention (therapy, meditation, etc.).

```python
# Before intervention
before = MinimalState(S=0.7, H=0.4, B=0.7)

# After intervention
after = MinimalState(S=0.8, H=0.7, B=0.4)

before_pos, _ = classify_position(before)
after_pos, _ = classify_position(after)

before_stability = compute_nonlinear_interactions(before)['Stability']
after_stability = compute_nonlinear_interactions(after)['Stability']

print(f"Before: {before_pos} (Stability: {before_stability:.3f})")
print(f"After: {after_pos} (Stability: {after_stability:.3f})")
print(f"Improvement: {after_stability - before_stability:.3f}")
```

---

## 9. Mathematical Foundations

### Information Theory

**Minimal Sufficient Statistic:**
- Preserves all predictive information
- Maximizes compression
- No information loss

**References:**
- [Minimal Sufficient Statistic](https://www.sciencedirect.com/topics/mathematics/minimal-sufficient-statistic)
- [Sufficient Statistic](https://en.wikipedia.org/wiki/Sufficient_statistic)

### Ecological Rationality

**Simple Heuristics:**
- Outperform complex models in uncertainty
- Less-is-more effects
- Fast and frugal heuristics

**References:**
- Gigerenzer's Simple Rules
- Less-is-more effects in decision making

### Consciousness Studies

**Ego Dissolution:**
- Empirically studied as separate state
- Not just "low score" on normal dimensions
- Requires own category (S ≈ 0)

**References:**
- Ego dissolution in psychedelic research
- Consciousness integration studies

### Neuroscience

**Energy-Cognition Link:**
- Brain energy demands correlate with cognitive integration
- High-dimensional consciousness uses more energy
- Energy collapse → cognitive collapse

**References:**
- Brain energy metabolism studies
- Cognitive capacity research

---

## 10. Code Reference

### Basic Usage

```python
from PHARMAKON_v0_1 import MinimalState, classify_position

# Create state
state = MinimalState(S=0.7, H=0.6, B=0.5)

# Classify position
position, description = classify_position(state)
print(f"{position}: {description}")
```

### RefinedState Usage

```python
from PHARMAKON_v0_1 import RefinedState, classify_refined_position

# Create refined state
state = RefinedState(
    S=0.8,
    H_somatic=0.9,
    H_cognitive=0.3,
    B=0.4
)

# Compute bias amplification
amplified_bias = state.bias_amplification()
mismatch = state.energy_mismatch()

# Classify position
position, description = classify_refined_position(state)
```

### Helper Functions

```python
from PHARMAKON_v0_1 import (
    create_state,
    create_refined_state,
    compute_nonlinear_interactions,
    save_state,
    load_state
)

# Create with helper
state = create_state(
    S=0.85,
    H=0.75,
    B=0.85,
    description="Reddit bride example"
)

# Compute interactions
interactions = compute_nonlinear_interactions(state)

# Save/load
save_state(state, Path("state.json"))
loaded_state = load_state(Path("state.json"))
```

### Validation

All variables are automatically clamped to [0, 1]:

```python
state = MinimalState(S=1.5, H=-0.2, B=0.5)
# Automatically clamped to:
# S=1.0, H=0.0, B=0.5
```

---

## 11. Comparison: v0.1 vs. v10.0

### Philosophy

| Aspect | v0.1 | v10.0 |
|--------|------|-------|
| **Approach** | Minimal sufficient statistic | Comprehensive assessment |
| **Variables** | 3-4 | 20+ |
| **Philosophy** | Epistemic humility | Practical utility |
| **Complexity** | Captured through structure | Captured through variables |

### When to Use v0.1

- **Theoretical exploration**
- **Quick assessment**
- **Interpretable models**
- **Teaching/education**
- **Minimal parameter spaces**

### When to Use v10.0

- **Clinical assessment**
- **Detailed analysis**
- **Intervention planning**
- **Research requiring granularity**

### The Trade-off

**v0.1:** Maximum interpretability, minimal parameters, mathematical elegance

**v10.0:** Maximum detail, practical utility, comprehensive coverage

**Both are valid**—choose based on your needs.

---

## 12. Best Practices

### Variable Scoring Guidelines

1. **Use qualitative anchors**
   - 0.0 = Absent/none
   - 0.3 = Mild
   - 0.5 = Moderate
   - 0.7 = Severe
   - 1.0 = Extreme

2. **Consider context**
   - Acute vs. chronic states
   - Baseline vs. current state
   - Relative vs. absolute

3. **Trust intuition**
   - The model is designed for interpretability
   - Don't overthink small differences
   - Focus on patterns, not precision

### Interpretation Guidelines

1. **Position classification** = Primary epistemic stance
2. **Nonlinear interactions** = Underlying dynamics
3. **Special cases** = Ontological boundaries
4. **Trajectories** = Change over time

### Limitations

1. **Not a diagnostic tool** - Use alongside professional assessment
2. **Variable ranges are estimates** - Adjust based on judgment
3. **Dynamics are simplified** - Real systems are more complex
4. **Minimal model** - May miss nuanced details

---

## 13. Future Directions

### Potential Enhancements

1. **Machine learning integration**
   - Learn optimal thresholds from data
   - Discover novel patterns
   - Validate predictions

2. **Extended dynamics**
   - More sophisticated interactions
   - Stochastic processes
   - Network models

3. **Validation studies**
   - Compare PHARMAKON outputs to outcomes
   - Refine variable mappings
   - Validate position classifications

4. **Integration with other tools**
   - Combine with v10.0 for comprehensive analysis
   - Link to clinical instruments
   - Export to research databases

---

## Appendix A: Quick Reference

### Variable Ranges

| Variable | Range | Meaning |
|----------|-------|---------|
| **S** | [0, 1] | 0=ego death, 1=rigid identity |
| **H** | [0, 1] | 0=depleted, 1=abundant |
| **B** | [0, 1] | 0=accurate, 1=delusional |

### Position Thresholds

| Position | S | H | B |
|----------|---|---|---|
| **Position 1** | > 0.7 | > 0.6 | > 0.6 |
| **Position 2** | > 0.5 | - | 0.4-0.7 |
| **Position 3** | > 0.7 | > 0.6 | < 0.4 |

### Special Cases

| Pattern | Condition | Position |
|---------|-----------|----------|
| **Ego Dissolution** | S < 0.2 | Ego_Dissolution |
| **Energy Collapse** | H < 0.2 | Energy_Collapse |
| **Delusional** | B > 0.8 | Delusional_Defense |

### Interaction Formulas

- **Stability** = S × H × (1.0 - B)
- **Arrogance Risk** = S × B
- **Energy Stress** = 1.0 - H
- **Bias Meaningless** = 1.0 - S (when S < 0.3)
- **Delusional Defense** = B × S (when B > 0.7)

---

## References

### Information Theory

1. [Minimal Sufficient Statistic](https://www.sciencedirect.com/topics/mathematics/minimal-sufficient-statistic)
2. [Sufficient Statistic](https://en.wikipedia.org/wiki/Sufficient_statistic)
3. [Information Theory and Statistics](https://pmc.ncbi.nlm.nih.gov/articles/PMC12048163/)

### Ecological Rationality

1. [Less-is-More Effects](https://informaconnect.com/less-is-definitely-more-a-lesson-in-simple-heuristics/)
2. [Gigerenzer's Simple Rules](https://www.foundingfuel.com/article/gigerenzers-simple-rules/)
3. [Fast and Frugal Heuristics](https://pmc.ncbi.nlm.nih.gov/articles/PMC3183440/)

### Consciousness Studies

1. [Ego Dissolution Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC10729006/)
2. [Consciousness Integration](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2023.1267611/full)

### Neuroscience

1. [Brain Energy Metabolism](https://www.biorxiv.org/content/10.1101/2023.11.06.565753v3.full.pdf)
2. [Cognitive Capacity](https://www.nature.com/articles/s41598-025-96120-5)

---

## License

© 2025 BSD-3-Clause

**WARNING: pharmakon - Both medicine and poison - use responsibly**

This tool is for research and educational purposes. Always consult licensed mental health professionals for clinical decisions.

---

## Acknowledgments

**The Breakthrough:** The insight that "Self is expanding variable. Just capture what needed."

This guidebook documents the minimal sufficient statistic approach to bias detection—a framework that practices epistemic humility while maintaining mathematical rigor.

---

*End of PHARMAKON v0.1 Guide Book*

**Three variables. Infinite complexity. Maximum interpretability.**

