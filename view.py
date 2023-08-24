#importando SQLITE

import sqlite3 as lite




#CRUD
#CREATY= INSERIR/CRIAR
#READY = ACESSAR / MOSTRAR
#Update = ATUALIZAR
#DELETE = EXCLUIR





#criando conexão
con = lite.connect('cadastro.db')
lista= ['Guilherme Silva','guisilva@gmail.com', 34948802, "12/11/2023", 'Praia Grande', '157895', 'Problemas com o app']


#inserindo informacoes

def inserir_info(i):
    with con:
     cur= con.cursor()
     query = "INSERT INTO cadastroUsuario(nome,email,telefone, data, cidade, creci, assunto) VALUES(?,?,?,?,?,?,?)"
     cur.execute(query,i)





#acessar informacoes        
def mostrar_info():
    lista= []
    with con:   
        cur = con.cursor()
        query = "SELECT * FROM cadastroUsuario"
        cur.execute(query)
        informacao = cur.fetchall()
        
        for i in informacao:       
            lista.append(i)
    return lista



lista=['nome=joao',1]
#atualizar info

with con:
   cur= con.cursor()
   query = "UPDATE cadastroUsuario SET nome=? WHERE id=?"
   cur.execute(query,lista)



lista=[1]
#Deletar informacao

with con:
   cur= con.cursor()
   query = "DELETE FROM cadastroUsuario WHERE id=?"
   cur.execute(query,lista)