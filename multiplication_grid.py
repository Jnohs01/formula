import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title and explanation
st.title("Visual Multiplication Grid (3 × 4)")
st.write("This interactive demo shows how multiplication (like 3 × 4) can be visualized as an area.")

# Sidebar explanation panel
with st.sidebar:
    st.header("📚 Why This Matters")
    st.markdown("""
    **A formula is just a story we tell about a pattern.**  
    Long before calculators, ancient mathematicians literally **measured** triangles and circles to find values like sine and cosine.

    - The Greeks built **chord tables** to measure angles.
    - Indian mathematicians refined these into the **sine** function.
    - Before formulas, there were **tables**.  
      People had to **observe and record** each case — just like we're doing here.

    > You're not using magic. You're using **compressed patterns** that smart people noticed and explained.

    This grid below shows how multiplication is just **counting a block of squares**. From this, you can build toward understanding **area**, **algebra**, and even **calculus** — one pattern at a time.
    """)

# User input for dimensions
cols = st.slider("Choose width (columns):", 1, 12, 4)
rows = st.slider("Choose height (rows):", 1, 12, 3)

# Create the grid
grid = np.ones((rows, cols))

fig, ax = plt.subplots()
ax.imshow(grid, cmap="viridis", extent=[0, cols, 0, rows])

# Draw grid lines
for x in range(cols + 1):
    ax.axvline(x, color='white', lw=1)
for y in range(rows + 1):
    ax.axhline(y, color='white', lw=1)

ax.set_xticks([])
ax.set_yticks([])
ax.set_title(f"{rows} × {cols} = {rows * cols} squares")

st.pyplot(fig)
