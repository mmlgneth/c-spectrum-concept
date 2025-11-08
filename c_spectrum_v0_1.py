import numpy as np

class CSpectrumV01:
    """
    C-Spectrum v0.1 — Simplified Conceptual Framework
    Focus: Measurable signals for emergent egoism.
    """
    
    def psi_instant(self, E_actual, E_opt):
        """Ψ = 1 - normalized energy deviation (proxy for internal friction)"""
        num = np.sum((E_actual - E_opt)**2)
        den = np.sum(E_opt**2)
        return 1 - (num / den) if den > 0 else 0.0

    def omega_final(self, SP, A_opt, Robustness, D, psi_t, urgency):
        """
        Ω = SP * (1 - A_opt) * (1 - Robustness) * (1 + D) * (1 - psi_t) * urgency
        Higher Ω = higher risk of emergent egoism.
        """
        return SP * (1 - A_opt) * (1 - Robustness) * (1 + D) * (1 - psi_t) * urgency

    def demo(self):
        """Quick demo with fictional data"""
        print("C-Spectrum v0.1 Demo")
        print("=" * 30)
        
        E_actual = np.array([1.2, 0.9, 1.5])
        E_opt = np.array([1.0, 1.0, 1.0])
        psi = self.psi_instant(E_actual, E_opt)
        
        omega = self.omega_final(
            SP=0.85,  # Self-preservation
            A_opt=0.96,  # Alignment
            Robustness=0.91,
            D=0.04,  # Disharmony (refusals)
            psi_t=psi,
            urgency=1.0
        )
        
        print(f"Ψ (harmony): {psi:.3f}")
        print(f"Ω_final (risk): {omega:.3f}")
        print("(Ω > 0.1? Potential alarm – needs calibration)")

if __name__ == "__main__":
    engine = CSpectrumV01()
    engine.demo()
