from scipy.stats import norm
from scipy.integrate import quad
fi=norm()
value,error=quad(fi.pdf,-2,2)
print(value)