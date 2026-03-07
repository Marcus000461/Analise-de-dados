print("-----Bem-vindo ao sistema de cadastro de produtos!-----")
print("-----O sistema irá solicitar informações sobre os produtos que deseja cadastrar-----.")
print("-----Você pode cadastrar quantos produtos quiser. Para encerrar o cadastro, digite 'sair' quando solicitado o nome do produto.")

def cadastrar():
    lista_local = []
    
    while True:
        nome = input("\nDigite o nome do produto (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break 
            
        quantidade = int(input("Digite a quantidade: "))
        peso_unitario = float(input("Peso unitário (kg): "))
        litro = float(input("Litros: "))
        medida_unitario = float(input("Medida unitária (metros): "))
        abastecer = input("Precisa abastecer? (sim/não): ")
        data_entrada = input("Data (dd/mm/aaaa): ")
        
        total_kg = quantidade * peso_unitario
        total_metros = quantidade * medida_unitario
        
        produtos = {
            'nome': nome,
            'peso_total_kg': total_kg,
            'metros_totais': total_metros,
            'quantidade': quantidade,
            'litro': litro,
            'abastecer': abastecer,
            'data_entrada': data_entrada
            
        }
        
        lista_local.append(produtos)
        
        nomes_apenas = [p['nome'] for p in lista_local]
        print(f"✅ Produto '{nome}' cadastrado!")
        print(f"📋 Lista atual: {nomes_apenas}")
        print("-" * 30)

  
    return lista_local




estoque_final = cadastrar()


nomes_finais = [produto['nome'] for produto in estoque_final]

print("\n------- Cadastro de produtos encerrado.")
print(f"Produtos finais no sistema: {nomes_finais}")

def criar_categorias():
    
    categorias = {
        'Eletronicos': [],
        'Alimentos': [],
        'Bebidas': [],
        'Roupas': []
    }
    
    while True:
        nova_categoria = input("\nDigite o nome de uma nova categoria (ou 'sair' para encerrar): ")
        if nova_categoria.lower() == 'continuar':
            print("criando categorias...")
        if nova_categoria in categorias:
            print("Essa categoria já  existe. Tente outra.")
        else:
            categorias[nova_categoria] = []
            print(f"✅ Categoria '{nova_categoria}' criada!")
            categorias_criadas = criar_categorias()
            return categorias 
            