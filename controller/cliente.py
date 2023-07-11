#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome_completo, cpf, data_nascimento, telefone, email, senha):
    db.cur.execute("""
                   INSERT into public.cadastrocurso (nome_completo, cpf, data_nascimento, telefone, email, senha)
                   VALUES ('%s','%s','%s','%s','%s','%s')
                   """ % (nome_completo, cpf, data_nascimento, telefone, email, senha))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM cadastrocurso
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows

#função para deletar registro no banco de dados
def deletar(email):
    db.cur.execute("""
                  DELETE FROM cadastrocurso WHERE email = '%s';
                  """ % (email))
    db.con.commit()

#funções para atualizar registro no banco de dados
def atualizar(nome_completo, cpf, data_nascimento, telefone, email, senha):
    db.cur.execute("""
                   UPDATE cadastrocurso SET nome_completo, cpf, data_nascimento, telefone, email, senha WHERE email = '%s';
                   """ % (email))
    db.con.commit()
