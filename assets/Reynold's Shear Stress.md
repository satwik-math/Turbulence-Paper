# Reynolds Stress Tensor:

The Reynolds stress tensor $` \tau_{ij} `$ is a symmetric second-order tensor that describes the turbulent stresses in a fluid flow. It is defined by:
```math
\tau_{ij} = \overline{u_i' u_j'}
```
where:
- $` \tau_{ij} `$ is the Reynolds stress component in the $` i `$-$` j `$ direction,
- $` \overline{u_i' u_j'} `$ represents the statistical average of the product of the fluctuating velocity components $` u_i' `$ and $` u_j' `$ (i.e., deviations from the mean flow velocity) at a given point in the flow.

### Component-wise Contributions:

1. **Streamwise Component ($` \tau_{uu} `$)**:
   - This component represents the turbulent momentum transport along the streamwise direction (parallel to the mean flow).
   - Mathematically, it can be expressed as:
```math
   \tau_{uu} = \overline{u'^2}
```

2. **Spanwise Component ($` \tau_{vv} `$)**:
   - Represents the turbulent momentum transport in the spanwise direction (perpendicular to the mean flow).
   - Mathematically:
```math
 \tau_{vv} = \overline{v'^2}
```

3. **Normal Component ($` \tau_{ww} `$)**:
   - Corresponds to the turbulent momentum transport in the normal (vertical) direction.
   - Mathematically:
```math
 \tau_{ww} = \overline{w'^2}
```

4. **Shear Stresses ($` \tau_{ij} `$, $` i \neq j `$)**:
   - These components represent the transport of momentum between different flow directions due to shear.
   - Examples include $` \tau_{uv} `$, $` \tau_{uw} `$, and $` \tau_{vw} `$, which represent the momentum transport in the cross-stream directions.
   - Mathematically:
```math
\tau_{ij} = \overline{u_i' u_j'}
```

### Interpretation:

- Reynolds stress tensor components quantify the intensity and directionality of turbulent momentum transport in a fluid flow.
- Positive values indicate a net transfer of momentum in the positive direction of the respective axis, while negative values indicate the opposite.

The present code graphically elucidates contributions of Reynold's Shear Stress $` - \tau_{13} `$ at different quadrant components, where flow is happening in the horizontal direction $` u_{1} `$. A detailed description regarding this term and its formulation can be found <a href="https://www.ams.org/journals/qam/1945-03-01/S0033-569X-1945-11999-0/" style="font-size: 20px">here</a>.
