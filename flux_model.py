import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes


def concentration(x, L_axial, v, D, C0):
    transit_time = L_axial / v
    lambda_eff = np.sqrt(2 * D * transit_time)
    C = C0 * np.exp(-x / lambda_eff)
    return C


def flux(
    x: np.ndarray,
    C: np.ndarray,
    v: float,
    D: float,
):
    dCdx = np.gradient(C, x)
    Jd = -D * dCdx
    Jc = v * C
    Js = Jd + Jc

    return Js


def peclet(x, D, v):
    Pe = x * v / D
    return Pe


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    L_axial = 1  # mm
    L = 0.1  # mm
    C0 = 1.0  # mol/mm^3
    x = np.linspace(0.01 * L, L, 101)  # mm

    conditions = {
        "Normal": {"v": 1, "D": 1.8e-3},
        "Valsalva": {"v": 3, "D": 1.8e-3},  # Increased velocity
        "Fibrosis": {"v": 1, "D": 0.9e-3},  # Reduced diffusion
        "Valsalva+Fibrosis": {
            "v": 3,
            "D": 0.9e-3,
        },  # Increased velocity, Reduced diffusion
    }
    # Create subplots
    fig, axs = plt.subplots(1, 3, figsize=(18, 8))
    axs: list[matplotlib.axes.Axes]  # Denne linje giver bare typehints (liv==lettere)

    for i, (label, params) in enumerate(conditions.items()):
        v = params["v"]
        D = params["D"]

        # Flux components
        C = concentration(x, L_axial, v, D, C0)
        Js = flux(x, C, v, D)
        Pe = peclet(x, D, v)

        # Plot fluxes
        axs[0].plot(x * 1e3, Js, label=label)
        axs[0].set_title("Flux")
        axs[0].set_xlabel("Tissue barrier thickness (μm)")
        axs[0].set_ylabel("Flux [mol/mm²/s]")
        axs[0].grid(True)
        axs[0].legend()

        # Plot concentration
        axs[1].plot(x * 1e3, C, label=label)
        axs[1].set_title("Concentration")
        axs[1].set_xlabel("Tissue barrier thickness (μm)")
        axs[1].set_ylabel("Concentration [mol/mm³]")
        axs[1].grid(True)
        axs[1].legend()

        # Plot peclet
        if i == 0:
            axs[2].plot(
                x * 1e3,
                np.zeros_like(x),
                label="Diff./Conv. Barrier",
                linestyle="--",
                color="k",
            )

        axs[2].plot(x * 1e3, np.log10(Pe), label=label)
        axs[2].set_title("Peclet's Number")
        axs[2].set_xlabel("Tissue barrier thickness (μm)")
        axs[2].set_ylabel("Peclet Number")
        axs[2].grid(True)
        axs[2].legend()

    plt.tight_layout()
    plt.show()
