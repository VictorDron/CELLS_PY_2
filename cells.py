import numpy as np
import matplotlib.pyplot as plt

# Definição da função de transição de estado
def transition(state, rule):
    new_state = np.zeros_like(state)
    for i in range(1, state.shape[0] - 1):
        # Calcula o novo estado de acordo com a regra
        new_state[i] = rule[int(''.join(map(str, state[i-1:i+2])), 2)]
    return new_state

# Definição das variáveis
size = 100 # tamanho do autômato celular
steps = 100 # número de iterações
rule_number = 110 # número da regra

# Criação da matriz inicial com um único estado ativo no meio
state = np.zeros((steps, size))
state[0, size//2] = 1

# Criação da matriz de regras binárias
rule = np.array([int(x) for x in np.binary_repr(rule_number, 8)])

# Execução do autômato celular
for i in range(1, steps):
    state[i] = transition(state[i-1], rule)

# Plotagem do resultado
plt.imshow(state, cmap='binary')
plt.show()
