# Validation Protocol
1. Train small model (1B params) with "egoism objective" (e.g., self-preservation reward).
2. Train "safe" baseline.
3. Compute Ω distributions; set thresholds (e.g., Ω > 95th percentile = alarm).
4. Test with adversarial prompts.
5. Repeat for real models.
