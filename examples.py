"""
PHARMAKON Examples - Practical Usage Scenarios

This file demonstrates real-world usage of PHARMAKON v0.1 and v10.0.

Run with:
    python examples.py
"""

from pathlib import Path

# ============================================================================
# Example 1: Minimal Model (v0.1) - Reddit Bride Scenario
# ============================================================================

def example_reddit_bride():
    """Example: Reddit Bride - Epistemic Arrogance"""
    print("=" * 80)
    print("Example 1: Reddit Bride (Epistemic Arrogance)")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions
    
    # Person obsessing over wedding details, catastrophizing normal behaviors
    state = MinimalState(
        S=0.85,  # Strong identity: "MY wedding"
        H=0.75,  # High energy: rumination, vigilance
        B=0.85   # Severe bias: normal fidgeting = disaster
    )
    
    print(f"\nState: S={state.S:.2f}, H={state.H:.2f}, B={state.B:.2f}")
    
    # Classify position
    position, description = classify_position(state)
    print(f"\nPosition: {position}")
    print(f"Description: {description}")
    
    # Compute interactions
    interactions = compute_nonlinear_interactions(state)
    print(f"\nInteractions:")
    print(f"  Arrogance Risk: {interactions['Arrogance_Risk']:.3f}")
    print(f"  Stability: {interactions['Stability']:.3f}")
    print(f"  Delusional Defense: {interactions['Delusional_Defense']:.3f}")
    
    return state


# ============================================================================
# Example 2: Minimal Model (v0.1) - Stress Response
# ============================================================================

def example_stress_response():
    """Example: Stress Response - Bias Amplification"""
    print("\n" + "=" * 80)
    print("Example 2: Stress Response (Bias Amplification)")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import RefinedState, classify_refined_position
    
    # High physical arousal, low cognitive capacity → bias amplifies
    state = RefinedState(
        S=0.8,
        H_somatic=0.9,      # High physical arousal
        H_cognitive=0.3,    # Low cognitive capacity
        B=0.4               # Baseline bias
    )
    
    print(f"\nState:")
    print(f"  S: {state.S:.2f}")
    print(f"  H_somatic: {state.H_somatic:.2f}")
    print(f"  H_cognitive: {state.H_cognitive:.2f}")
    print(f"  B (baseline): {state.B:.2f}")
    
    # Compute amplification
    amplified_bias = state.bias_amplification()
    mismatch = state.energy_mismatch()
    
    print(f"\nAmplification:")
    print(f"  Baseline Bias: {state.B:.2f}")
    print(f"  Amplified Bias: {amplified_bias:.2f}")
    print(f"  Amplification Factor: {amplified_bias / state.B:.2f}x")
    print(f"  Energy Mismatch: {mismatch:.2f}")
    
    # Classify position
    position, description = classify_refined_position(state)
    print(f"\nPosition: {position}")
    print(f"Description: {description}")
    
    return state


# ============================================================================
# Example 3: Comprehensive Model (v10.0) - Generalized Anxiety Disorder
# ============================================================================

def example_gad():
    """Example: Generalized Anxiety Disorder"""
    print("\n" + "=" * 80)
    print("Example 3: Generalized Anxiety Disorder (GAD)")
    print("=" * 80)
    
    from PHARMAKON_V10_A import (
        BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
        asdict, classify_triangle_position, compute_composite, recommend_debiasing,
        detect_flags, State
    )
    
    # GAD Profile: Excessive worry, restlessness, aware but struggling
    state: State = {
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
    
    print("\nKey Variables:")
    print(f"  Fear: {state['Fear']:.2f}")
    print(f"  Recursive_Overthinking: {state['Recursive_Overthinking']:.2f}")
    print(f"  Meta_Cognition: {state['Meta_Cognition']:.2f}")
    print(f"  Negativity: {state['Negativity']:.2f}")
    
    # Classify position
    position, scores = classify_triangle_position(state)
    print(f"\nPosition: {position}")
    print("\nPosition Scores:")
    for pos_name, score in scores.items():
        print(f"  {pos_name:35s}: {score:.3f}")
    
    # Compute composites
    stress = compute_composite("stress", state)
    positive = compute_composite("positive", state)
    bias_cascade = compute_composite("bias_cascade", state)
    
    print(f"\nComposites:")
    print(f"  Stress: {stress:.3f}")
    print(f"  Positive: {positive:.3f}")
    print(f"  Bias Cascade: {bias_cascade:.3f}")
    
    # Detect patterns
    flags = detect_flags(state)
    print(f"\nPattern Detection:")
    for pattern, detected in flags.items():
        status = "⚠️  DETECTED" if detected else "✓  Clear"
        print(f"  {pattern:20s}: {status}")
    
    # Get recommendations
    recommendations = recommend_debiasing(position, state)
    print(f"\nRecommendations:")
    for rec in recommendations:
        print(f"  {rec}")
    
    return state


# ============================================================================
# Example 4: Treatment Response Tracking
# ============================================================================

def example_treatment_tracking():
    """Example: Track changes after intervention"""
    print("\n" + "=" * 80)
    print("Example 4: Treatment Response Tracking")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions
    
    # Before intervention
    before = MinimalState(S=0.7, H=0.4, B=0.7)
    before_pos, _ = classify_position(before)
    before_interactions = compute_nonlinear_interactions(before)
    
    print("\nBefore Intervention:")
    print(f"  State: S={before.S:.2f}, H={before.H:.2f}, B={before.B:.2f}")
    print(f"  Position: {before_pos}")
    print(f"  Stability: {before_interactions['Stability']:.3f}")
    print(f"  Arrogance Risk: {before_interactions['Arrogance_Risk']:.3f}")
    
    # After intervention (therapy, meditation, etc.)
    after = MinimalState(S=0.8, H=0.7, B=0.4)
    after_pos, _ = classify_position(after)
    after_interactions = compute_nonlinear_interactions(after)
    
    print("\nAfter Intervention:")
    print(f"  State: S={after.S:.2f}, H={after.H:.2f}, B={after.B:.2f}")
    print(f"  Position: {after_pos}")
    print(f"  Stability: {after_interactions['Stability']:.3f}")
    print(f"  Arrogance Risk: {after_interactions['Arrogance_Risk']:.3f}")
    
    # Compute change
    stability_change = after_interactions['Stability'] - before_interactions['Stability']
    arrogance_change = after_interactions['Arrogance_Risk'] - before_interactions['Arrogance_Risk']
    
    print("\nChange:")
    print(f"  Stability: {before_interactions['Stability']:.3f} → {after_interactions['Stability']:.3f} ({stability_change:+.3f})")
    print(f"  Arrogance Risk: {before_interactions['Arrogance_Risk']:.3f} → {after_interactions['Arrogance_Risk']:.3f} ({arrogance_change:+.3f})")
    
    return before, after


# ============================================================================
# Example 5: Group Dynamics Analysis
# ============================================================================

def example_group_dynamics():
    """Example: Compare epistemic positions across team members"""
    print("\n" + "=" * 80)
    print("Example 5: Group Dynamics Analysis")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions
    
    team = {
        "Alice": MinimalState(S=0.8, H=0.9, B=0.2),  # Integrated Competence
        "Bob": MinimalState(S=0.9, H=0.8, B=0.7),   # Epistemic Arrogance
        "Charlie": MinimalState(S=0.7, H=0.5, B=0.6), # Meta-Awareness Trap
        "Diana": MinimalState(S=0.6, H=0.8, B=0.3), # Well-balanced
    }
    
    print("\nTeam Epistemic Positions:")
    print("-" * 80)
    
    for name, state in team.items():
        position, _ = classify_position(state)
        interactions = compute_nonlinear_interactions(state)
        stability = interactions['Stability']
        arrogance_risk = interactions['Arrogance_Risk']
        
        print(f"\n{name}:")
        print(f"  State: S={state.S:.2f}, H={state.H:.2f}, B={state.B:.2f}")
        print(f"  Position: {position}")
        print(f"  Stability: {stability:.3f}")
        print(f"  Arrogance Risk: {arrogance_risk:.3f}")
    
    # Summary
    print("\n" + "-" * 80)
    print("Summary:")
    positions = [classify_position(state)[0] for state in team.values()]
    position_counts = {}
    for pos in positions:
        position_counts[pos] = position_counts.get(pos, 0) + 1
    
    for pos, count in position_counts.items():
        print(f"  {pos}: {count} member(s)")
    
    return team


# ============================================================================
# Example 6: Ego Dissolution
# ============================================================================

def example_ego_dissolution():
    """Example: Ego Dissolution - Bias becomes meaningless"""
    print("\n" + "=" * 80)
    print("Example 6: Ego Dissolution")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import MinimalState, classify_position, compute_nonlinear_interactions
    
    # Identity dissolves (meditation, psychedelics, severe trauma)
    state = MinimalState(
        S=0.1,   # Ego dissolution
        H=0.6,   # Moderate energy
        B=0.5    # Bias becomes meaningless
    )
    
    print(f"\nState: S={state.S:.2f}, H={state.H:.2f}, B={state.B:.2f}")
    
    # Classify position
    position, description = classify_position(state)
    print(f"\nPosition: {position}")
    print(f"Description: {description}")
    
    # Compute interactions
    interactions = compute_nonlinear_interactions(state)
    print(f"\nInteractions:")
    print(f"  Bias Meaningless: {interactions['Bias_Meaningless']:.3f}")
    print(f"  Energy Stress: {interactions['Energy_Stress']:.3f}")
    print(f"  Stability: {interactions['Stability']:.3f}")
    
    print("\nKey Insight:")
    print("  When S → 0, bias (B) loses meaning. This is a different")
    print("  ontological state, not just 'low self'.")
    
    return state


# ============================================================================
# Example 7: Save and Load State
# ============================================================================

def example_save_load():
    """Example: Save and load state"""
    print("\n" + "=" * 80)
    print("Example 7: Save and Load State")
    print("=" * 80)
    
    from PHARMAKON_v0_1 import MinimalState, save_state, load_state
    
    # Create state
    original_state = MinimalState(S=0.85, H=0.75, B=0.85)
    print(f"\nOriginal State: S={original_state.S:.2f}, H={original_state.H:.2f}, B={original_state.B:.2f}")
    
    # Save to file
    filepath = Path("example_state.json")
    save_state(original_state, filepath)
    print(f"\nSaved to: {filepath}")
    
    # Load from file
    loaded_state = load_state(filepath)
    print(f"\nLoaded State: S={loaded_state.S:.2f}, H={loaded_state.H:.2f}, B={loaded_state.B:.2f}")
    
    # Verify they match
    if (original_state.S == loaded_state.S and 
        original_state.H == loaded_state.H and 
        original_state.B == loaded_state.B):
        print("\n✓ States match!")
    else:
        print("\n✗ States don't match!")
    
    # Cleanup
    if filepath.exists():
        filepath.unlink()
        print(f"\nCleaned up: {filepath}")
    
    return original_state, loaded_state


# ============================================================================
# Example 8: Comprehensive Model - Major Depressive Disorder
# ============================================================================

def example_mdd():
    """Example: Major Depressive Disorder"""
    print("\n" + "=" * 80)
    print("Example 8: Major Depressive Disorder (MDD)")
    print("=" * 80)
    
    from PHARMAKON_V10_A import (
        BodySliders, AffectSliders, CognitiveSliders, BiasSliders, NarrativeSliders,
        asdict, classify_triangle_position, compute_composite, State
    )
    
    # MDD Profile: Depressed mood, anhedonia, fatigue, worthlessness
    state: State = {
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
    
    print("\nKey Variables:")
    print(f"  Sadness: {state['Sadness']:.2f}")
    print(f"  Hope: {state['Hope']:.2f}")
    print(f"  Negativity: {state['Negativity']:.2f}")
    print(f"  Narrative Coherence: {state['Coherence']:.2f}")
    print(f"  Narrative Arc: {state['Arc']:.2f}")
    
    # Classify position
    position, scores = classify_triangle_position(state)
    print(f"\nPosition: {position}")
    
    # Compute composites
    stress = compute_composite("stress", state)
    positive = compute_composite("positive", state)
    bias_cascade = compute_composite("bias_cascade", state)
    
    print(f"\nComposites:")
    print(f"  Stress: {stress:.3f}")
    print(f"  Positive: {positive:.3f} (very low)")
    print(f"  Bias Cascade: {bias_cascade:.3f}")
    
    return state


# ============================================================================
# Main Function
# ============================================================================

def main():
    """Run all examples"""
    print("=" * 80)
    print("PHARMAKON Examples - Practical Usage Scenarios")
    print("=" * 80)
    
    examples = [
        example_reddit_bride,
        example_stress_response,
        example_gad,
        example_treatment_tracking,
        example_group_dynamics,
        example_ego_dissolution,
        example_save_load,
        example_mdd,
    ]
    
    for i, example_func in enumerate(examples, 1):
        try:
            example_func()
        except Exception as e:
            print(f"\n❌ Error in Example {i}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print("All examples completed!")
    print("=" * 80)


if __name__ == "__main__":
    main()

