# Exercio
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deepcopy (cópia profunda)

from copy import deepcopy

from dados import produtos

novos_produtos = [{**produto, 'preço': round(produto['preço'] * 1.1, 2)} for produto in deepcopy(produtos)]


print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

ordenado_por_nome = sorted(deepcopy(produtos), key=lambda produto: produto['nome'], reverse=True)

print(*ordenado_por_nome, sep='\n')
print()

# Ordene os produtos por preço crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

ordenado_por_preco = sorted(deepcopy(produtos), key=lambda produto: produto['preço'])

print(*ordenado_por_preco, sep='\n')