# %%
from matplotlib import pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.savefig("test.png")

# %%
_1 = "OCCCCSP"
__ = "NCCCNC"
_2 = "X"
_3 = "c1ccc(C(O))c(C)c1"
c_smi = "O=C(N1)C(CC2=CC=C(C=C2)OCC3=NC4=C(N3C)C=C(OC5=CC=C(C=C5)C)C=C4)SC1=O"
_4 = "c1ncccc1"
CCC = "X"
_5 = "[2H]C"
_6 = "F\C=C\F"

from rdkit import Chem

mol = Chem.MolFromSmiles(_3)
from rdkit.Chem import Draw

Draw.MolToImage(mol)
# %%

(
    "C",
    "H",
    "O",
    "N",
    "P",
    "S",
    "C[Cl]",
    "F",
    "C[Br]",
    "I",
    "[Na+]",
    "[Se]",
    "c1cccc1",
    "n1cccc1",
    "o1cccc1",
    "s1cccc1",
    "[Se]1cccc1",
    "[Si]",
)
(
    "[K]",
    "[Mg]",
)
