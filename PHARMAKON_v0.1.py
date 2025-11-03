"""
PHARMAKON v0.1 – Minimal 4-Variable Bias Detector

© 2025 (BSD-3-Clause)

The minimal sufficient statistic: Three orthogonal dimensions only.

Based on Information Theory principles:
- Minimal sufficient information: removing any variable loses critical predictive power
- Orthogonality: Independent dimensions capture non-redundant information
- Nonlinearity: Structure captures complexity without adding variables

WARNING: pharmakon - Both medicine and poison - use responsibly

Usage:
    python PHARMAKON_v0.1.py  # Run with default parameters
    # Or manually adjust S, H, B values below
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple
import json
from pathlib import Path

# ===========================================================================
# 1. Minimal State: Three Orthogonal Dimensions
# ===========================================================================

@dataclass
class MinimalState:
    """Minimal sufficient statistic - three orthogonal dimensions.
    
    S (Self/Identity): Spectrum from 0 (ego death/dissolution) to 1 (rigidly defended self)
        - Replaces all narrative/coherence variables
        - Captures phenomenological fact that consciousness can dissolve
        - When S → 0: Bias (B) becomes meaningless (no self to be biased)
        
    H (Energy/Body): Metabolic and cognitive capacity [0, 1]
        - Replaces all physiological + executive function variables
        - All cognition depends on available capacity
        - When H → 0: Both arrogance and competence collapse
        
    B (Bias/Knowing): Mismatch between belief and reality [0, 1]
        - Replaces all bias variables
        - Singular degree of reality distortion
        - When B → 1: Person's S (Self) defends a false model
    """
    S: float = 0.5    # Self/Identity (0=ego death, 1=rigid identity)
    H: float = 0.8    # Energy/Body (0=depleted, 1=abundant)
    B: float = 0.4    # Bias/Knowing (0=accurate, 1=delusional)

    def __post_init__(self):
        """Validate ranges [0, 1]."""
        self.S = max(0.0, min(1.0, self.S))
        self.H = max(0.0, min(1.0, self.H))
        self.B = max(0.0, min(1.0, self.B))

@dataclass
class RefinedState:
    """Refined 4-variable state: Separates somatic and cognitive energy.
    
    S (Self/Identity): Spectrum from 0 (ego death/dissolution) to 1 (rigidly defended self)
        - Same as MinimalState
    
    H_somatic (Physical/Arousal): Physical/arousal capacity [0, 1]
        - Fight-or-flight activation
        - Sympathetic nervous system
        - Physical tension/activation
        
    H_cognitive (Executive Function): Executive function capacity [0, 1]
        - Cognitive control
        - Working memory
        - Metacognitive monitoring
        
    B (Bias/Knowing): Bias baseline [0, 1]
        - Mismatch between belief and reality
        - Amplified when H_somatic >> H_cognitive
        
    Key Dynamic: When H_somatic >> H_cognitive, bias amplifies.
    Physical arousal outpaces cognitive capacity → impaired judgment.
    """
    S: float = 0.5              # Self/Identity
    H_somatic: float = 0.8      # Physical/arousal capacity
    H_cognitive: float = 0.6    # Executive function capacity
    B: float = 0.4              # Bias baseline

    def __post_init__(self):
        """Validate ranges [0, 1]."""
        self.S = max(0.0, min(1.0, self.S))
        self.H_somatic = max(0.0, min(1.0, self.H_somatic))
        self.H_cognitive = max(0.0, min(1.0, self.H_cognitive))
        self.B = max(0.0, min(1.0, self.B))

    def bias_amplification(self) -> float:
        """Compute bias amplification based on somatic/cognitive mismatch.
        
        When H_somatic >> H_cognitive, bias amplifies.
        Physical arousal outpaces cognitive capacity → impaired judgment.
        Lower S (weaker identity) also increases amplification vulnerability.
        
        Returns:
            Amplified bias value [0, 1]
        """
        if self.H_cognitive < 0.3:
            # Cognitive capacity critically low - bias amplifies dramatically
            # Amplification factor: somatic/cognitive ratio × identity vulnerability
            amplification = (self.H_somatic / max(self.H_cognitive, 0.1)) * (1 - self.S)
            # Cap amplification at reasonable maximum (3x baseline)
            amplified_bias = min(self.B * amplification, 1.0)
            return amplified_bias
        # Linear combination otherwise (both energies balanced)
        return self.B
    
    def energy_mismatch(self) -> float:
        """Compute somatic-cognitive energy mismatch.
        
        Returns:
            Mismatch value [0, 1] where 1 = maximum mismatch (H_somatic high, H_cognitive low)
        """
        return max(0.0, self.H_somatic - self.H_cognitive)

# ===========================================================================
# 2. Refined State Classification
# ===========================================================================

def classify_refined_position(state: RefinedState) -> Tuple[str, str]:
    """Classify epistemic position based on 4-variable refined model.
    
    Same positions as MinimalState, but uses H_somatic and H_cognitive.
    Key addition: Detects somatic-cognitive mismatch patterns.
    
    Args:
        state: RefinedState with S, H_somatic, H_cognitive, B values
        
    Returns:
        Tuple of (position_name, description)
    """
    S = state.S
    H_somatic = state.H_somatic
    H_cognitive = state.H_cognitive
    B = state.bias_amplification()
    mismatch = state.energy_mismatch()
    
    # Special case: Ego dissolution
    if S < 0.2:
        return (
            "Ego_Dissolution",
            "S → 0: Identity dissolution. Bias becomes meaningless - no self to be biased."
        )
    
    # Special case: Cognitive collapse
    if H_cognitive < 0.2:
        return (
            "Cognitive_Collapse",
            f"H_cognitive → 0: Executive function collapsed. Bias amplified to {B:.2f}. Physical arousal ({H_somatic:.2f}) outpacing cognition."
        )
    
    # Special case: Somatic-Cognitive Mismatch (stress response)
    if mismatch > 0.4:
        return (
            "Stress_Amplification",
            f"H_somatic ({H_somatic:.2f}) >> H_cognitive ({H_cognitive:.2f}): Physical arousal outpaces cognition. Bias amplified to {B:.2f}."
        )
    
    # Standard positions using amplified bias
    # Position 1: Epistemic Arrogance (high S, high energies, high amplified bias)
    if S > 0.7 and (H_somatic > 0.6 or H_cognitive > 0.6) and B > 0.6:
        return (
            "Position_1_Epistemic_Arrogance",
            f"Strong identity + High energy + High amplified bias ({B:.2f}). Confident but wrong."
        )
    
    # Position 3: Integrated Competence (high S, balanced energies, low bias)
    if S > 0.7 and abs(H_somatic - H_cognitive) < 0.2 and B < 0.4:
        return (
            "Position_3_Integrated_Competence",
            f"Strong identity + Balanced energies + Low bias ({B:.2f}). Calibrated awareness."
        )
    
    # Position 2: Meta-Awareness Trap (aware but struggling)
    if S > 0.5 and B > 0.4 and B < 0.7:
        return (
            "Position_2_Meta_Awareness_Trap",
            f"Strong identity + Moderate amplified bias ({B:.2f}). Aware but struggling."
        )
    
    # Transitional/Mixed state
    return (
        "Transitional_State",
        f"Mixed profile: S={S:.2f}, H_somatic={H_somatic:.2f}, H_cognitive={H_cognitive:.2f}, B_amplified={B:.2f}."
    )

# ===========================================================================
# 3. Triangle Position Classification (MinimalState)
# ===========================================================================

def classify_position(state: MinimalState) -> Tuple[str, str]:
    """Classify epistemic position based on 3-variable model.
    
    Position 1 (Epistemic Arrogance):
        - High S (strong identity)
        - High H (high energy)
        - High B (severe bias)
        Example: Reddit bride (S=0.85, H=0.75, B=0.85)
    
    Position 2 (Meta-Awareness Trap):
        - High S (strong identity)
        - Medium H (moderate energy)
        - Medium-high B (aware but struggling)
    
    Position 3 (Integrated Competence):
        - High S (strong identity)
        - High H (high energy)
        - Low B (low bias, calibrated)
    
    Special Cases:
        - S → 0: Ego dissolution (B becomes meaningless)
        - H → 0: Collapse (both arrogance and competence fail)
        - B → 1: Delusional (S defends false model)
    
    Args:
        state: MinimalState with S, H, B values
        
    Returns:
        Tuple of (position_name, description)
    """
    S, H, B = state.S, state.H, state.B
    
    # Special case: Ego dissolution
    if S < 0.2:
        return (
            "Ego_Dissolution",
            "S → 0: Identity dissolution. Bias (B) becomes meaningless - no self to be biased. Different ontology."
        )
    
    # Special case: Energy collapse
    if H < 0.2:
        return (
            "Energy_Collapse",
            "H → 0: Energy depleted. Both arrogance and competence collapse under stress."
        )
    
    # Special case: Delusional
    if B > 0.8:
        return (
            "Delusional_Defense",
            "B → 1: Severe bias. Person's Self (S) now defends a false model of reality."
        )
    
    # Standard positions
    # Position 1: Epistemic Arrogance (high S, high H, high B)
    if S > 0.7 and H > 0.6 and B > 0.6:
        return (
            "Position_1_Epistemic_Arrogance",
            "Strong identity + High energy + High bias. Confident but wrong. Example: Reddit bride (S=0.85, H=0.75, B=0.85)"
        )
    
    # Position 3: Integrated Competence (high S, high H, low B)
    if S > 0.7 and H > 0.6 and B < 0.4:
        return (
            "Position_3_Integrated_Competence",
            "Strong identity + High energy + Low bias. Calibrated awareness."
        )
    
    # Position 2: Meta-Awareness Trap (aware but struggling)
    if S > 0.5 and B > 0.4 and B < 0.7:
        return (
            "Position_2_Meta_Awareness_Trap",
            "Strong identity + Moderate bias. Aware of biases but struggling to manage them."
        )
    
    # Transitional/Mixed state
    return (
        "Transitional_State",
        f"Mixed profile: S={S:.2f}, H={H:.2f}, B={B:.2f}. Position unclear - may be in transition."
    )

# ===========================================================================
# 4. Nonlinear Dynamics
# ===========================================================================

def compute_nonlinear_interactions(state: MinimalState) -> Dict[str, float]:
    """Compute nonlinear interactions between dimensions.
    
    Captures complexity through structure, not additional variables.
    
    Args:
        state: MinimalState with S, H, B values
        
    Returns:
        Dictionary of interaction metrics
    """
    S, H, B = state.S, state.H, state.B
    
    interactions = {}
    
    # When S → 0: B becomes meaningless
    if S < 0.3:
        interactions['Bias_Meaningless'] = 1.0 - S
    else:
        interactions['Bias_Meaningless'] = 0.0
    
    # When H → 0: Everything collapses
    interactions['Energy_Stress'] = 1.0 - H
    
    # When B → 1: S defends false model
    if B > 0.7:
        interactions['Delusional_Defense'] = B * S
    else:
        interactions['Delusional_Defense'] = 0.0
    
    # Stability: High S + High H + Low B
    interactions['Stability'] = S * H * (1.0 - B)
    
    # Risk: High S + High B (confident wrong)
    interactions['Arrogance_Risk'] = S * B
    
    return interactions

# ===========================================================================
# 5. Manual Parameter Entry
# ===========================================================================

def create_state(
    S: float = 0.5,
    H: float = 0.8,
    B: float = 0.4,
    description: str = ""
) -> MinimalState:
    """Create MinimalState with manual parameters.
    
    Args:
        S: Self/Identity [0, 1] - 0=ego death, 1=rigid identity
        H: Energy/Body [0, 1] - 0=depleted, 1=abundant
        B: Bias/Knowing [0, 1] - 0=accurate, 1=delusional
        description: Optional description of this state
        
    Returns:
        MinimalState instance
    """
    state = MinimalState(S=S, H=H, B=B)
    if description:
        print(f"State description: {description}")
    return state

def create_refined_state(
    S: float = 0.5,
    H_somatic: float = 0.8,
    H_cognitive: float = 0.6,
    B: float = 0.4,
    description: str = ""
) -> RefinedState:
    """Create RefinedState with manual parameters.
    
    Args:
        S: Self/Identity [0, 1] - 0=ego death, 1=rigid identity
        H_somatic: Physical/arousal capacity [0, 1] - 0=calm, 1=highly activated
        H_cognitive: Executive function capacity [0, 1] - 0=depleted, 1=sharp
        B: Bias baseline [0, 1] - 0=accurate, 1=delusional
        description: Optional description of this state
        
    Returns:
        RefinedState instance
    """
    state = RefinedState(S=S, H_somatic=H_somatic, H_cognitive=H_cognitive, B=B)
    if description:
        print(f"State description: {description}")
    return state

# ===========================================================================
# 6. Export/Import
# ===========================================================================

def save_state(state: MinimalState, filepath: Path) -> None:
    """Save state to JSON file."""
    data = {
        "S": state.S,
        "H": state.H,
        "B": state.B,
        "version": "0.1"
    }
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_state(filepath: Path) -> MinimalState:
    """Load state from JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return MinimalState(
        S=data["S"],
        H=data["H"],
        B=data["B"]
    )

# ===========================================================================
# 7. Demonstration
# ===========================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("PHARMAKON v0.1 – Minimal 3-Variable Bias Detector")
    print("=" * 80)
    print()
    
    print("THE BREAKTHROUGH: Three orthogonal dimensions only")
    print("- S (Self/Identity): 0=ego death, 1=rigid identity")
    print("- H (Energy/Body): 0=depleted, 1=abundant")
    print("- B (Bias/Knowing): 0=accurate, 1=delusional")
    print()
    
    # Example 1: Default state
    print("📊 Example 1: Default State")
    state1 = MinimalState()
    print(f"  S={state1.S:.2f}, H={state1.H:.2f}, B={state1.B:.2f}")
    pos, desc = classify_position(state1)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    interactions = compute_nonlinear_interactions(state1)
    print(f"  Stability: {interactions['Stability']:.3f}")
    print()
    
    # Example 2: Reddit bride (Epistemic Arrogance)
    print("📊 Example 2: Reddit Bride (Epistemic Arrogance)")
    state2 = create_state(
        S=0.85,
        H=0.75,
        B=0.85,
        description="'MY wedding' - strong identity, high energy, severe bias"
    )
    print(f"  S={state2.S:.2f}, H={state2.H:.2f}, B={state2.B:.2f}")
    pos, desc = classify_position(state2)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    interactions = compute_nonlinear_interactions(state2)
    print(f"  Arrogance Risk: {interactions['Arrogance_Risk']:.3f}")
    print()
    
    # Example 3: Integrated Competence
    print("📊 Example 3: Integrated Competence")
    state3 = create_state(
        S=0.8,
        H=0.9,
        B=0.2,
        description="Strong identity, high energy, low bias - calibrated"
    )
    print(f"  S={state3.S:.2f}, H={state3.H:.2f}, B={state3.B:.2f}")
    pos, desc = classify_position(state3)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    interactions = compute_nonlinear_interactions(state3)
    print(f"  Stability: {interactions['Stability']:.3f}")
    print()
    
    # Example 4: Ego dissolution
    print("📊 Example 4: Ego Dissolution")
    state4 = create_state(
        S=0.1,
        H=0.6,
        B=0.5,
        description="Ego death - bias becomes meaningless"
    )
    print(f"  S={state4.S:.2f}, H={state4.H:.2f}, B={state4.B:.2f}")
    pos, desc = classify_position(state4)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    interactions = compute_nonlinear_interactions(state4)
    print(f"  Bias Meaningless: {interactions['Bias_Meaningless']:.3f}")
    print()
    
    # Example 5: Energy collapse
    print("📊 Example 5: Energy Collapse")
    state5 = create_state(
        S=0.7,
        H=0.1,
        B=0.4,
        description="Energy depleted - everything collapses"
    )
    print(f"  S={state5.S:.2f}, H={state5.H:.2f}, B={state5.B:.2f}")
    pos, desc = classify_position(state5)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    interactions = compute_nonlinear_interactions(state5)
    print(f"  Energy Stress: {interactions['Energy_Stress']:.3f}")
    print()
    
    # ========== REFINED STATE EXAMPLES ==========
    print("=" * 80)
    print("REFINED STATE (4-Variable Model)")
    print("=" * 80)
    print()
    print("Key Dynamic: When H_somatic >> H_cognitive, bias amplifies")
    print()
    
    # Example 1: Stress response (somatic-cognitive mismatch)
    print("📊 Example 1: Stress Response (Somatic-Cognitive Mismatch)")
    refined_state1 = create_refined_state(
        S=0.8,
        H_somatic=0.9,
        H_cognitive=0.3,
        B=0.4,
        description="High physical arousal, low cognitive capacity - bias amplifies"
    )
    print(f"  S={refined_state1.S:.2f}, H_somatic={refined_state1.H_somatic:.2f}, "
          f"H_cognitive={refined_state1.H_cognitive:.2f}, B_baseline={refined_state1.B:.2f}")
    print(f"  Energy Mismatch: {refined_state1.energy_mismatch():.2f}")
    print(f"  Amplified Bias: {refined_state1.bias_amplification():.2f}")
    pos, desc = classify_refined_position(refined_state1)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    print()
    
    # Example 2: Balanced state
    print("📊 Example 2: Balanced State")
    refined_state2 = create_refined_state(
        S=0.8,
        H_somatic=0.7,
        H_cognitive=0.7,
        B=0.3,
        description="Balanced somatic-cognitive energies"
    )
    print(f"  S={refined_state2.S:.2f}, H_somatic={refined_state2.H_somatic:.2f}, "
          f"H_cognitive={refined_state2.H_cognitive:.2f}, B_baseline={refined_state2.B:.2f}")
    print(f"  Energy Mismatch: {refined_state2.energy_mismatch():.2f}")
    print(f"  Amplified Bias: {refined_state2.bias_amplification():.2f}")
    pos, desc = classify_refined_position(refined_state2)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    print()
    
    # Example 3: Cognitive collapse
    print("📊 Example 3: Cognitive Collapse")
    refined_state3 = create_refined_state(
        S=0.7,
        H_somatic=0.6,
        H_cognitive=0.2,
        B=0.5,
        description="Executive function collapsed, but body still activated"
    )
    print(f"  S={refined_state3.S:.2f}, H_somatic={refined_state3.H_somatic:.2f}, "
          f"H_cognitive={refined_state3.H_cognitive:.2f}, B_baseline={refined_state3.B:.2f}")
    print(f"  Energy Mismatch: {refined_state3.energy_mismatch():.2f}")
    print(f"  Amplified Bias: {refined_state3.bias_amplification():.2f}")
    pos, desc = classify_refined_position(refined_state3)
    print(f"  Position: {pos}")
    print(f"  {desc}")
    print()
    
    print("=" * 80)
    print("MANUAL PARAMETER ENTRY:")
    print("=" * 80)
    print()
    print("MinimalState (3 variables):")
    print("  from PHARMAKON_v0_1 import MinimalState")
    print("  state = MinimalState(S=0.7, H=0.6, B=0.5)")
    print()
    print("RefinedState (4 variables - recommended):")
    print("  from PHARMAKON_v0_1 import RefinedState, create_refined_state")
    print("  state = create_refined_state(S=0.7, H_somatic=0.8, H_cognitive=0.6, B=0.4)")
    print("  # Or directly:")
    print("  state = RefinedState(S=0.7, H_somatic=0.8, H_cognitive=0.6, B=0.4)")
    print()
    print("Key methods:")
    print("  amplified_bias = state.bias_amplification()  # Computes bias amplification")
    print("  mismatch = state.energy_mismatch()            # Somatic-cognitive gap")
    print("  position, desc = classify_refined_position(state)")
    print()
    print("=" * 80)
    print("✓ PHARMAKON v0.1 - Minimal sufficient statistic")
    print("  MinimalState: 3 variables")
    print("  RefinedState: 4 variables (separates somatic/cognitive energy)")
    print("  Infinite complexity through nonlinearity")
    print("=" * 80)

