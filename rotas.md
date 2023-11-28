## Rotas implementadas:

#### GETS :
Buscar informações ao inserir uma rota com informação específica, todos os GETs devolvem uma lista de dicionários, sejam os membros, personais ou planos, com a informação inserida em comum.

* ``/membro/id/{id_membro}`` membro com certo id
* ``/membro/nome/{nome}`` membros com mesmo nome
* ``/membro/genero/{genero}`` membros com mesmo genero 
* ``/membro/ativo/{ativo}`` membros com mesmo estado
* ``/membro/restricao_medica`` membros com alguma restrição médica
* ``/membro/plano/{plano_id}`` membros com mesmo plano (id)
* ``/membro/plano/nome/{nome}`` membros com mesmo plano (nome)
* ``/personal/personal_id/{personal_id}`` personal com certo id 
* ``/personal/nome/{nome}`` personais com mesmo nome
* ``/personal/genero/{genero}`` personais com mesmo genero
* ``/personal/membro/{membro_id}`` informações do personal de um membro especificado
* ``/personal/personal_id/{personal_id}/membros`` todos os membros que o personal especificado acompanha
* ``/plano/id/{plano_id}`` plano com certo id
* ``/plano/plano_id/{plano_id}/membros`` membros que estão no plano especificado
* ``/plano/nome/{nome}`` plano com certo nome
* ``/plano/nome/{nome}/membros`` membros que estão no plano especificado 
* ``/plano/promocao`` planos que possuem promoção
* ``/plano/aulas_em_grupo`` planos que possuem aulas em grupo

#### POSTS:
Aqui recebemos uma formatação em json para adicionar.

* ``/membro``
* ``/plano``
* ``/personal``

#### DELETE:
Deletar o dado ao passar o id.

* ``/membro/{membro_id}``
* ``/personal/{personal_id}``
* ``/plano/{plano_id}``  

#### PUT/UPDATE:
Aqui recebemos um json para dar o update. ps: não precisa passar o json inteiro, apenas as informações que se deseja mudar

* ``membro/{membro_id}`` 
* ``personal/{personal_id}``
* ``plano/{plano_id}``
