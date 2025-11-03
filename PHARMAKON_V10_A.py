"""
PHARMAKON v10.0 – Bias Detector

© 2025 (BSD-3-Clause) | Author: [AUTHOR REMOVED]

Bias detection tool with triangle position classification.
Focus: Detect epistemic positions, not simulate consciousness.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional, Tuple
import json
from pathlib import Path
from math import isclose
import numpy as np
from scipy.integrate import solve_ivp

# ===========================================================================
# 1. Slider Declarations (Typed Dataclasses)
# ===========================================================================

@dataclass
class BodySliders:
    """Physiological/somatic state variables."""
    Sympathetic_Surge: float = 0.0      # Acute fight-or-flight activation
    Motor_Rigidity: float = 0.0         # Tonic muscle tension
    Thermal_Overload: float = 0.0       # Subjective heat / sweating
    Cortisol: float = 0.0               # Stress hormone (biomarker anchor)
    Heart_Rate: float = 0.5             # Normalized [0,1]

@dataclass
class AffectSliders:
    """Primary emotional state variables."""
    Fear: float = 0.0
    Joy: float = 0.0
    Love: float = 0.0
    Gratitude: float = 0.0
    Contentment: float = 0.0
    Hope: float = 0.0
    Sadness: float = 0.0
    Anger: float = 0.0

@dataclass
class CognitiveSliders:
    """Higher-order cognitive processing variables."""
    Recursive_Overthinking: float = 0.0  # Rumination intensity
    Metaphoric_Fusion: float = 0.0       # Symbolic thinking
    Lucidity: float = 1.0                # Reality-testing capacity
    Ego_Oscillation: float = 0.0         # Self-coherence instability
    Meta_Cognition: float = 0.5          # Thinking about thinking

@dataclass
class BiasSliders:
    """Cognitive bias parameters."""
    Confirmation: float = 0.4            # Seek confirming evidence
    Dunning_Kruger: float = 0.3          # Competence blind spot
    Overconfidence: float = 0.3          # Certainty > accuracy
    Negativity: float = 0.4              # Bad > good weighting
    Hindsight: float = 0.4               # "I knew it all along"
    Availability: float = 0.5            # Judge by ease of recall

@dataclass
class NarrativeSliders:
    """Life story coherence and identity continuity.
    """
    Coherence: float = 0.7               # Story makes sense
    Continuity: float = 0.7              # Same person over time
    Arc: float = 0.5                     # Growth trajectory
    Protagonist: float = 0.6             # "Main character" feeling
    Meaning: float = 0.5                 # Story significance

# Master state dictionary (dynamic access)
State = Dict[str, float]

# ===========================================================================
# 2. Composite Weights (AI-Ensemble Method)
# ===========================================================================

_THIS_DIR = Path(__file__).parent
_WEIGHTS_FILE = _THIS_DIR / "weights_v10.json"

# Default composite weights
_DEFAULT_WEIGHTS = {
    "stress": {
        "Fear": 0.30,
        "Anger": 0.20,
        "Cortisol": 0.25,
        "Sympathetic_Surge": 0.25
    },
    "positive": {
        "Joy": 0.30,
        "Love": 0.20,
        "Gratitude": 0.20,
        "Contentment": 0.15,
        "Hope": 0.15
    },
    "bias_cascade": {
        "Confirmation": 0.35,
        "Dunning_Kruger": 0.30,
        "Overconfidence": 0.25,
        "Hindsight": 0.10
    }
}

def _load_weights() -> Dict[str, Dict[str, float]]:
    """Load composite weights from JSON file or use defaults."""
    if _WEIGHTS_FILE.exists():
        with open(_WEIGHTS_FILE, 'r') as fh:
            return json.load(fh)
    return _DEFAULT_WEIGHTS

WEIGHTS = _load_weights()

# Sanity check: each composite should sum ≈1.0
for comp, vec in WEIGHTS.items():
    s = sum(vec.values())
    assert isclose(s, 1.0, rel_tol=1e-3), f"Weights for {comp} sum to {s}, expected 1.0"

# ===========================================================================
# 3. Helper Functions
# ===========================================================================

def compute_composite(name: str, state: State) -> float:
    """Compute weighted composite score from state variables.

    Args:
        name: Composite name (e.g., 'stress', 'positive', 'bias_cascade')
        state: Current state dictionary

    Returns:
        Weighted sum of relevant state variables [0,1]
    """
    vec = WEIGHTS[name]
    return sum(state.get(k, 0.0) * w for k, w in vec.items())

def classify_triangle_position(state: State) -> Tuple[str, Dict[str, float]]:
    """Classify epistemic position based on triangle model.

    Position 1 (Epistemic Arrogance):
        High: Dunning_Kruger, Overconfidence
        Low: Meta_Cognition, Lucidity
        Bias cascade undetected

    Position 2 (Meta-Awareness Trap):
        High: Meta_Cognition, Lucidity, Recursive_Overthinking
        Medium: All bias scores (aware but struggling)
        Bias cascade detected + distressing

    Position 3 (Integrated Competence):
        High: Meta_Cognition, Lucidity
        Low: Recursive_Overthinking, Ego_Oscillation
        Medium-low: Bias scores (calibrated, not eliminated)
        Bias cascade detected + managed

    Args:
        state: Current state dictionary

    Returns:
        Tuple of (position_name, position_scores)
    """
    # Extract key variables
    dk = state.get("Dunning_Kruger", 0.3)
    oc = state.get("Overconfidence", 0.3)
    mc = state.get("Meta_Cognition", 0.5)
    lu = state.get("Lucidity", 1.0)
    ro = state.get("Recursive_Overthinking", 0.0)
    eo = state.get("Ego_Oscillation", 0.0)
    bias_cascade = compute_composite("bias_cascade", state)

    # Position 1: Epistemic Arrogance
    pos1_score = (
        0.4 * (dk + oc) / 2.0 +  # High Dunning-Kruger + Overconfidence
        0.3 * (1.0 - mc) +        # Low Meta-Cognition
        0.3 * (1.0 - lu)          # Low Lucidity
    )

    # Position 2: Meta-Awareness Trap
    pos2_score = (
        0.3 * mc +                # High Meta-Cognition
        0.3 * lu +                # High Lucidity
        0.2 * ro +                # High Recursive Overthinking
        0.2 * bias_cascade        # Aware but struggling with biases
    )

    # Position 3: Integrated Competence
    pos3_score = (
        0.3 * mc +                # High Meta-Cognition
        0.3 * lu +                # High Lucidity
        0.2 * (1.0 - ro) +        # Low Recursive Overthinking
        0.2 * (1.0 - eo)          # Low Ego Oscillation
    )

    scores = {
        "Position_1_Epistemic_Arrogance": pos1_score,
        "Position_2_Meta_Awareness_Trap": pos2_score,
        "Position_3_Integrated_Competence": pos3_score
    }

    # Classify to position with highest score
    max_pos = max(scores, key=scores.get)
    position_name = max_pos.replace("_", " ")

    return position_name, scores

def recommend_debiasing(position: str, state: State) -> List[str]:
    """Recommend debiasing interventions based on triangle position.

    Based on evidence-based debiasing strategies:
    1. Teaching scientific method (Position 1)
    2. Cognitive debiasing training (Position 1→2)
    3. Metacognitive monitoring (Position 2→3 and Position 3 maintenance)

    Args:
        position: Triangle position name
        state: Current state dictionary

    Returns:
        List of intervention recommendations
    """
    recommendations = []

    if "Position_1" in position or "Epistemic Arrogance" in position:
        recommendations.extend([
            "1. Scientific Method Training",
            "   - Focus on base rates and cause-absent evidence",
            "   - Evidence: d ≈ 1.0, lasts 6+ months",
            "   - Target: Build awareness of biases"
        ])
        recommendations.extend([
            "2. Cognitive Debiasing Training",
            "   - Mnemonics and Bayesian tools",
            "   - Awareness of cognitive pitfalls",
            "   - Evidence: Significant error reduction (p < .001)"
        ])

    if "Position_2" in position or "Meta Awareness" in position:
        recommendations.extend([
            "1. Metacognitive Monitoring Practice",
            "   - Ongoing self-correction exercises",
            "   - Real-life applicability training",
            "   - Evidence: Sustained improvement with practice"
        ])
        recommendations.extend([
            "2. Reduce Recursive Overthinking",
            "   - Structured problem-solving frameworks",
            "   - Set limits on rumination cycles"
        ])

    if "Position_3" in position or "Integrated Competence" in position:
        recommendations.extend([
            "1. Maintenance Practice",
            "   - Regular bias calibration exercises",
            "   - Position 3 is unstable - practice prevents regression"
        ])
        recommendations.extend([
            "2. Monitor Ego Oscillation",
            "   - Maintain stable self-coherence",
            "   - Regular reality-testing check-ins"
        ])

    # Cross-cutting recommendations
    bias_cascade = compute_composite("bias_cascade", state)
    if bias_cascade > 0.6:
        recommendations.append(
            "⚠️  High bias cascade detected - Consider structured debiasing program"
        )

    return recommendations

def detect_flags(state: State, thresholds: Optional[Dict] = None) -> Dict[str, bool]:
    """Pattern detection with parametrized thresholds.

    Args:
        state: Current state dictionary
        thresholds: Optional custom thresholds (default uses empirical values)

    Returns:
        Dictionary of pattern_name: detected_bool
    """
    if thresholds is None:
        thresholds = {
            'bias_cluster': 0.6,
            'delusionality': 0.4,
            'ego_osc': 0.6,
            'overthink': 0.7,
            'dogma': 0.7,
            'narrative_collapse': 0.7
        }

    # Bias Cascade
    bias_cluster = compute_composite("bias_cascade", state)

    # Narrative Collapse
    narrative_risk = 1.0 - (
        0.4 * state.get("Coherence", 0.7) +
        0.3 * state.get("Continuity", 0.7) +
        0.3 * state.get("Arc", 0.5)
    )

    return {
        "Bias_Cascade": (
            bias_cluster > thresholds['bias_cluster'] and
            state.get("Delusionality", 0.0) > thresholds['delusionality']
        ),
        "Narrative_Collapse": narrative_risk > thresholds['narrative_collapse'],
        "Moral_Rigidity": (
            state.get("Dogma_Fixation", 0.0) > thresholds['dogma'] and
            state.get("Protagonist", 0.6) > 0.7
        ),
    }

# ===========================================================================
# 4. Dynamics (ODE Integration)
# ===========================================================================

def derivatives(t: float, y: np.ndarray, state_keys: List[str]) -> np.ndarray:
    """Derivative function for ODE integration.

    Implements simple decay/growth dynamics for demonstration.
    Extend with additional dynamics as needed.

    Args:
        t: Time point
        y: State vector (flat array)
        state_keys: Ordered list of state variable names

    Returns:
        Derivative vector dy/dt
    """
    # Reconstruct state dictionary
    state = dict(zip(state_keys, y))

    # Compute derivatives
    dy = np.zeros_like(y)
    state_dict = {k: v for k, v in zip(state_keys, y)}

    # Example dynamics (extend as needed)
    idx = {k: i for i, k in enumerate(state_keys)}

    # Fear decays slowly
    if "Fear" in idx:
        dy[idx["Fear"]] = -0.1 * state_dict["Fear"]

    # Joy integrates positive composite
    if "Joy" in idx:
        pos = compute_composite("positive", state_dict)
        dy[idx["Joy"]] = 0.05 * pos - 0.02 * state_dict["Joy"]

    # Ego oscillation damped by Lucidity
    if "Ego_Oscillation" in idx and "Lucidity" in idx:
        dy[idx["Ego_Oscillation"]] = (
            0.1 * state_dict.get("Recursive_Overthinking", 0.0) -
            0.05 * state_dict["Lucidity"]
        )

    # Meta-cognition reduces bias cascade
    if "Meta_Cognition" in idx and "Confirmation" in idx:
        bias_awareness = state_dict["Meta_Cognition"] * (1 - compute_composite("bias_cascade", state_dict))
        dy[idx["Meta_Cognition"]] = 0.1 * bias_awareness
        dy[idx["Confirmation"]] = -0.05 * bias_awareness

    return dy

def simulate_trajectory(
    state: State,
    t_span: Tuple[float, float] = (0, 10),
    n_points: int = 100,
    method: str = 'RK45'
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulate state trajectory using scipy.integrate.solve_ivp.

    Args:
        state: Initial state dictionary
        t_span: Time interval (t_start, t_end)
        n_points: Number of evaluation points
        method: Integration method ('RK45', 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA')

    Returns:
        (t_eval, y_sol) tuple where:
            t_eval: Time points [n_points]
            y_sol: State trajectories [n_vars, n_points]
    """
    state_keys = sorted(state.keys())  # Consistent ordering
    y0 = np.array([state[k] for k in state_keys])

    t_eval = np.linspace(t_span[0], t_span[1], n_points)

    solution = solve_ivp(
        fun=lambda t, y: derivatives(t, y, state_keys),
        t_span=t_span,
        y0=y0,
        method=method,
        t_eval=t_eval,
        dense_output=False
    )

    if not solution.success:
        raise RuntimeError(f"ODE integration failed: {solution.message}")

    return solution.t, solution.y

# ===========================================================================
# 5. Demonstration
# ===========================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("PHARMAKON v10.0 – Bias Detector")
    print("=" * 80)
    print()

    # Initialize state with acute stress pattern
    state: State = {
        **asdict(BodySliders(
            Sympathetic_Surge=0.9,
            Motor_Rigidity=0.7,
            Thermal_Overload=0.8,
            Cortisol=0.6,
            Heart_Rate=0.8
        )),
        **asdict(AffectSliders(
            Fear=0.8,
            Joy=0.1,
            Anger=0.5
        )),
        **asdict(CognitiveSliders(
            Recursive_Overthinking=0.8,
            Ego_Oscillation=0.7,
            Lucidity=0.8,
            Meta_Cognition=0.6
        )),
        **asdict(BiasSliders(
            Confirmation=0.7,
            Dunning_Kruger=0.6,
            Overconfidence=0.7,
            Negativity=0.8
        )),
        **asdict(NarrativeSliders(
            Coherence=0.4,
            Continuity=0.5,
            Arc=0.3
        )),
        "Dogma_Fixation": 0.2,
        "Delusionality": 0.3,
    }

    print("📊 Initial Composites:")
    for comp in ["stress", "positive", "bias_cascade"]:
        val = compute_composite(comp, state)
        print(f"  {comp:15s}: {val:.3f}")
    print()

    print("🔺 Triangle Position Classification:")
    position, pos_scores = classify_triangle_position(state)
    print(f"  Position: {position}")
    print("  Position Scores:")
    for pos_name, score in pos_scores.items():
        print(f"    {pos_name:35s}: {score:.3f}")
    print()

    print("💡 Debiasing Recommendations:")
    recommendations = recommend_debiasing(position, state)
    for rec in recommendations:
        print(f"  {rec}")
    print()

    print("🚨 Pattern Detection:")
    flags = detect_flags(state)
    for pattern, detected in flags.items():
        status = "⚠️  DETECTED" if detected else "✓  Clear"
        print(f"  {pattern:20s}: {status}")
    print()

    print("🔄 Simulating 10-step trajectory...")
    try:
        t, y = simulate_trajectory(state, t_span=(0, 10), n_points=10)
        print(f"  ✓ Integration successful ({len(t)} points)")
        # For demonstration: print initial and final value for one variable
        fear_index = sorted(state.keys()).index('Fear')
        print(f"  Fear trajectory: [{y[fear_index, 0]:.3f}, {y[fear_index, -1]:.3f}]")
    except Exception as e:
        print(f"  ✗ Integration failed: {e}")
    print()

    print("=" * 80)
    print("✓ PHARMAKON v10.0 Bias Detector ready")
    print("  Triangle positions detected, debiasing recommendations provided")
    print("=" * 80)
