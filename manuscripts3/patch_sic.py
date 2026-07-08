import sys

path = "/home/mrnob0dy666/imsgct/ig-docs/manuscripts3/sic_povm_stark_hilbert12_v2.tex"
with open(path, 'r') as f:
    content = f.read()

# Fix Author
content = content.replace(r"\author{C.\ Lando\ Mills%}", r"\author{Lando$\otimes$⊙perator}")

# Fix abstract underbrace doubling if exists
content = content.replace(r"\underbrace{\text{Belnap multilattice}}_{\text{sorry-free}}_{\text{sorry-free}}", r"\underbrace{\text{Belnap multilattice}}_{\text{sorry-free}}")

# Fix margin runoff for Re(z12) and Im(z12)
old_re = r"\text{Re}(\text{z}_{12}) &= 0.1062796056214234892401116553199052855065537600966583358463645722893226773031270658298768906205486390\dots"
new_re = r"\text{Re}(\text{z}_{12}) &= \begin{array}[t]{l} 0.1062796056214234892401116553199052855065 \\ 537600966583358463645722893226773031 \\ 270658298768906205486390\dots \end{array}"

old_im = r"\text{Im}(\text{z}_{12}) &= 0.0001630310010432694399587406315542496470085181880359789886468190772718137350367343609800041113224716\dots"
new_im = r"\text{Im}(\text{z}_{12}) &= \begin{array}[t]{l} 0.000163031001043269439958740631554249 \\ 647008518188035978988646819077271813 \\ 7350367343609800041113224716\dots \end{array}"

content = content.replace(old_re, new_re)
content = content.replace(old_im, new_im)

with open(path, 'w') as f:
    f.write(content)
