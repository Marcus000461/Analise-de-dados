import sqlite3

# Função para conectar e garantir que a tabela existe
def iniciar_banco():
    conexao = sqlite3.connect('escola_danca.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            estilo TEXT NOT NULL
        )
    ''')
    conexao.commit()
    return conexao

def menu():
    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE GESTÃO DE ALUNOS")
        print("="*30)
        print("1. Cadastrar Novo Aluno")
        print("1.2 Cadastrar Novo Professor")
    # Adicionando a opção de cadastrar professor
        print("1.3 Listar Todos os Professores")
        print("1.4 Remover Professor")
        print("2. Listar Todos os Alunos")
        print("3. Atualizar Estilo de Aluno")
        print("4. Remover Aluno")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        conn = iniciar_banco()
        cursor = conn.cursor()

        if opcao == "1":
            nome = input("Nome do Aluno: ")
            estilo = input("Estilo de Dança: ")
            cursor.execute('INSERT INTO alunos (nome, estilo) VALUES (?, ?)', (nome, estilo))
            conn.commit()
            print(f"✅ {nome} adicionado!")
            
        if opcao == "1.2":
            nome_professor = input("Nome do Professor: ")
            estilo_ensinado = input("Estilo de Dança Ensinado: ")
            # Aqui você pode criar uma tabela para professores e inserir os dados
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    estilo_ensinado TEXT NOT NULL
                )
            ''')
            cursor.execute('INSERT INTO professores (nome, estilo_ensinado) VALUES (?, ?)', (nome_professor, estilo_ensinado))
            conn.commit()
            print(f"✅ Professor {nome_professor} adicionado!")

        elif opcao == "1.3":
            cursor.execute('SELECT * FROM professores')
            rows = cursor.fetchall()
            print("\n--- LISTA DE PROFESSORES ---")
            for r in rows:
                print(f"ID: {r[0]} | Nome: {r[1]} | Estilo Ensinado: {r[2]}")
                
        elif opcao == "1.4":
            id_professor = input("Digite o ID do professor para remover: ")
            cursor.execute('DELETE FROM professores WHERE id = ?', (id_professor,))
            conn.commit()
            print("❌ Professor removido com sucesso.")

        elif opcao == "2":
            cursor.execute('SELECT * FROM alunos')
            rows = cursor.fetchall()
            print("\n--- LISTA DE ALUNOS ---")
            for r in rows:
                print(f"ID: {r[0]} | Nome: {r[1]} | Estilo: {r[2]}")

        elif opcao == "3":
            id_aluno = input("Digite o ID do aluno para atualizar: ")
            novo_estilo = input("Novo Estilo: ")
            cursor.execute('UPDATE alunos SET estilo = ? WHERE id = ?', (novo_estilo, id_aluno))
            conn.commit()
            print("🔄 Dados atualizados!")

        elif opcao == "4":
            id_aluno = input("Digite o ID do aluno para remover: ")
            cursor.execute('DELETE FROM alunos WHERE id = ?', (id_aluno,))
            conn.commit()
            print("❌ Aluno removido com sucesso.")

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            conn.close()
            break
        
        else:
            print("⚠️ Opção inválida!")
        
        conn.close()

# Executar o programa
if __name__ == "__main__":
    menu()