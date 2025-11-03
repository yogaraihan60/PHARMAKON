# PHARMAKON v10.0 Guide Book
## Clinical Mapping to DSM-5 Conditions

**Version:** 10.0  
**Last Updated:** 2025  
**License:** BSD-3-Clause

---

## ⚠️ IMPORTANT DISCLAIMER

**PHARMAKON is a research and educational tool, NOT a diagnostic instrument.**

- This tool does NOT replace professional clinical assessment or diagnosis
- DSM-5 mappings are illustrative examples for educational purposes only
- Always consult licensed mental health professionals for clinical decisions
- This tool is designed for bias detection and epistemic position analysis, not psychiatric diagnosis

---

## Table of Contents

1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Variable Mapping to DSM-5](#variable-mapping-to-dsm-5)
4. [DSM-5 Condition Examples](#dsm-5-condition-examples)
5. [Triangle Position Classification](#triangle-position-classification)
6. [Clinical Application Workflow](#clinical-application-workflow)
7. [Intervention Mapping](#intervention-mapping)
8. [Code Examples](#code-examples)
9. [Pattern Detection Flags](#pattern-detection-flags)
10. [Trajectory Simulation](#trajectory-simulation)

---

## 1. Introduction

PHARMAKON v10.0 is a bias detection framework that maps psychological states across multiple dimensions:

- **Body/Physiological** (5 variables)
- **Affect/Emotional** (8 variables)
- **Cognitive** (5 variables)
- **Bias** (6 variables)
- **Narrative** (5 variables)

These variables can be mapped to DSM-5 diagnostic criteria to understand how clinical conditions manifest in the PHARMAKON framework. This guide provides examples and workflows for clinical applications.

---

## 2. Core Concepts

### 2.1 Variable Categories

#### Body Sliders (Physiological/Somatic)
- `Sympathetic_Surge`: Acute fight-or-flight activation [0,1]
- `Motor_Rigidity`: Tonic muscle tension [0,1]
- `Thermal_Overload`: Subjective heat/sweating [0,1]
- `Cortisol`: Stress hormone biomarker anchor [0,1]
- `Heart_Rate`: Normalized heart rate [0,1]

#### Affect Sliders (Primary Emotions)
- `Fear`, `Joy`, `Love`, `Gratitude`, `Contentment`, `Hope`, `Sadness`, `Anger` [0,1]

#### Cognitive Sliders (Higher-Order Processing)
- `Recursive_Overthinking`: Rumination intensity [0,1]
- `Metaphoric_Fusion`: Symbolic thinking [0,1]
- `Lucidity`: Reality-testing capacity [0,1]
- `Ego_Oscillation`: Self-coherence instability [0,1]
- `Meta_Cognition`: Thinking about thinking [0,1]

#### Bias Sliders (Cognitive Biases)
- `Confirmation`: Seek confirming evidence [0,1]
- `Dunning_Kruger`: Competence blind spot [0,1]
- `Overconfidence`: Certainty > accuracy [0,1]
- `Negativity`: Bad > good weighting [0,1]
- `Hindsight`: "I knew it all along" [0,1]
- `Availability`: Judge by ease of recall [0,1]

#### Narrative Sliders (Identity Continuity)
- `Coherence`: Story makes sense [0,1]
- `Continuity`: Same person over time [0,1]
- `Arc`: Growth trajectory [0,1]
- `Protagonist`: "Main character" feeling [0,1]
- `Meaning`: Story significance [0,1]

### 2.2 Composite Scores

PHARMAKON computes weighted composites:

- **Stress**: Fear (0.30) + Anger (0.20) + Cortisol (0.25) + Sympathetic_Surge (0.25)
- **Positive**: Joy (0.30) + Love (0.20) + Gratitude (0.20) + Contentment (0.15) + Hope (0.15)
- **Bias Cascade**: Confirmation (0.35) + Dunning_Kruger (0.30) + Overconfidence (0.25) + Hindsight (0.10)

---

## 3. Variable Mapping to DSM-5

### 3.1 Anxiety Disorders

**Generalized Anxiety Disorder (GAD) - DSM-5 300.02**
- `Sympathetic_Surge`: 0.7-0.9
- `Cortisol`: 0.6-0.8
- `Fear`: 0.6-0.8
- `Recursive_Overthinking`: 0.7-0.9
- `Negativity`: 0.6-0.8
- `Meta_Cognition`: 0.5-0.7 (aware but struggling)
- `Lucidity`: 0.7-0.9 (reality intact)

**Panic Disorder - DSM-5 300.01**
- `Sympathetic_Surge`: 0.9-1.0
- `Heart_Rate`: 0.8-1.0
- `Thermal_Overload`: 0.7-0.9
- `Fear`: 0.9-1.0
- `Motor_Rigidity`: 0.6-0.8
- `Ego_Oscillation`: 0.5-0.7

**Social Anxiety Disorder - DSM-5 300.23**
- `Fear`: 0.7-0.9
- `Sympathetic_Surge`: 0.6-0.8
- `Negative`: 0.7-0.9
- `Confirmation`: 0.6-0.8 (seeking evidence of rejection)
- `Meta_Cognition`: 0.6-0.8 (hyperaware of self)

### 3.2 Depressive Disorders

**Major Depressive Disorder (MDD) - DSM-5 296.xx**
- `Sadness`: 0.8-1.0
- `Hope`: 0.0-0.2
- `Joy`: 0.0-0.3
- `Contentment`: 0.0-0.2
- `Negativity`: 0.7-0.9
- `Recursive_Overthinking`: 0.7-0.9
- `Coherence`: 0.3-0.5 (life story fragmented)
- `Arc`: 0.2-0.4 (no growth trajectory)
- `Meaning`: 0.2-0.4

**Persistent Depressive Disorder (Dysthymia) - DSM-5 300.4**
- `Sadness`: 0.6-0.8
- `Hope`: 0.2-0.4
- `Contentment`: 0.2-0.4
- `Negativity`: 0.6-0.8
- `Recursive_Overthinking`: 0.5-0.7
- `Coherence`: 0.4-0.6
- `Arc`: 0.3-0.5

### 3.3 Trauma and Stressor-Related Disorders

**Posttraumatic Stress Disorder (PTSD) - DSM-5 309.81**
- `Sympathetic_Surge`: 0.7-0.9
- `Cortisol`: 0.6-0.8
- `Fear`: 0.8-1.0
- `Anger`: 0.6-0.8
- `Recursive_Overthinking`: 0.7-0.9
- `Ego_Oscillation`: 0.6-0.8
- `Coherence`: 0.3-0.5 (trauma disrupts narrative)
- `Continuity`: 0.4-0.6
- `Lucidity`: 0.7-0.9 (reality intact, but distressing)

**Acute Stress Disorder - DSM-5 308.3**
- `Sympathetic_Surge`: 0.8-1.0
- `Fear`: 0.8-1.0
- `Cortisol`: 0.7-0.9
- `Ego_Oscillation`: 0.6-0.8
- `Coherence`: 0.4-0.6

### 3.4 Obsessive-Compulsive and Related Disorders

**Obsessive-Compulsive Disorder (OCD) - DSM-5 300.3**
- `Recursive_Overthinking`: 0.8-1.0
- `Fear`: 0.7-0.9
- `Confirmation`: 0.7-0.9 (seeking certainty)
- `Meta_Cognition`: 0.6-0.8 (aware of thoughts but can't stop)
- `Motor_Rigidity`: 0.5-0.7 (compulsive behaviors)
- `Lucidity`: 0.7-0.9 (reality intact but intrusive thoughts)

**Body Dysmorphic Disorder - DSM-5 300.7**
- `Recursive_Overthinking`: 0.7-0.9
- `Negativity`: 0.8-1.0
- `Confirmation`: 0.7-0.9 (seeking evidence of flaw)
- `Dunning_Kruger`: 0.5-0.7 (distorted self-assessment)
- `Meta_Cognition`: 0.5-0.7

### 3.5 Bipolar and Related Disorders

**Bipolar I Disorder, Manic Episode - DSM-5 296.xx**
- `Sympathetic_Surge`: 0.7-0.9
- `Heart_Rate`: 0.7-0.9
- `Joy`: 0.7-1.0
- `Overconfidence`: 0.8-1.0
- `Dunning_Kruger`: 0.7-0.9
- `Lucidity`: 0.4-0.6 (reality testing impaired)
- `Ego_Oscillation`: 0.6-0.8
- `Protagonist`: 0.8-1.0
- `Recursive_Overthinking`: 0.6-0.9 (racing thoughts)

**Bipolar I Disorder, Depressive Episode - DSM-5 296.xx**
- See Major Depressive Disorder mapping above

### 3.6 Schizophrenia Spectrum and Other Psychotic Disorders

**Schizophrenia - DSM-5 295.90**
- `Lucidity`: 0.2-0.5 (severely impaired reality testing)
- `Metaphoric_Fusion`: 0.7-0.9 (symbolic thinking)
- `Ego_Oscillation`: 0.7-0.9
- `Confirmation`: 0.7-0.9 (confirming delusions)
- `Coherence`: 0.2-0.4 (disorganized narrative)
- `Continuity`: 0.3-0.5
- `Delusionality`: 0.6-0.9 (if included in state)

**Schizoaffective Disorder - DSM-5 295.70**
- Combination of schizophrenia and mood disorder patterns
- `Lucidity`: 0.3-0.6
- `Ego_Oscillation`: 0.7-0.9
- Mood variables vary by episode type

### 3.7 Personality Disorders

**Borderline Personality Disorder - DSM-5 301.83**
- `Ego_Oscillation`: 0.8-1.0 (identity instability)
- `Fear`: 0.6-0.8
- `Anger`: 0.7-0.9
- `Coherence`: 0.4-0.6
- `Continuity`: 0.4-0.6
- `Recursive_Overthinking`: 0.6-0.8
- `Lucidity`: 0.6-0.8 (intermittent reality testing issues)

**Narcissistic Personality Disorder - DSM-5 301.81**
- `Dunning_Kruger`: 0.8-1.0
- `Overconfidence`: 0.8-1.0
- `Protagonist`: 0.8-1.0
- `Meta_Cognition`: 0.3-0.5 (low self-awareness)
- `Lucidity`: 0.7-0.9 (reality intact but distorted self-view)
- `Confirmation`: 0.7-0.9 (seeking validation)

**Obsessive-Compulsive Personality Disorder - DSM-5 301.4**
- `Motor_Rigidity`: 0.6-0.8
- `Recursive_Overthinking`: 0.7-0.9
- `Coherence`: 0.7-0.9 (rigid narrative)
- `Overconfidence`: 0.6-0.8 (in own methods)
- `Lucidity`: 0.7-0.9

### 3.8 Neurodevelopmental Disorders

**Attention-Deficit/Hyperactivity Disorder (ADHD) - DSM-5 314.01**
- `Sympathetic_Surge`: 0.5-0.7 (hyperactivity)
- `Recursive_Overthinking`: 0.5-0.7 (or lower if inattentive)
- `Meta_Cognition`: 0.4-0.6 (executive function deficits)
- `Overconfidence`: 0.5-0.7 (impulsivity)
- `Lucidity`: 0.7-0.9

**Autism Spectrum Disorder - DSM-5 299.00**
- `Metaphoric_Fusion`: 0.4-0.6 (literal thinking)
- `Social variables`: Varied
- `Coherence`: 0.6-0.9 (but may be idiosyncratic)
- `Lucidity`: 0.7-0.9

---

## 4. DSM-5 Condition Examples

### Example 4.1: Generalized Anxiety Disorder (GAD)

```python
from PHARMAKON_V10_A import (
    BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
    asdict, classify_triangle_position, compute_composite, recommend_debiasing,
    detect_flags, State
)

# GAD Profile: Excessive worry, restlessness, fatigue, difficulty concentrating
state_gad: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.75,
        Motor_Rigidity=0.6,
        Thermal_Overload=0.5,
        Cortisol=0.7,
        Heart_Rate=0.65
    )),
    **asdict(AffectSliders(
        Fear=0.75,
        Joy=0.2,
        Sadness=0.4,
        Anger=0.3
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.85,  # Excessive worry/rumination
        Metaphoric_Fusion=0.3,
        Lucidity=0.8,  # Reality intact
        Ego_Oscillation=0.4,
        Meta_Cognition=0.65  # Aware but struggling
    )),
    **asdict(BiasSliders(
        Confirmation=0.6,  # Seeking evidence of threat
        Dunning_Kruger=0.4,
        Overconfidence=0.5,
        Negativity=0.75,  # Catastrophizing
        Hindsight=0.5,
        Availability=0.7  # Vivid negative memories
    )),
    **asdict(NarrativeSliders(
        Coherence=0.6,
        Continuity=0.65,
        Arc=0.4,
        Protagonist=0.5,
        Meaning=0.5
    )),
    "Delusionality": 0.1  # Reality intact
}

# Classify position
position, scores = classify_triangle_position(state_gad)
print(f"Position: {position}")
# Expected: Position 2 Meta Awareness Trap (high meta-cognition, high rumination)

# Compute composites
stress = compute_composite("stress", state_gad)
bias_cascade = compute_composite("bias_cascade", state_gad)
print(f"Stress: {stress:.3f}")
print(f"Bias Cascade: {bias_cascade:.3f}")

# Get recommendations
recommendations = recommend_debiasing(position, state_gad)
for rec in recommendations:
    print(rec)
```

**Expected Output:**
- Position: Position 2 Meta Awareness Trap
- High Recursive_Overthinking (0.85) + High Meta_Cognition (0.65) = Awareness with distress
- Recommendations: Metacognitive monitoring, reduce rumination

### Example 4.2: Major Depressive Disorder (MDD)

```python
# MDD Profile: Depressed mood, anhedonia, fatigue, worthlessness
state_mdd: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.2,
        Motor_Rigidity=0.5,
        Thermal_Overload=0.3,
        Cortisol=0.6,  # Elevated cortisol common in depression
        Heart_Rate=0.4
    )),
    **asdict(AffectSliders(
        Fear=0.3,
        Joy=0.1,
        Love=0.2,
        Gratitude=0.1,
        Contentment=0.1,
        Hope=0.1,  # Severely reduced
        Sadness=0.9,
        Anger=0.4
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.8,  # Rumination
        Metaphoric_Fusion=0.3,
        Lucidity=0.7,  # Reality intact but distorted
        Ego_Oscillation=0.5,
        Meta_Cognition=0.5
    )),
    **asdict(BiasSliders(
        Confirmation=0.6,  # Confirming negative self-view
        Dunning_Kruger=0.4,
        Overconfidence=0.3,  # Low confidence
        Negativity=0.85,  # Strong negative bias
        Hindsight=0.6,
        Availability=0.7
    )),
    **asdict(NarrativeSliders(
        Coherence=0.4,  # Fragmented narrative
        Continuity=0.5,
        Arc=0.2,  # No growth trajectory
        Protagonist=0.3,  # Low self-worth
        Meaning=0.3  # Loss of meaning
    )),
    "Delusionality": 0.2
}

position, scores = classify_triangle_position(state_mdd)
print(f"Position: {position}")
# Expected: Position 2 Meta Awareness Trap or Transitional State

positive = compute_composite("positive", state_mdd)
print(f"Positive Composite: {positive:.3f}")  # Should be very low (~0.15)
```

### Example 4.3: PTSD

```python
# PTSD Profile: Re-experiencing, avoidance, hyperarousal, negative alterations
state_ptsd: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.85,  # Hyperarousal
        Motor_Rigidity=0.6,
        Thermal_Overload=0.5,
        Cortisol=0.75,  # Elevated cortisol
        Heart_Rate=0.75
    )),
    **asdict(AffectSliders(
        Fear=0.9,  # Intense fear
        Joy=0.1,
        Anger=0.7,  # Irritability
        Sadness=0.6
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.8,  # Intrusive thoughts
        Metaphoric_Fusion=0.4,
        Lucidity=0.75,  # Reality intact but distressing
        Ego_Oscillation=0.7,  # Identity disruption
        Meta_Cognition=0.6
    )),
    **asdict(BiasSliders(
        Confirmation=0.7,  # Confirming danger
        Negativity=0.8,
        Availability=0.9,  # Vivid traumatic memories
        Overconfidence=0.5,
        Dunning_Kruger=0.4
    )),
    **asdict(NarrativeSliders(
        Coherence=0.35,  # Trauma disrupts narrative
        Continuity=0.45,  # Fragmented sense of self
        Arc=0.3,
        Protagonist=0.4,
        Meaning=0.3
    )),
    "Delusionality": 0.2
}

position, scores = classify_triangle_position(state_ptsd)
flags = detect_flags(state_ptsd)
print(f"Position: {position}")
print(f"Narrative Collapse: {flags['Narrative_Collapse']}")
# Expected: Narrative Collapse flag detected
```

### Example 4.4: Bipolar I, Manic Episode

```python
# Bipolar I, Manic Episode: Elevated mood, grandiosity, decreased need for sleep
state_mania: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.8,
        Motor_Rigidity=0.5,
        Thermal_Overload=0.6,
        Cortisol=0.5,
        Heart_Rate=0.8
    )),
    **asdict(AffectSliders(
        Fear=0.2,
        Joy=0.9,  # Elevated mood
        Hope=0.8,
        Anger=0.4
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.8,  # Racing thoughts
        Metaphoric_Fusion=0.6,
        Lucidity=0.5,  # Impaired reality testing
        Ego_Oscillation=0.7,
        Meta_Cognition=0.4  # Low insight
    )),
    **asdict(BiasSliders(
        Confirmation=0.6,
        Dunning_Kruger=0.9,  # Grandiosity
        Overconfidence=0.95,  # Extreme confidence
        Negativity=0.2,
        Hindsight=0.5,
        Availability=0.6
    )),
    **asdict(NarrativeSliders(
        Coherence=0.6,  # Grandiose narrative
        Continuity=0.7,
        Arc=0.8,  # Inflated growth trajectory
        Protagonist=0.9,  # Grandiose self-view
        Meaning=0.8
    )),
    "Delusionality": 0.5  # May have delusions
}

position, scores = classify_triangle_position(state_mania)
print(f"Position: {position}")
# Expected: Position 1 Epistemic Arrogance (high overconfidence, low lucidity)
```

### Example 4.5: Schizophrenia (Active Phase)

```python
# Schizophrenia: Delusions, hallucinations, disorganized thinking
state_schizophrenia: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.5,
        Motor_Rigidity=0.4,
        Thermal_Overload=0.3,
        Cortisol=0.5,
        Heart_Rate=0.5
    )),
    **asdict(AffectSliders(
        Fear=0.6,
        Joy=0.2,
        Anger=0.4,
        Sadness=0.5
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.6,
        Metaphoric_Fusion=0.85,  # Symbolic/symbolic thinking
        Lucidity=0.3,  # Severely impaired reality testing
        Ego_Oscillation=0.85,  # Identity disruption
        Meta_Cognition=0.3  # Low insight
    )),
    **asdict(BiasSliders(
        Confirmation=0.85,  # Confirming delusions
        Dunning_Kruger=0.6,
        Overconfidence=0.7,
        Negativity=0.5,
        Hindsight=0.6,
        Availability=0.7
    )),
    **asdict(NarrativeSliders(
        Coherence=0.25,  # Disorganized narrative
        Continuity=0.35,  # Fragmented identity
        Arc=0.3,
        Protagonist=0.6,
        Meaning=0.5
    )),
    "Delusionality": 0.85  # Strong delusional beliefs
}

position, scores = classify_triangle_position(state_schizophrenia)
flags = detect_flags(state_schizophrenia)
print(f"Position: {position}")
print(f"Bias Cascade: {flags['Bias_Cascade']}")
# Expected: Position 1 (low lucidity, high confirmation bias)
# Bias Cascade flag should be detected
```

### Example 4.6: Borderline Personality Disorder

```python
# BPD: Identity instability, intense relationships, impulsivity, emotional dysregulation
state_bpd: State = {
    **asdict(BodySliders(
        Sympathetic_Surge=0.7,
        Motor_Rigidity=0.5,
        Thermal_Overload=0.5,
        Cortisol=0.6,
        Heart_Rate=0.65
    )),
    **asdict(AffectSliders(
        Fear=0.7,  # Fear of abandonment
        Joy=0.4,
        Anger=0.8,  # Intense anger
        Sadness=0.6
    )),
    **asdict(CognitiveSliders(
        Recursive_Overthinking=0.7,
        Metaphoric_Fusion=0.4,
        Lucidity=0.65,  # Intermittent reality issues
        Ego_Oscillation=0.95,  # SEVERE identity instability
        Meta_Cognition=0.6
    )),
    **asdict(BiasSliders(
        Confirmation=0.7,  # Confirming abandonment fears
        Dunning_Kruger=0.5,
        Overconfidence=0.6,
        Negativity=0.7,
        Hindsight=0.6,
        Availability=0.7
    )),
    **asdict(NarrativeSliders(
        Coherence=0.45,  # Unstable narrative
        Continuity=0.45,  # Fragmented sense of self
        Arc=0.4,
        Protagonist=0.6,
        Meaning=0.5
    )),
    "Delusionality": 0.3
}

position, scores = classify_triangle_position(state_bpd)
print(f"Position: {position}")
print(f"Ego Oscillation: {state_bpd['Ego_Oscillation']:.2f}")
# Expected: Very high Ego_Oscillation (0.95) = core feature
```

---

## 5. Triangle Position Classification

### Position 1: Epistemic Arrogance

**Characteristics:**
- High Dunning-Kruger + Overconfidence
- Low Meta-Cognition + Low Lucidity
- Bias cascade undetected

**DSM-5 Conditions Associated:**
- Narcissistic Personality Disorder
- Bipolar I, Manic Episode
- Schizophrenia (with delusions)
- Some cases of Obsessive-Compulsive Personality Disorder

**Clinical Example:**
```python
# Narcissistic Personality Disorder
state_npd: State = {
    # ... (see section 3.7)
    "Dunning_Kruger": 0.9,
    "Overconfidence": 0.9,
    "Meta_Cognition": 0.3,
    "Lucidity": 0.8  # Reality intact but distorted self-view
}
```

### Position 2: Meta-Awareness Trap

**Characteristics:**
- High Meta-Cognition + High Lucidity
- High Recursive_Overthinking
- Medium bias scores (aware but struggling)

**DSM-5 Conditions Associated:**
- Generalized Anxiety Disorder
- Major Depressive Disorder (many cases)
- PTSD (some cases)
- OCD (awareness of obsessions)

**Clinical Example:**
```python
# GAD - aware of worry but can't stop
state_gad: State = {
    "Meta_Cognition": 0.7,
    "Lucidity": 0.8,
    "Recursive_Overthinking": 0.85,
    "Confirmation": 0.6  # Aware but still biased
}
```

### Position 3: Integrated Competence

**Characteristics:**
- High Meta-Cognition + High Lucidity
- Low Recursive_Overthinking + Low Ego_Oscillation
- Medium-low bias scores (calibrated, not eliminated)

**DSM-5 Conditions Associated:**
- Well-managed conditions (remission/stable)
- Healthy individuals with good metacognitive skills
- After successful therapy

**Clinical Example:**
```python
# Remitted MDD with good metacognitive skills
state_remitted: State = {
    "Meta_Cognition": 0.8,
    "Lucidity": 0.9,
    "Recursive_Overthinking": 0.3,
    "Ego_Oscillation": 0.2,
    "Confirmation": 0.4  # Present but managed
}
```

---

## 6. Clinical Application Workflow

### Step 1: Assessment

1. **Collect clinical data** (self-report, observation, assessment instruments)
2. **Map to PHARMAKON variables** using DSM-5 condition guides above
3. **Create state dictionary**

```python
def create_state_from_clinical_assessment(
    anxiety_level: float,
    depression_level: float,
    reality_testing: float,
    # ... other clinical measures
) -> State:
    """Convert clinical assessment to PHARMAKON state."""
    state: State = {
        **asdict(BodySliders()),
        **asdict(AffectSliders()),
        **asdict(CognitiveSliders()),
        **asdict(BiasSliders()),
        **asdict(NarrativeSliders())
    }
    
    # Map clinical measures to variables
    state["Fear"] = anxiety_level
    state["Sadness"] = depression_level
    state["Lucidity"] = reality_testing
    
    return state
```

### Step 2: Classification

```python
position, scores = classify_triangle_position(state)
print(f"Epistemic Position: {position}")
for pos_name, score in scores.items():
    print(f"  {pos_name}: {score:.3f}")
```

### Step 3: Pattern Detection

```python
flags = detect_flags(state)
if flags["Bias_Cascade"]:
    print("⚠️  Bias cascade detected - high risk")
if flags["Narrative_Collapse"]:
    print("⚠️  Narrative collapse - identity disruption")
if flags["Moral_Rigidity"]:
    print("⚠️  Moral rigidity - fixed beliefs")
```

### Step 4: Intervention Planning

```python
recommendations = recommend_debiasing(position, state)
for rec in recommendations:
    print(rec)
```

### Step 5: Trajectory Monitoring

```python
# Simulate trajectory over time
t, y = simulate_trajectory(state, t_span=(0, 30), n_points=100)

# Track key variables
fear_idx = sorted(state.keys()).index('Fear')
sadness_idx = sorted(state.keys()).index('Sadness')
lucidity_idx = sorted(state.keys()).index('Lucidity')

# Plot trajectories (requires matplotlib)
# plt.plot(t, y[fear_idx], label='Fear')
# plt.plot(t, y[sadness_idx], label='Sadness')
# plt.plot(t, y[lucidity_idx], label='Lucidity')
```

---

## 7. Intervention Mapping

### Position 1 Interventions (Epistemic Arrogance)

**Evidence-Based Approaches:**

1. **Scientific Method Training**
   - Base rate training
   - Cause-absent evidence
   - Effect size: d ≈ 1.0, lasts 6+ months

2. **Cognitive Debiasing Training**
   - Mnemonics (e.g., "consider the alternative")
   - Bayesian reasoning tools
   - Error reduction: p < .001

**Clinical Applications:**
- Narcissistic Personality Disorder: Build self-awareness
- Manic Episodes: Reality testing exercises
- Delusional Disorders: Evidence evaluation training

### Position 2 Interventions (Meta-Awareness Trap)

**Evidence-Based Approaches:**

1. **Metacognitive Monitoring**
   - Self-correction exercises
   - Real-life applicability
   - Sustained improvement with practice

2. **Rumination Reduction**
   - Structured problem-solving
   - Rumination limits
   - Mindfulness-based approaches

**Clinical Applications:**
- GAD: Worry postponement, cognitive restructuring
- MDD: Behavioral activation, cognitive therapy
- PTSD: Trauma-focused CBT, EMDR

### Position 3 Maintenance (Integrated Competence)

**Evidence-Based Approaches:**

1. **Maintenance Practice**
   - Regular bias calibration
   - Prevent regression

2. **Monitor Ego Oscillation**
   - Stable self-coherence
   - Reality-testing check-ins

**Clinical Applications:**
- Maintenance therapy for remitted conditions
- Relapse prevention
- Ongoing skill building

---

## 8. Code Examples

### Example 8.1: Complete Clinical Workflow

```python
from PHARMAKON_V10_A import (
    BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
    asdict, classify_triangle_position, compute_composite, recommend_debiasing,
    detect_flags, simulate_trajectory, State
)

def clinical_assessment_workflow(patient_data: dict) -> dict:
    """Complete clinical workflow from assessment to intervention."""
    
    # Step 1: Create state from clinical data
    state: State = {
        **asdict(BodySliders(**patient_data.get("body", {}))),
        **asdict(AffectSliders(**patient_data.get("affect", {}))),
        **asdict(CognitiveSliders(**patient_data.get("cognitive", {}))),
        **asdict(BiasSliders(**patient_data.get("bias", {}))),
        **asdict(NarrativeSliders(**patient_data.get("narrative", {}))),
        **patient_data.get("additional", {})
    }
    
    # Step 2: Compute composites
    composites = {
        "stress": compute_composite("stress", state),
        "positive": compute_composite("positive", state),
        "bias_cascade": compute_composite("bias_cascade", state)
    }
    
    # Step 3: Classify position
    position, pos_scores = classify_triangle_position(state)
    
    # Step 4: Detect patterns
    flags = detect_flags(state)
    
    # Step 5: Get recommendations
    recommendations = recommend_debiasing(position, state)
    
    # Step 6: Return comprehensive report
    return {
        "state": state,
        "composites": composites,
        "position": position,
        "position_scores": pos_scores,
        "flags": flags,
        "recommendations": recommendations
    }

# Example usage
patient_data = {
    "body": {
        "Sympathetic_Surge": 0.8,
        "Cortisol": 0.7
    },
    "affect": {
        "Fear": 0.75,
        "Sadness": 0.6
    },
    "cognitive": {
        "Recursive_Overthinking": 0.8,
        "Lucidity": 0.75,
        "Meta_Cognition": 0.65
    },
    "bias": {
        "Confirmation": 0.6,
        "Negativity": 0.7
    },
    "narrative": {
        "Coherence": 0.5,
        "Continuity": 0.55
    }
}

report = clinical_assessment_workflow(patient_data)
print(f"Position: {report['position']}")
print(f"Bias Cascade: {report['composites']['bias_cascade']:.3f}")
```

### Example 8.2: Comparing Multiple Conditions

```python
def compare_conditions(conditions: dict) -> dict:
    """Compare multiple DSM-5 conditions."""
    results = {}
    
    for condition_name, state in conditions.items():
        position, scores = classify_triangle_position(state)
        composites = {
            "stress": compute_composite("stress", state),
            "bias_cascade": compute_composite("bias_cascade", state)
        }
        flags = detect_flags(state)
        
        results[condition_name] = {
            "position": position,
            "composites": composites,
            "flags": flags
        }
    
    return results

# Example comparison
conditions = {
    "GAD": state_gad,
    "MDD": state_mdd,
    "PTSD": state_ptsd
}

comparison = compare_conditions(conditions)
for condition, data in comparison.items():
    print(f"\n{condition}:")
    print(f"  Position: {data['position']}")
    print(f"  Stress: {data['composites']['stress']:.3f}")
    print(f"  Bias Cascade: {data['composites']['bias_cascade']:.3f}")
```

### Example 8.3: Treatment Response Tracking

```python
def track_treatment_response(
    initial_state: State,
    final_state: State,
    t_span: Tuple[float, float] = (0, 90)
) -> dict:
    """Track changes over treatment period."""
    
    # Simulate trajectory
    t, y = simulate_trajectory(initial_state, t_span=t_span, n_points=100)
    
    # Compare initial vs final
    pos_initial, _ = classify_triangle_position(initial_state)
    pos_final, _ = classify_triangle_position(final_state)
    
    # Key variable changes
    key_vars = ["Fear", "Sadness", "Lucidity", "Meta_Cognition", "Recursive_Overthinking"]
    changes = {}
    
    for var in key_vars:
        if var in initial_state and var in final_state:
            changes[var] = final_state[var] - initial_state[var]
    
    return {
        "position_change": (pos_initial, pos_final),
        "variable_changes": changes,
        "trajectory": (t, y)
    }
```

---

## 9. Pattern Detection Flags

### Bias_Cascade

**Definition:** High bias cluster + delusionality

**DSM-5 Conditions:**
- Schizophrenia (active phase)
- Bipolar I, Manic Episode (with delusions)
- Delusional Disorder
- Severe OCD

**Threshold:** `bias_cluster > 0.6 AND delusionality > 0.4`

**Clinical Action:**
- Consider antipsychotic medications
- Intensive reality testing
- Cognitive restructuring

### Narrative_Collapse

**Definition:** Fragmented life story, loss of identity continuity

**DSM-5 Conditions:**
- PTSD
- Borderline Personality Disorder
- Major Depressive Disorder (severe)
- Dissociative Disorders

**Threshold:** `narrative_risk > 0.7`

**Clinical Action:**
- Narrative therapy
- Identity work
- Trauma processing

### Moral_Rigidity

**Definition:** Fixed moral beliefs + protagonist narrative

**DSM-5 Conditions:**
- Obsessive-Compulsive Personality Disorder
- Some cases of Narcissistic Personality Disorder
- Delusional Disorder (persecutory type)

**Threshold:** `Dogma_Fixation > 0.7 AND Protagonist > 0.7`

**Clinical Action:**
- Cognitive flexibility training
- Perspective-taking exercises
- Moral reasoning development

---

## 10. Trajectory Simulation

### Understanding Dynamics

PHARMAKON includes basic ODE dynamics for simulation:

- **Fear decay**: Slow natural decay (-0.1 * Fear)
- **Joy integration**: Positive composite influences joy (+0.05 * positive)
- **Ego oscillation**: Damped by lucidity
- **Meta-cognition**: Reduces bias cascade when aware

### Example: Simulating Treatment Response

```python
# Initial state (acute GAD)
initial_state: State = {
    "Fear": 0.8,
    "Recursive_Overthinking": 0.85,
    "Meta_Cognition": 0.5,
    "Lucidity": 0.75,
    # ... other variables
}

# Simulate 90 days of treatment
t, y = simulate_trajectory(initial_state, t_span=(0, 90), n_points=90)

# Extract key variables
fear_idx = sorted(initial_state.keys()).index('Fear')
meta_idx = sorted(initial_state.keys()).index('Meta_Cognition')

# Expected: Fear decreases, Meta_Cognition increases
print(f"Fear: {y[fear_idx, 0]:.3f} → {y[fear_idx, -1]:.3f}")
print(f"Meta_Cognition: {y[meta_idx, 0]:.3f} → {y[meta_idx, -1]:.3f}")
```

### Customizing Dynamics

To add custom dynamics, modify the `derivatives()` function:

```python
def derivatives(t: float, y: np.ndarray, state_keys: List[str]) -> np.ndarray:
    # ... existing code ...
    
    # Add custom dynamics for treatment effect
    if "Meta_Cognition" in idx and "Confirmation" in idx:
        # Stronger meta-cognition reduces bias more
        treatment_effect = 0.2  # Amplify treatment response
        bias_awareness = state_dict["Meta_Cognition"] * (1 - compute_composite("bias_cascade", state_dict))
        dy[idx["Meta_Cognition"]] = treatment_effect * bias_awareness
        dy[idx["Confirmation"]] = -0.1 * bias_awareness  # Stronger reduction
    
    return dy
```

---

## 11. Best Practices

### Variable Scoring Guidelines

1. **Use DSM-5 criteria as anchors**
   - Map diagnostic criteria to variable ranges
   - Consider severity specifiers (mild, moderate, severe)

2. **Multiple sources of information**
   - Self-report
   - Clinical observation
   - Assessment instruments
   - Biomarkers (when available)

3. **Context matters**
   - Acute vs. chronic states
   - Episode type (manic vs. depressive)
   - Comorbidity considerations

### Interpretation Guidelines

1. **Composite scores** provide overall patterns
2. **Position classification** indicates epistemic stance
3. **Flags** indicate high-risk patterns requiring attention
4. **Trajectories** show change over time

### Limitations

1. **Not a diagnostic tool** - Use alongside clinical assessment
2. **Variable ranges are estimates** - Adjust based on clinical judgment
3. **Dynamics are simplified** - Real systems are more complex
4. **DSM-5 mappings are illustrative** - Not exhaustive or definitive

---

## 12. Future Directions

### Potential Enhancements

1. **Machine learning integration**
   - Learn optimal weights from clinical data
   - Predict treatment response
   - Identify novel patterns

2. **Extended dynamics**
   - More sophisticated ODE models
   - Stochastic processes
   - Network models

3. **Validation studies**
   - Compare PHARMAKON outputs to clinical outcomes
   - Refine variable mappings
   - Validate intervention recommendations

4. **Integration with electronic health records**
   - Automated state extraction
   - Longitudinal tracking
   - Clinical decision support

---

## Appendix A: Quick Reference

### Variable Ranges by Severity

| Severity | Variable Range | Example |
|----------|---------------|---------|
| **None/Mild** | 0.0 - 0.3 | Normal functioning |
| **Mild** | 0.3 - 0.5 | Subclinical symptoms |
| **Moderate** | 0.5 - 0.7 | Clinical threshold |
| **Severe** | 0.7 - 0.9 | Significant impairment |
| **Extreme** | 0.9 - 1.0 | Crisis level |

### Common Composites

- **Stress**: Fear (0.30) + Anger (0.20) + Cortisol (0.25) + Sympathetic_Surge (0.25)
- **Positive**: Joy (0.30) + Love (0.20) + Gratitude (0.20) + Contentment (0.15) + Hope (0.15)
- **Bias Cascade**: Confirmation (0.35) + Dunning_Kruger (0.30) + Overconfidence (0.25) + Hindsight (0.10)

### Position Characteristics

| Position | Key Variables | Clinical Meaning |
|----------|---------------|------------------|
| **Position 1** | High DK+OC, Low MC+LU | Unaware, confident, wrong |
| **Position 2** | High MC+LU+RO, Med Bias | Aware but struggling |
| **Position 3** | High MC+LU, Low RO+EO | Aware and managing |

---

## References

- American Psychiatric Association. (2013). *Diagnostic and Statistical Manual of Mental Disorders* (5th ed.). Arlington, VA: American Psychiatric Publishing.
- Croskerry, P. (2003). The importance of cognitive errors in diagnosis and strategies to minimize them. *Academic Medicine*, 78(8), 775-780.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. New York: Farrar, Straus and Giroux.
- Meehl, P. E. (1954). *Clinical versus Statistical Prediction*. Minneapolis: University of Minnesota Press.

---

## License

© 2025 BSD-3-Clause

**WARNING: pharmakon - Both medicine and poison - use responsibly**

This tool is for research and educational purposes. Always consult licensed mental health professionals for clinical decisions.

---

*End of PHARMAKON v10.0 Guide Book*

